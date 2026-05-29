#Qn2 = find the sum of digit of the number
num = int(input("Enter teh number "))

sum = 0
while num>0:
    n = num%10
    sum = sum + n
    num = num/10

print("sum of digit is = ",sum)

#Qn02 = write a prgram of recerse number
num= int(input("enter the number "))

reverse = 0
while num>0:
    remainder= num%10
    reverse = (reverse *10) + remainder
    num = num//10

print("The reverse of number = ",reverse)

# Qno3 find the product of didgit 
num= int(input("enter the number "))

product = 1


while num>0:
    remainder= num%10
    product = product*remainder
    num = num//10

print("The product of number = ",product)



