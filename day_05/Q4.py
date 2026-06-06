#largest facter 
num = int(input("enter the number"))
temp = num
count=0
for i in range(1,temp):
    if temp%i==0:
        count=count+1
        
        
print(count)