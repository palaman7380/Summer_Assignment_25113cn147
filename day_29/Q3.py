def string_operations():
    print("\n=== STRING OPERATIONS ===")
    print("1. Find length")
    print("2. Reverse string")
    print("3. Count vowels")
    print("4. Check palindrome")
    print("5. Convert case")
    print("6. Count words")
    print("7. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '7':
            print("Exiting...")
            break
        
        text = input("Enter a string: ")
        
        if choice == '1':
            print(f"Length: {len(text)}")
        
        elif choice == '2':
            print(f"Reversed: {text[::-1]}")
        
        elif choice == '3':
            vowels = "aeiouAEIOU"
            count = sum(1 for char in text if char in vowels)
            print(f"Vowels: {count}")
        
        elif choice == '4':
            if text == text[::-1]:
                print(f"'{text}' is a palindrome")
            else:
                print(f"'{text}' is not a palindrome")
        
        elif choice == '5':
            print(f"Uppercase: {text.upper()}")
            print(f"Lowercase: {text.lower()}")
        
        elif choice == '6':
            words = text.split()
            print(f"Words: {len(words)}")
        
        else:
            print("Invalid choice!")
            
string_operations()