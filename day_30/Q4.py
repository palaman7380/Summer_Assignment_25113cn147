def student_grade_manager():
    students = {}
    print("\n=== STUDENT GRADE MANAGER ===")
    print("1. Add student")
    print("2. Add grade")
    print("3. Calculate average")
    print("4. View student grades")
    print("5. Top performer")
    print("6. View all students")
    print("7. Exit")
    
    def calculate_average(grades):
        return sum(grades) / len(grades) if grades else 0
    
    while True:
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '7':
            print("Exiting grade manager...")
            break
        
        elif choice == '1':
            name = input("Enter student name: ").strip()
            if name in students:
                print("Student already exists!")
            else:
                students[name] = []
                print(f"Student {name} added!")
        
        elif choice == '2':
            name = input("Enter student name: ").strip()
            if name not in students:
                print("Student not found!")
            else:
                try:
                    grade = float(input("Enter grade: "))
                    students[name].append(grade)
                    print(f"Grade {grade} added for {name}")
                except ValueError:
                    print("Invalid grade!")
        
        elif choice == '3':
            name = input("Enter student name: ").strip()
            if name not in students:
                print("Student not found!")
            else:
                if not students[name]:
                    print("No grades available!")
                else:
                    avg = calculate_average(students[name])
                    print(f"{name}'s average grade: {avg:.2f}")
        
        elif choice == '4':
            name = input("Enter student name: ").strip()
            if name not in students:
                print("Student not found!")
            else:
                if not students[name]:
                    print("No grades available!")
                else:
                    print(f"{name}'s grades: {students[name]}")
                    print(f"Average: {calculate_average(students[name]):.2f}")
        
        elif choice == '5':
            if not students:
                print("No students found!")
            else:
                top_student = None
                top_avg = -1
                for name, grades in students.items():
                    avg = calculate_average(grades)
                    if avg > top_avg:
                        top_avg = avg
                        top_student = name
                if top_student:
                    print(f"Top performer: {top_student} (Avg: {top_avg:.2f})")
        
        elif choice == '6':
            if not students:
                print("No students found!")
            else:
                print("\n--- ALL STUDENTS ---")
                for name, grades in students.items():
                    avg = calculate_average(grades)
                    grade_count = len(grades)
                    print(f"{name}: {grade_count} grades, Avg: {avg:.2f}")
        
        else:
            print("Invalid choice!")


student_grade_manager()