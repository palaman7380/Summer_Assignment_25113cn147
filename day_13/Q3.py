arr = list(map(int , input("Enter the array element : ").split()))
n = len(arr)
arr.sort
largest = arr[0]
for i in range(1 ,n):
    if arr[i] > largest:
        largest = arr[i]
    # else:
    #     print(False)
        
print("Largest element is : " , largest)