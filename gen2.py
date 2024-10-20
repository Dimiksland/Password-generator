#Генератор паролей

import random

symbols = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%&'
lenght = 24
password = ''

for i in range(lenght):
    password += random.choice(symbols)
print(password)
