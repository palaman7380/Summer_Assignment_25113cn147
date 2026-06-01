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
#Qn 3 = facter of the number
num = int(input("enter the number"))
temp = n
count=0
for i in range(1,temp):
    if temp%i==0:
        count=count+1
        
        
        print(count)
    
#Qn=4 lagest facter 
num = int(input("enter the number"))
temp = n
count=0
for i in range(1,temp):
    if temp%i==0:
        count=count+1
        
        
print(count)