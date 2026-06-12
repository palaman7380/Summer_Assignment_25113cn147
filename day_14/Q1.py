arr = list(map(int , input("Enter the array element : ").split()))
idx = 0
n = len(arr)
element = int(input("enter the element"))
for i in range(n):
    if element == arr[i]:
        idx = i+1
        break

if idx == 0:
    print("searching succesfull")
else:
    print(f"element find {idx} location")
