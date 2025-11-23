import random

print('=== Welcome to the Application ===')

symbols =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_pass = int(input('Введи длинну пароля: '))
password = ''

for i in range(len_pass):
    password += random.choice(symbols)

print('\nвот твой пароль:', password)
