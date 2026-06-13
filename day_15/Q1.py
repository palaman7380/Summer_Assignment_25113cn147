arr = list(map(int , input("Enter the array element : ").split()))
reverse = []
for i in range(len(arr)-1 ,-1,-1):
    reverse.append(arr[i])

print(f"reverse of arr{arr}: is {reverse}")

