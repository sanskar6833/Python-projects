import random
import string
char= string.ascii_letters + string.digits + string.punctuation
n= int(input("enter desired length of password"))
password=""
for i in range (n-1):
    password+=random.choice(char)
print(f"your password = {password}")    
