#Qn=2 Strong number
n = int(input("Enter the number"))
temp = n
sum_fact = 0
while temp>0:
    digit = temp%10
    fact = 1
    for i in range(1 ,digit+1):
        fact = fact *i
    sum_fact = sum_fact + fact
    temp = temp//10

if sum_fact == n:
    print("it is strong number")
else:
    print(False)