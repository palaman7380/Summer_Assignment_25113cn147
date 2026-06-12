arr = list(map(int , input("Enter the array element : ").split()))
sec_largest = -1
largest = arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
        sec_largest = largest
        largest= arr[i]
    elif arr[i]> sec_largest and arr[i] != largest:
        sec_largest = arr[i]
if sec_largest == -1:
    print(False)
else:
    print("second largest element : ", sec_largest)

        
        
        