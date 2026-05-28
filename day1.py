#Qn1 =Find the sum of n natural number 
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)

#Qn2= Print multiplaction table of given number 
num= int(input("Enter the number"))

for i in range(1, 11):
    i= num * i
    print(i)

#QN = 3 find the factorial of the number 
num = int(input("Enter the number"))
fact = 1

for i in range(1 , num+1):
    fact *= i

print("Factorial = " ,fact)

#QN4 = count digit in the number 
num = int(input("Enter the number"))
count = 0
while num != 0:
    num = num//10
    count = count +1
    
print("toital digit is = ", count)


