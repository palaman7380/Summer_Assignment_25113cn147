def mini_employee_system():
    employees = []
    print("\n=== EMPLOYEE MANAGEMENT ===")
    print("1. Add employee")
    print("2. View all employees")
    print("3. Search employee")
    print("4. Update salary")
    print("5. Delete employee")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '6':
            print("Exiting employee system...")
            break
        
        elif choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            try:
                salary = float(input("Enter salary: "))
                emp = {"id": emp_id, "name": name, "salary": salary}
                employees.append(emp)
                print(f"Employee {name} added successfully!")
            except ValueError:
                print("Invalid salary!")
        
        elif choice == '2':
            if not employees:
                print("No employees found!")
            else:
                print("\n--- EMPLOYEE LIST ---")
                for i, e in enumerate(employees, 1):
                    print(f"{i}. ID: {e['id']}, Name: {e['name']}, Salary: ${e['salary']:.2f}")
        
        elif choice == '3':
            emp_id = input("Enter employee ID to search: ")
            for e in employees:
                if e['id'] == emp_id:
                    print(f"ID: {e['id']}, Name: {e['name']}, Salary: ${e['salary']:.2f}")
                    break
            else:
                print("Employee not found!")
        
        elif choice == '4':
            emp_id = input("Enter employee ID to update salary: ")
            for e in employees:
                if e['id'] == emp_id:
                    try:
                        new_salary = float(input("Enter new salary: "))
                        e['salary'] = new_salary
                        print("Salary updated successfully!")
                    except ValueError:
                        print("Invalid salary!")
                    break
            else:
                print("Employee not found!")
        
        elif choice == '5':
            emp_id = input("Enter employee ID to delete: ")
            for i, e in enumerate(employees):
                if e['id'] == emp_id:
                    del employees[i]
                    print("Employee deleted successfully!")
                    break
            else:
                print("Employee not found!")
        
        else:
            print("Invalid choice!")


mini_employee_system()