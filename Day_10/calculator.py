from audioop import add
import math
from symtable import Symbol
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y



calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))

for symbol in calculator_operations:
    print(symbol)
    
opertaion_symbol =  input('Please pich the operation from the above: ')


result = num1


