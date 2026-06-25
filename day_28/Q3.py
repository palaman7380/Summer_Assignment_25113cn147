class Employee:
    employees = []

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"\nEmployee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : ₹{self.salary}")

    def annual_salary(self):
        return self.salary * 12


class SalaryManagement:

    def add_employee(self):
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Monthly Salary: "))

        emp = Employee(emp_id, name, salary)
        Employee.employees.append(emp)

        print("Employee Added Successfully!")

    def display_employees(self):
        if not Employee.employees:
            print("No Employee Found!")
        else:
            for emp in Employee.employees:
                emp.display()

    def update_salary(self):
        emp_id = int(input("Enter Employee ID: "))

        for emp in Employee.employees:
            if emp.emp_id == emp_id:
                new_salary = float(input("Enter New Salary: "))
                emp.salary = new_salary
                print("Salary Updated Successfully!")
                return

        print("Employee Not Found!")

    def annual_salary(self):
        emp_id = int(input("Enter Employee ID: "))

        for emp in Employee.employees:
            if emp.emp_id == emp_id:
                print(f"Annual Salary = ₹{emp.annual_salary()}")
                return

        print("Employee Not Found!")

    def main(self):
        while True:
            print("\n===== SALARY MANAGEMENT SYSTEM =====")
            print("1. Add Employee")
            print("2. Display Employees")
            print("3. Update Salary")
            print("4. Calculate Annual Salary")
            print("5. Exit")

            choice = input("Enter Choice: ")

            if choice == '1':
                self.add_employee()

            elif choice == '2':
                self.display_employees()

            elif choice == '3':
                self.update_salary()

            elif choice == '4':
                self.annual_salary()

            elif choice == '5':
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")


obj = SalaryManagement()
obj.main()