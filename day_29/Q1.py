def calculator():
    print("\n=== CALCULATOR ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting calculator...")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue
        
        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")

calculator()