height = float(input("What is your height in meters? "))
weight = int(input("What is your weight? "))

bmi = round(weight/height**2, 2)


if bmi <20:
    print(f"Your BMI is: {bmi}, You are under weight")
elif bmi >=20 and bmi<25:
    print(f"Your BMI is: {bmi}, You have normal weight")
else:
    print(f"Your BMI is: {bmi}, You are over weight")






