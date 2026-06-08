def prime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num%i==0:
           
            return False
        else:
            return True

num = int(input("Enter the number"))
if prime(num):
    print("prime number")
else:
    print("Not prime number")
