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