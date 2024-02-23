#string
a = "Hello"
print(a)
print(type(a))
#to check individual charactor in a srting
print(a[0])
print("==============")


#integer
a = 123
print(a)
print(type(a))
print(15+14)
print("==============")


#Floting

a = 3.284
print(a)
print(type(a))
print(a+14)
print("==============")

#bullon
a = 15
if a ==15:
    print(True)
    
else:
    print(False)
print("==============")

#conversion of data type from int to string    
num_char = len(input("What is your name: "))
new_num_char = str(num_char)

print("your name has " +new_num_char+ " Charactors")
print("==============")


#change data type from string to int
two_digits = input("Please enter two digits: ")

first_digit = int(two_digits[0])
second_digit = int(two_digits[1])

two_digits_number = first_digit + second_digit

print(two_digits_number)