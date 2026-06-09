def perfect(num):
    sum = 0
    
    for i in range(1,num):
        
        if num %i==0:
            
            sum = sum +i 

        elif sum == num:
            print("Perfect number")
        else:
            print(False)

num=int(input("Enter the number"))
print(perfect(num))