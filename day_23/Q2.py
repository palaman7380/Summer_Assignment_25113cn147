#  Find first repeating charecter
#  Find first non-repeating charecter
str_1 = input("Enter the stringh")
for ch in str_1:
    if str_1.count(ch) > 2:
        print("First repeating character is:", ch)
        break 
    else:
        print("No repeating character found")