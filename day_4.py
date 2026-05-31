#Qn1 = find Fabbonacci number 
num =int(input("Enter the number "))
a = 0 
b = 1 
i = 2
if(num==0 or num<0):
    print(False)
elif(num==1):
    print(a)
else:
    print(a,b,end="")
    
    while i< num:
        c = a+b
        i+=1
        print(c,end="")
        a=b
        b=c
# Qno2 = Term of fabbonacci
num =int(input("Enter the term "))
a = 0 
b = 1 
i = 2
if(num==0 or num<0):
    print(False)
elif(num==1):
    print(a)
else:
    
    
    while i< num:
        c = a+b
        i+=1

        a=b
        b=c
print(c)
#Qn3 = Aremstron number
num= int(input("Enter the number "))
temp = num
sum=0 #sum where number is add
n= len(str(num))
while num>0:
    remainder = num%10
    sum = sum + remainder ** n
    num= num//10

if sum == temp:
    print("It is armstrom number")
else:
    print(False)

#Qn4 = Range of fabbonacci
for num in range(1 , 1000):


    temp = num

    sum=0 #sum where number is add
    n= len(str(num))
    while num>0:
     remainder = num%10
     sum = sum + remainder ** n

     num= num//10

    if(sum == temp):
       print(sum,end=" ")








