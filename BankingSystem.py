import json

try:
    with open("accounts.json", "r") as file:
        accounts = json.load(file)

except FileNotFoundError:
    accounts = []


def save_data():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)


def is_empty(*inputs):
    for i in inputs:
        if i.strip() == "":
            return True
    return False


def no_accounts():
    if len(accounts) == 0:
        print("No account found!")
        return True
    return False



def find_account(id):
    for account in accounts:
        if account["id"] == id:
            return account
    return None


def create_account():

    account_id = input("Enter account id: ").strip()
    name = input("Enter account holder name: ").strip().title()
    balance = input("Enter initial balance: ").strip()

    if is_empty(account_id, name, balance):
        print("Invalid input!")
        return 

    if not account_id.isdigit():
        print("Account id must contain only numbers.")
        return


    for account in accounts:
        if account["id"] == account_id:
            print("Account id already exists.")
            return

    try:
        balance = int(balance)
    except ValueError:
        print("Balance must be a number.")
        return

    if balance < 0:
        print("Balance cannot be negative.")
        return

    accounts.append({
        "id": account_id,
        "name": name,
        "balance": balance,
        "transactions": []
    })

    save_data()
    print("Account created successfully.")



def show_accounts():
    if no_accounts():
        return

    print("All accounts:")
    for account in accounts:
        print(account["id"],
              ":",
              account["name"],
              ": Balance: ",
              account["balance"]
              )


def search_account():
    account_id = input("Enter account id to search: ").strip()

    if is_empty(account_id):
        print("Invalid input!")
        return

    account = find_account(account_id)

    if account is None:
        print("Account not found!")
        return

    print("Account found!")
    print("ID", account["id"])
    print("Name", account["name"])
    print("Balance", account["balance"])


def deposit_money():
    account_id = input("Enter account id: ").strip()
    amount = input("Enter deposit amount: ").strip()

    if is_empty(account_id, amount):
        print("Invalid input!")
        return

    account = find_account(account_id)

    if account is None:
        print("Account not found!")
        return

    try:
        amount = int(amount)
    except ValueError:
        print("Deposit amount must be a number.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return

    account["balance"] += amount
    account["transactions"].append(f"Deposited ${amount}")
    save_data()

    print("Deposit successful.")

def withdraw_money():
    account_id = input("Enter account id: ").strip()
    amount = input("Enter withdrawal amount: ").strip()

    if is_empty(account_id, amount):
        print("Invalid input!")
        return

    account = find_account(account_id)

    if account  is None:
        print("Account not found!")
        return

    try:
        amount = int(amount)
    except ValueError:
        print("Amount must be a number")
        return

    if amount <= 0:
        print("Amount cannot be zero or negative!")
        return

    if amount > account["balance"]:
        print("Insufficient funds!")
        return

    account["balance"] -= amount
    account["transactions"].append(f"Withdrawn ${amount}")
    save_data()

    print("Withdraw successful")


def transfer_money():
    from_id = input("Enter sender account id: ").strip()
    to_id = input("Enter receiver account id: ").strip()
    amount = input("Enter transfer amount: ").strip()

    if is_empty(from_id, to_id, amount):
        print("Invalid input!")
        return

    sender = find_account(from_id)

    if sender is None:
        print("Sender account not found!")
        return

    receiver = find_account(to_id)

    if receiver is None:
        print("Receiver account not found!")
        return

    try:
        amount = int(amount)
    except ValueError:
        print("Amount must be a number!")
        return

    if amount <= 0:
        print("Amount cannot be zero or negative!")
        return

    if amount > sender["balance"]:
        print("Amount exceeds account current balance!")
        return

    sender["balance"] -= amount
    sender["transactions"].append(f"Transferred ${amount}")
    receiver["balance"] += amount
    receiver["transactions"].append(f"Received ${amount}")
    save_data()
    print("Transfer successful")


def show_transactions():
    account_id = input("Enter account id to show transactions: ").strip()

    if is_empty(account_id):
        print("Invalid input!")
        return

    account = find_account(account_id)

    if account is None:
        print("Account not found!")
        return

    print("Transactions:")

    if len(account["transactions"]) == 0:
        print("No transactions found!")
        return
    
    for transaction in account["transactions"]:
        print(transaction)


def delete_account():
    account_id = input("Enter account id to delete: ").strip()

    if is_empty(account_id):
        print("Invalid input!")
        return

    account = find_account(account_id)

    if account is None:
        print("Account not found!")
        return


    accounts.remove(account)
    save_data()

    print("Account deleted successfully")


def richest_account():
    if no_accounts():
        return

    richest = None

    for account in accounts:
        if richest is None or account["balance"] > richest["balance"]:
            richest = account

    print("Richest account:")
    print("ID: ", richest["id"])
    print("Name: ", richest["name"])
    print("Balance: ", richest["balance"])


def total_bank_balance():
    if no_accounts():
        return

    total = 0

    for account in accounts:
        total += account["balance"]

    print("Total money in bank: ", total)


def menu():
    while True:
        print("\nBanking system:")
        print("1. Create account")
        print("2. Show accounts")
        print("3. Search account")
        print("4. Deposit money")
        print("5. Withdraw money")
        print("6. Transfer money")
        print("7. Show transactions")
        print("8. Delete account")
        print("9. Richest account")
        print("10. Total bank balance")
        print("11. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            show_accounts()
        elif choice == "3":
            search_account()
        elif choice == "4":
            deposit_money()
        elif choice == "5":
            withdraw_money()
        elif choice == "6":
            transfer_money()
        elif choice == "7":
            show_transactions()
        elif choice == "8":
            delete_account()
        elif choice == "9":
            richest_account()
        elif choice == "10":
            total_bank_balance()
        elif choice == "11":
            break
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    menu()
        

