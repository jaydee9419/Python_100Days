number = [1,2,5,6,8,9,45,67,3,56,65,7]
even_number = []
odd_number = []
for item in number:
    if item %2 ==0:
        even_number.append(item)
    else:
        odd_number.append(item)
print(even_number)
print(odd_number)