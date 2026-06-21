# Program to merge two sorted arrays

arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))

merged = arr1 + arr2
merged.sort()

print("Merged Array:", merged)