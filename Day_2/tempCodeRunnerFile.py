print("Welcome to the tip calculator")

bill = float(input("What was the total bill? "))

tip = int(input("What percentage tip would you loke to give? "))

people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill*tip/100)
print(bill_with_tip)