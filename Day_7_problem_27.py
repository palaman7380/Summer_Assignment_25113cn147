# Write a program to Recursive sum of digits. 

def sum(n):
    if n==0:
        return 0
    else:
        return(n%10)+sum(n//10)
    

n=int(input("enter no:"))
print(sum(n))