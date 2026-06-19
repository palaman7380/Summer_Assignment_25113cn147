#Character frequency
str_1 = input("enter the string")
for ch in set(str_1):
    print(f"{ch} : {str_1.count(ch)} times")