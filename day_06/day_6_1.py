#Qn1 = convert decimal tobinary
num = int(input("Enter the number"))
count = ""
while num>0:
    remainder = num%2
    count = str(remainder) + count
    num = num//2

print(f"The binary of thr number{num} = {count}")
