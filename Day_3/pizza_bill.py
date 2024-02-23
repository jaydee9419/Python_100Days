



print("Welcome to the Pizza Hut!")
bill = 0

size = input("Please choose the size? (S/M/L): ").lower()
if size == "s":
    bill = bill + 10
    
elif size == "m":
    bill = bill + 15

elif size == "l":
    bill = bill + 20
else:
    print("wrong selecton")


pepper = input("additional pepper is required? (Y/N): ").lower()

if pepper == "y":
    if size == 's':
        bill += 3
    else:
        bill += 5
else:
    final_bill = bill
    
extra_cheese = input("Extra cheese requird? (Y/N): ").lower()

if extra_cheese == "y":
    bill += 5
    final_bill = bill
else:
    final_bill = bill
print(f"Here is your final bill: ₹{final_bill}.")






