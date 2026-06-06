#Qn 1 = Perfect number
num = int(input("Enter the number"))
sum = 0
for i in range(1,num):
    if num %i==0:
        sum = sum +i 

    elif sum == num:

     print("Perfect number")
    else:
     print(False)
