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