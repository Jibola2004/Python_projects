import random
try:
    number= int(input('Enter the length of the password: '))

except:
    raise ValueError('Invalid input enter integer value.')



choices='abcdefghijklmnopqrstuvwxyz!1234567890.,?;:><#+-*$^ABCDEFGHIJKLMNOPQRSTUVWXYZ@'
choices = list(choices)
result=''
for i in range(number):
    result += random.choice(choices)

print(f"Your password is {result}")    

