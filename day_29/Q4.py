def inventory_management():
    inventory = {}
    print("\n=== INVENTORY MANAGEMENT ===")
    print("1. Add item")
    print("2. Update quantity")
    print("3. View inventory")
    print("4. Search item")
    print("5. Delete item")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '6':
            print("Exiting inventory system...")
            break
        
        elif choice == '1':
            name = input("Enter item name: ").strip()
            if name in inventory:
                print("Item already exists!")
            else:
                try:
                    qty = int(input("Enter quantity: "))
                    inventory[name] = qty
                    print(f"{name} added with quantity {qty}")
                except ValueError:
                    print("Invalid quantity!")
        
        elif choice == '2':
            name = input("Enter item name: ").strip()
            if name not in inventory:
                print("Item not found!")
            else:
                try:
                    qty = int(input("Enter new quantity: "))
                    inventory[name] = qty
                    print(f"{name} quantity updated to {qty}")
                except ValueError:
                    print("Invalid quantity!")
        
        elif choice == '3':
            if not inventory:
                print("Inventory is empty!")
            else:
                print("\n--- INVENTORY ---")
                for item, qty in inventory.items():
                    print(f"{item}: {qty}")
        
        elif choice == '4':
            name = input("Enter item name to search: ").strip()
            if name in inventory:
                print(f"{name}: {inventory[name]} units")
            else:
                print("Item not found!")
        
        elif choice == '5':
            name = input("Enter item name to delete: ").strip()
            if name in inventory:
                del inventory[name]
                print(f"{name} deleted successfully!")
            else:
                print("Item not found!")
        
        else:
            print("Invalid choice!")


inventory_management()