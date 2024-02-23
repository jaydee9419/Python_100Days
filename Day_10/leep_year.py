def is_leep(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def days_in_month(year, month):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leep(year):
        return 29
    else:
        return month_days[month -1]

year = int(input("Please enter year: "))
month = int(input("Please enter month: "))

days = days_in_month(year, month)

print(days)