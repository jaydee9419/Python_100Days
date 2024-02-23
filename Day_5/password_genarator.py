import random

letters = ['A', 'B','C', 'D']
numbers = ["1","2","3","4"]
symbols = ['@', '#', '$', '&']

print("Welcome to the _listpassword_list generator")

nr_letters = int(input('How many letters required:\n'))
nr_numbers = int(input('How many digits required:\n'))
nr_symbols = int(input('How many symboles do you wanna use:\n'))


# Easy Method
password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for symb in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
    

random.shuffle(password_list)


password = ""

for char in password_list:
    password += char
    
print(password)
