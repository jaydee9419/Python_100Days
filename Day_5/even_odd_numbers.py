even_number = []
odd_number = []


for number in range(1,31):
    if number %2 ==0:
        even_number.append(number)
        
    else:
        odd_number.append(number)
        
print(even_number)
print(len(even_number))
print(odd_number)
print(len(odd_number))