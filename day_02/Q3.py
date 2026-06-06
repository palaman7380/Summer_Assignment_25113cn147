# Qno3 find the product of didgit 
num= int(input("enter the number "))

product = 1


while num>0:
    remainder= num%10
    product = product*remainder
    num = num//10

print("The product of number = ",product)

