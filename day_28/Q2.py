# employ management system
class employee:
    employees = []
    def __init__(self,name, emp_id, emp_sal, work):
        self.name = name
        self.__emp_id = emp_id
        self.__emp_sal = emp_sal
        self.work = work
        self.main()
 
    @classmethod
    def add_emp(cls):
        name = input("enter the name")
        emp_id = input("enter emply id ")
        emp_sal = int(input("enter the emp_saley"))
        emp_work= input("Enter the work")
        emp = employee(name,emp_id,emp_sal,emp_work)
        cls.employees.append(emp)
        print("employ added succesfully")
        self.main()


    @classmethod
    def emp_dis(cls):
        if not cls.employees:
            print("data not found")
            return
        print("\n===== EMPLOYEE LIST =====")
        for emp in cls.employees:
            emp.display()

            
        
    @classmethod
    
    def update_det(cls):
        update_id = input("enter the new id")

        for emp in cls.employees:
            if emp._employee__emp_id == update_id:

                new_name = input("Enter New Name: ")
                new_salary = int(input("Enter New Salary: "))
                new_work = input("Enter New Work: ")

                emp.name= new_name
                emp._Employee__emp_sal = new_salary
                emp.work = new_work

                print("Data added succesfullly")
                return

        print("data not found")



    @classmethod
    def delete_employee(cls):
        delete_id = input("Enter Employee ID to Delete: ")

        for emp in cls.employees:
            if emp._employee__emp_id == delete_id:
                cls.employees.remove(emp)

                print("✅ Employee Deleted Successfully!")
                return

        print(" Employee Not Found!")

    @classmethod
    def count_employee(cls):
        print(f"Total Employees = {len(cls.employees)}")



            
while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Count Employees")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee.add_emp()

    elif choice == "2":
        employee.emp_dis()

    
    elif choice == "3":
        employee.update_det()

    elif choice == "4":
        employee.delete_employee()

    elif choice == "5":
        employee.count_employee()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
        
       
