def mini_library():
    library = {}
    print("\n=== MINI LIBRARY SYSTEM ===")
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. View all books")
    print("5. Search book")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '6':
            print("Exiting library...")
            break
        
        elif choice == '1':
            title = input("Enter book title: ").strip()
            if title in library:
                print("Book already exists!")
            else:
                author = input("Enter author name: ")
                library[title] = {"author": author, "status": "Available"}
                print(f"'{title}' added successfully!")
        
        elif choice == '2':
            title = input("Enter book title to borrow: ").strip()
            if title not in library:
                print("Book not found!")
            elif library[title]["status"] == "Borrowed":
                print("Book is already borrowed!")
            else:
                library[title]["status"] = "Borrowed"
                print(f"'{title}' borrowed successfully!")
        
        elif choice == '3':
            title = input("Enter book title to return: ").strip()
            if title not in library:
                print("Book not found!")
            elif library[title]["status"] == "Available":
                print("Book is already in library!")
            else:
                library[title]["status"] = "Available"
                print(f"'{title}' returned successfully!")
        
        elif choice == '4':
            if not library:
                print("Library is empty!")
            else:
                print("\n--- LIBRARY ---")
                for title, info in library.items():
                    print(f"'{title}' by {info['author']} - {info['status']}")
        
        elif choice == '5':
            title = input("Enter book title to search: ").strip()
            if title in library:
                info = library[title]
                print(f"'{title}' by {info['author']} - {info['status']}")
            else:
                print("Book not found!")
        
        else:
            print("Invalid choice!")


mini_library()