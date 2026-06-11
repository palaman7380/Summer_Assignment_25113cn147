arr = list(map(int , input("Enter the array element : ").split()))
n = len(arr)
count = 0
odd = 0
for i in range(n):
    if arr[i]%2 == 0:
        count = count + 1
    else:
        odd = odd +1
        

print("even number of element= ",count)
print("Odd number of element = " ,odd)