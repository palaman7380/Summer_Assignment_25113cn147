#Qn2 = find the sum of digit of the number
num = int(input("Enter teh number "))

sum = 0
while num>0:
    n = num%10
    sum = sum + n
    num = num/10

print("sum of digit is = ",sum)