
arr = list(map(int , input("Enter array element").split()))

for i in set(arr):
    print(f"frequncey of an {i} is {arr.count(i)}times")

