import random
symbolsglas = 'eyuioaEYUIOA'
symbolssoglas = 'qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '!@#$%^&'
lenght = 3

password = ''

for i in range(lenght):
    password += random.choice(symbolssoglas)
    password += random.choice(symbolsglas)
for i in range(lenght):
    password += random.choice(numbers)
for i in range(lenght):
    password += random.choice(symbols)
print(password)
    
