arr = list(map(int , input("Enter the array element : ").split()))

for i in set(arr):
    print(i ,":",arr.count(i))