height = float(input('Please enter your height: '))
weight =  int(input("Please enter your Weight: "))

BMI = weight/height**2
print(BMI)
if BMI <10:
    print("Low weight")
    
elif BMI >10:
    print("Need to buildup")
    
elif BMI >20:
    print("Optimum Weight")
    
elif BMI>30:
    print("Need to reduce the weight")
else:
    print("out of range")


