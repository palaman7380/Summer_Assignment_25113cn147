#q4 remove dublicate array
arr = list(map(int ,input("enter the element").split()))
ans = []
n = len(arr)
for i in range(n-1):
    if arr[i]!= arr[i+1]:
        ans.append(i)
print(ans)


