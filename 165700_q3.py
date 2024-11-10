# Class representing an employee
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated for {self.name} to ${self.salary:.2f}")

# Class representing a department
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employees in the department

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added to the '{self.department_name}' department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for '{self.department_name}' department: ${total_salary:.2f}")

    def display_all_employees(self):
        if not self.employees:
            print(f"No employees in the '{self.department_name}' department.")
        else:
            print(f"Employees in '{self.department_name}' department:")
            for employee in self.employees:
                employee.display_details()
                print("-" * 20)

# Sample department
department = Department("IT Department")

# Interactive menu function
def menu():
    while True:
        print("\nDepartment Management System Menu")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Update Employee Salary")
        print("4. Display Total Salary Expenditure")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter the employee's name: ")
            employee_id = input("Enter the employee's ID: ")
            salary = input("Enter the employee's salary: ")
            try:
                salary = float(salary)
                new_employee = Employee(name, employee_id, salary)
                department.add_employee(new_employee)
            except ValueError:
                print("Invalid salary input. Please enter a numeric value.")

        elif choice == '2':
            department.display_all_employees()

        elif choice == '3':
            employee_id = input("Enter the employee ID to update salary: ")
            for employee in department.employees:
                if employee.employee_id == employee_id:
                    new_salary = input("Enter the new salary: ")
                    try:
                        new_salary = float(new_salary)
                        employee.update_salary(new_salary)
                        break
                    except ValueError:
                        print("Invalid salary input. Please enter a numeric value.")
                        break
            else:
                print(f"Employee with ID {employee_id} not found.")

        elif choice == '4':
            department.calculate_total_salary_expenditure()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

# Run the menu function to start the program
menu()
