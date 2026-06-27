def student_record_system():
    students = []
    print("\n=== STUDENT RECORD SYSTEM ===")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '6':
            print("Exiting student system...")
            break
        
        elif choice == '1':
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            marks = input("Enter marks (comma-separated): ")
            marks_list = [float(m.strip()) for m in marks.split(',')]
            student = {"name": name, "roll": roll, "marks": marks_list}
            students.append(student)
            print(f"Student {name} added successfully!")
        
        elif choice == '2':
            if not students:
                print("No students found!")
            else:
                print("\n--- STUDENT LIST ---")
                for i, s in enumerate(students, 1):
                    avg = sum(s['marks'])/len(s['marks']) if s['marks'] else 0
                    print(f"{i}. {s['name']} (Roll: {s['roll']}) - Avg: {avg:.2f}")
        
        elif choice == '3':
            roll = input("Enter roll number to search: ")
            found = False
            for s in students:
                if s['roll'] == roll:
                    print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
                    found = True
                    break
            if not found:
                print("Student not found!")
        
        elif choice == '4':
            roll = input("Enter roll number to update: ")
            for s in students:
                if s['roll'] == roll:
                    s['name'] = input("Enter new name: ")
                    marks = input("Enter new marks (comma-separated): ")
                    s['marks'] = [float(m.strip()) for m in marks.split(',')]
                    print("Student updated successfully!")
                    break
            else:
                print("Student not found!")
        
        elif choice == '5':
            roll = input("Enter roll number to delete: ")
            for i, s in enumerate(students):
                if s['roll'] == roll:
                    del students[i]
                    print("Student deleted successfully!")
                    break
            else:
                print("Student not found!")
        
        else:
            print("Invalid choice!")


student_record_system()