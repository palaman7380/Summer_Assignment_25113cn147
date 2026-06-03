# Write a program to Recursive reverse number. 

def rev(n):
    if n==0:
        return 0
    else:
        return str(n%10)+str(rev(n//10))
    
n=int(input("enter no:"))
print(rev(n))