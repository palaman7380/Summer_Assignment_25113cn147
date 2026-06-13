arr = [1, 2, 3, 4, 5]
k = int(input("Enter rotation positions: "))
n = len(arr)

# Left rotation
left = arr[k % n:] + arr[:k % n]
print("Left Rotation:", left)
