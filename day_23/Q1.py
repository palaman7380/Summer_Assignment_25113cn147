#  Find first non-repeating charecter
str_1 = input("Enter the stringh")
for ch in str_1:
    if str_1.count(ch) == 1:
        print("First non-repeating character is:", ch)
        break 
    else:
        print("non repeating  harecter the charecter")