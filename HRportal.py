import json

users = {
    "admin":{"password": "1234", "role": "admin"},
    "user": {"password": "1111", "role": "user"}
}
try:
    with open("employees.json", "r") as file:
        employees = json.load(file)
except:
    employees =[]

def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users and users[username]["password"] == password:
        print("Login successful")
        return users[username]["role"]
    
    print("Invalid login!")
    return None

def save_data():
    with open("employees.json", "w") as file:
        json.dump(employees,file)

def find_employee(emp_id):
    for i in employees:
        if i["id"] == emp_id:
            return i
    return None

def is_empty(*inputs):
    for i in inputs:
        if i.strip() == "":
            return True
    return False

def no_employees():
    if len(employees) == 0:
        print("No employees found!")
        return True
    return False

def add_employee():
    emp_id = input("Enter employee id: ").strip()
    name = input("Enter employee name(first and last name): ").strip().title()
    dept = input("Enter employee department: ").strip()
    salary = input("Enter employee salary: ").strip()

    if is_empty(emp_id,name,dept,salary):
        print("Invalid input!")
        return
    
    if not salary.isdigit():
        print("Salary must be a number")
        return
    
    
    if find_employee(emp_id):
        print("Employee already exists!")
        return
    
    name_parts = name.split()

   
    if len(name_parts) != 2:
        print("Please only enter first and last name")
        return
    
    first, last = name_parts

    if not first.isalpha() or not last.isalpha():
        print("Name must contain only letters")
        return
    
    name = first.title()+" "+last.title()

    employees.append({
        "id": emp_id,
        "name": name,
        "department": dept,
        "salary": int(salary)
        })

    save_data()
    print("Employee added")

def show_employees():
    print("\nAll employees:")

    if no_employees():
        return
    
    for i in employees:
        print(
            i["id"],
            ":",
            i["name"],
            ":",
            i["department"],
            ":",
            i["salary"]
            )

def search_employee():
    search_name = input("Enter employee name to search: ").strip().lower()

    if is_empty(search_name):
        print("Ivalid input!")
        return
    
    if no_employees():
        return
    
    
    found = False

    for i in employees:
        if search_name in i["name"].lower():
            print(
            i["id"],
            ":",
            i["name"],
            ":",
            i["department"],
            ":",
            i["salary"]
            )
            found = True

    if not found:
        print("Employee not found!")


def delete_employee():

    if no_employees():
        return
    
    delete_id = input("Enter employee id to delete: ").strip()

    if is_empty(delete_id):
        print("Invalid input!")
        return
    
    emp = find_employee(delete_id)

    if not emp:
        print("Employee not found!")
        return
    
    employees.remove(emp)

    save_data()

    print("Employee deleted:", emp["name"])


def update_department():
    if no_employees():
        return
    
    update_id = input("Enter employee id to update department: ").strip()

    if is_empty(update_id):
        print("Invalid input!")
        return
    
    emp = find_employee(update_id)

    if not emp:
        print("Employee not found!")
        return
    
    new_dept = input("Enter new department: ").strip()

    if is_empty(new_dept):
        print("Invalid input!")
        return
    
    old_dept = emp["department"]
    emp["department"] = new_dept.title()

    save_data()

    print("\nDepartment updated")
    print("Old department:",  old_dept)
    print("New department:", emp["department"])
    

def update_employee_id():
    if no_employees():
        return
    
    current_id = input("Enter employee id to update: ").strip()

    if is_empty(current_id):
        print("Invalid input!")
        return
    
    emp = find_employee(current_id)

    if not emp:
        print("Employee not found!")
        return
    
    new_id = input("Enter new id: ").strip()

    if is_empty(new_id):
        print("Invalid input!")
        return
    
    if new_id == emp["id"]:
        print("New id is same as old id")
        return
    
    if find_employee(new_id):
        print("Id already exists!")
        return
    
    old_id = emp["id"]
    emp["id"] = new_id

    save_data()

    print("\nId updated")
    print("Old id:", old_id)
    print("New id:", emp["id"])

def employees_by_department():

    if no_employees():
        return
    
    dept = input("Enter the department: ").strip()

    if is_empty(dept):
        print("Invalid input!")
        return
    
    dept = dept.title()

    found = False

    print("\nAll employees of", dept)
    for i in employees:
        if i["department"] == dept:
            print(
            i["id"],
            ":",
            i["name"],
            ":",
            i["department"],
            ":",
            i["salary"]
            )
            found = True


    if not found:
        print("No employees found in this department:", dept)


def highest_salary():

    if no_employees():
        return
    
    highest = employees[0]

    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

    print(
        highest["id"],
        ":",
        highest["name"],
        ":",
        highest["department"],
        ":",
        highest["salary"]
    )

def lowest_salary():

    if no_employees():
        return
    
    lowest = employees[0]

    for emp in employees:
        if emp["salary"] < lowest["salary"]:
            lowest = emp

    print(
        lowest["id"],
        ":",
        lowest["name"],
        ":",
        lowest["department"],
        ":",
        lowest["salary"]
    )


def average_salary():

    if no_employees():
        return
    
    total = 0

    for emp in employees:
        total += emp["salary"]

    avg = total / len(employees)

    print("\nAverage salary:", round(avg, 2))


