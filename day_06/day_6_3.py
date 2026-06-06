#Qn=3 calculate power without power sunction
a = int(input("Enter a"))
b = int(input("Enter b"))
result = 1
while b !=0:
    result *= a
    b-= 1

print(f"{a}to the power {b} = {result}")
    
