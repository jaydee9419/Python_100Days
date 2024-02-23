from re import L


male_name = input("Please enter male name: ")
female_name = input("Please enter female name: ")

combined_names = (male_name + female_name).lower()

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
first_digit = t + r + u + e

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score <10 or score >90:
    print(f"Your score is: {score}, just friends")
elif score >=40 and score <=50:
    print(f"your are score is: {score}, lovers")
else:
    print(f"Your score is: {score}.")