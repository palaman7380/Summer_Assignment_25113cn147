def array_operations():
    arr = []
    print("\n=== ARRAY OPERATIONS ===")
    print("1. Insert element")
    print("2. Delete element")
    print("3. Search element")
    print("4. Display array")
    print("5. Sort array")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '6':
            print("Exiting...")
            break
        
        elif choice == '1':
            try:
                elem = int(input("Enter element to insert: "))
                arr.append(elem)
                print(f"{elem} inserted successfully!")
            except ValueError:
                print("Invalid input! Enter integer.")
        
        elif choice == '2':
            if not arr:
                print("Array is empty!")
                continue
            try:
                elem = int(input("Enter element to delete: "))
                if elem in arr:
                    arr.remove(elem)
                    print(f"{elem} deleted successfully!")
                else:
                    print("Element not found!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == '3':
            if not arr:
                print("Array is empty!")
                continue
            try:
                elem = int(input("Enter element to search: "))
                if elem in arr:
                    print(f"{elem} found at position {arr.index(elem) + 1}")
                else:
                    print("Element not found!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == '4':
            if not arr:
                print("Array is empty!")
            else:
                print(f"Array: {arr}")
        
        elif choice == '5':
            if not arr:
                print("Array is empty!")
            else:
                arr.sort()
                print(f"Sorted array: {arr}")
        
        else:
            print("Invalid choice!")

array_operations()