arr = [1, 2, 3, 4, 5]
k = int(input("Enter rotation positions: "))
n = len(arr)
right = arr[-(k % n):] + arr[:-(k % n)]
print("Right Rotation:", right)