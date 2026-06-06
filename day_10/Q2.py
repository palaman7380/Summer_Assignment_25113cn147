num=int(input("enter number of rows"))
for i in range(num , -1,-1):
    for j in range(i ,num):
        print(" " , end="")
    for j in range(2*i+1):
        print("*" , end =" ")
    print()