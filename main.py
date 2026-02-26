print("--- Python OOP Project: Employee Management System ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department


def menu():
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")


person_obj = None
employee_obj = None
manager_obj = None


while True:
    menu()
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        person_obj = Person(name, age)   # <-- No error here
        print(f"\nPerson created with name: {name} and age: {age}.")

    elif choice == 2:
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        employee_obj = Employee(name, age, emp_id, salary)
        print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")

    elif choice == 3:
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        manager_obj = Manager(name, age, emp_id, salary, dept)
        print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")

    elif choice == 4:
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        detail_choice = int(input("Enter your choice: "))

        if detail_choice == 1 and person_obj:
            print("\nPerson Details:")
            print("Name:", person_obj.name)
            print("Age:", person_obj.age)

        elif detail_choice == 2 and employee_obj:
            print("\nEmployee Details:")
            print("Name:", employee_obj.name)
            print("Age:", employee_obj.age)
            print("Employee ID:", employee_obj.emp_id)
            print("Salary: $", employee_obj.salary)

        elif detail_choice == 3 and manager_obj:
            print("\nManager Details:")
            print("Name:", manager_obj.name)
            print("Age:", manager_obj.age)
            print("Employee ID:", manager_obj.emp_id)
            print("Salary: $", manager_obj.salary)
            print("Department:", manager_obj.department)
            
        elif detail_choice ==4:
            if manager:
                manager.display()
            elif employee:
                employee.display()
            elif person:
                person.display()
        else:
            print("\nNo data available!")

    elif choice == 5:
        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice.")

    print("\n--- Choose another operation ---")
