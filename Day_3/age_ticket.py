print('Welcome to rollercoaster!')
height = int(input("What is your height in cm? "))

ticket = 0
if height >=120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    
    if age <12:
        amount = ticket + 5
        print(f"Please pay: {amount}")
        
    elif age >=12 and age<18:
        amount = ticket + 7
        print(f"Please pay: {amount}")
        
    else:
        amount = ticket + 9
        print(f"Please pay: {amount}")
        
else:
    print("Sorry, you have to grow taller before ride.")



