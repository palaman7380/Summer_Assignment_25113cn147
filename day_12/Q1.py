def palindrome(num):
    temp = num
    count = 0
    while temp >0:
        digit = temp % 10
        count = (count*10)+ digit 
        temp =temp//10

    if num == count:
        
        print("Palindrome number")
    else:
        print(False)


num = int(input("Enter the number"))
print(palindrome(num))
