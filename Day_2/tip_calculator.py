print("Welcome to the tip calculator")

bill = float(input("What was the total bill? "))

tip = int(input("What percentage tip would you loke to give? "))

people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill*tip/100)

bill_per_person = bill_with_tip/people
final_amount = round(bill_per_person,2)
print(f"Each person sholuld pay: {final_amount}")


