print('Welcome to rollercoaster!')
height = int(input("What is your height in cm? "))

ticket = 0
if height >=120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    
    if age <12:
        bill = ticket + 5
        print(f"Child ticket: ₹{bill}")
        
    elif age >=12 and age<18:
        bill = ticket + 7
        print(f"Youth ticket: ₹{bill}")
    
    elif age >=45 and age <=50:
        bill = ticket
        print("Please have a free ride.")
        
        
    else:
        bill = ticket + 9
        print(f"Audult ticket: ₹{bill}")
        
    photo = input("Do you wanna photo Y/N: ").lower()
    if photo == "y": 
        bill += 3
         
    print(f"Your final bill is: ₹{bill}")
else:
    print("Sorry, you have to grow taller before ride.")
