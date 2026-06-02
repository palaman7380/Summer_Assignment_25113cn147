#Qn=2 convert Binary to decimal
bn = int(input("Enter the number"))
dec ,i=0,0
while bn>0:
    r = bn%10
    exp = r*(2**i)
    dec = dec + exp
    bn = bn//10
    i+=1
print("Decimal number",dec)
    
