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