def update_salary():

    if no_employees():
        return
    
    emp_id = input("Enter employee id to update salary: ").strip()

    if is_empty(emp_id):
        print("Invalid input!")
        return
    
    emp = find_employee(emp_id)

    if not emp:
        print("Employee not found!")
        return
    
    new_salary = input("Enter new amount of salary: ").strip()

    if is_empty(new_salary):
        print("Invalid input!")
        return
    
    if not new_salary.isdigit():
        print("Salary must be in a number")
        return
    
    if emp["salary"] == int(new_salary):
        print("New salary is same as old salary")
        return
    
    old_salary = emp["salary"]

    emp["salary"] = int(new_salary)

    save_data()

    print("\nSalary updated")
    print("Old salary:", old_salary)
    print("New salary:", emp["salary"])


def salary_raise():

    if no_employees():
        return
    
    emp_id = input("Enter employee id: ").strip()

    if is_empty(emp_id):
        print("Invalid input!")
        return
    
    emp = find_employee(emp_id)

    if not emp:
        print("Employee not found!")
        return
    
    raise_amount = input("Enter the raise amount: ").strip()

    if is_empty(raise_amount):
        print("Invalid input!")
        return
    
    if not raise_amount.isdigit():
        print("Raise amount must be a number")
        return
    
    if int(raise_amount) <= 0:
        print("Raise amount must be greater than 0")
        return
    
    old_salary = emp["salary"]

    emp["salary"] += int(raise_amount)

    save_data()

    print("\nRaise added successfully")
    print("Old salary:", old_salary)
    print("New salary:", emp["salary"])

def salary_cut():

    if no_employees():
        return
    
    emp_id = input("Enter employee id: ").strip()

    if is_empty(emp_id):
        print("Invalid input!")
        return
    
    emp = find_employee(emp_id)

    if not emp:
        print("Employee not found!")
        return
    
    cut_amount = input("Enter cut amount: ").strip()

    if is_empty(cut_amount):
        print("Invalid input!")
        return
    
    if not cut_amount.isdigit():
        print("Cut amount must be a number")
        return

    cut_amount = int(cut_amount)

    if cut_amount <= 0:
        print("Cut amount must be greater than 0")
        return
    
    old_salary = emp["salary"]
    new_salary = old_salary - cut_amount

    if new_salary < 0:
        print("Salary can not be in negative")
        return

    emp["salary"] = new_salary
    
    save_data()

    print("\nSalary cut successfully")
    print("Old salary:", old_salary)
    print("New salary:", emp["salary"])


def sort_by_salary():

    if no_employees():
        return
    
    sorted_employees = sorted(
        employees,
        key = lambda emp: emp["salary"],
        reverse = True
    )
    
    print("\nEmployees based salary(highest to lowest):")
    for emp in sorted_employees:
        print(
            emp["id"],
            ":",
            emp["name"],
            ":",
            emp["department"],
            ":",
            emp["salary"]
        )

def sort_by_name():

    if no_employees():
        return
    
    sorted_employees =sorted(
        employees,
        key = lambda emp: emp["name"]
    )

    print("\nEmployees based name(A to Z):")
    for emp in sorted_employees:
        print(
            emp["id"],
            ":",
            emp["name"],
            ":",
            emp["department"],
            ":",
            emp["salary"]
        )

def department_count():

    if no_employees():
        return
    
    counts = {}

    for emp in employees:
        dept = emp["department"]

        if dept in counts:
            counts[dept] += 1
        else:
            counts[dept] = 1

    print("\nEmployees per department:")

    for dept, count in counts.items():
        print(dept,":",count)
    


    






def main(role):

    while True:

        print("\n ===== Employee System =====")

        if role == "admin":
            print("1. Add employee")
            print("2. Show employees")
            print("3. Search employee")
            print("4. Delete employee")
            print("5. Update department")
            print("6. Update employee id")
            print("7. Employees by department")
            print("8. Highest salary")
            print("9. Lowest salary")
            print("10. Average salary")
            print("11. Update salary")
            print("12. Salary raise")
            print("13. Salary cut")
            print("14. Sort by salary")
            print("15. Sort by name")
            print("16. Department count")
            print("17. Exit")

        elif role == "user":
            print("1. Show employees")
            print("2. Search employee")
            print("3. Exit")

        
        choice = input("Enter your choice: ").strip()

        if role == "admin":

            if choice == "1":
                add_employee()

            elif choice == "2":
                show_employees()
            
            elif choice == "3":
                search_employee()

            elif choice == "4":
                delete_employee()

            elif choice == "5":
                update_department()

            elif choice == "6":
                update_employee_id()

            elif choice == "7":
                employees_by_department()

            elif choice == "8":
                highest_salary()

            elif choice == "9":
                lowest_salary()

            elif choice == "10":
                average_salary()

            elif choice == "11":
                update_salary()

            elif choice == "12":
                salary_raise()

            elif choice == "13":
                salary_cut()

            elif choice == "14":
                sort_by_salary()
            
            elif choice == "15":
                sort_by_name()

            elif choice == "16":
                department_count()

            elif choice == "17":
                break

        if role == "user":

            if choice == "1":
                show_employees()

            elif choice == "2":
                search_employee()

            elif choice == "3":
                break

role = login()

if role is None:
    exit()

main(role)       