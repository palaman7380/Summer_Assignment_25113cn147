# Write a program to Recursive reverse number. 

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

# Input
num = int(input("Enter a number: "))

# Output
print("Reversed number is:", reverse_number(num))
