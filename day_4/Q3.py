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