#quiz application 
import random
import string
length = int(input("enter the password length"))
charecters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(length):
    password += random.choice(charecters)

print("congratulation : password is generated: " , password)