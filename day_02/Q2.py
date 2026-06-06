#Qn02 = write a prgram of recerse number
num= int(input("enter the number "))

reverse = 0
while num>0:
    remainder= num%10
    reverse = (reverse *10) + remainder
    num = num//10

print("The reverse of number = ",reverse)
