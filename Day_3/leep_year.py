year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leep Year")
        else:
            print("Not Leep year")
    else:
        print("Leep Year")
else:
    print("Not Leep Year")
    