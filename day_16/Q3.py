#q3 pair of given sum
arr = list(map(int , input("Enter array element").split()))
target = int(input("enter the target"))
n = len(arr)
for i in range(n-1):
    if arr[i]+ arr[i+1] == target:
        print("target is achieve")
    