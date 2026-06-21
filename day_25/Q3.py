# Program to sort names alphabetically

names = input("Enter names separated by space: ").split()

names.sort()

print("Sorted Names:")
for name in names:
    print(name)