import math

input1 = input(" Add, Subtract, Multiply, or Divide, what math operation would you like to do? ")

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

if input1 == "Add":
    print("The sum of the two numbers is: ", addition(x, y))

if input1 == "Subtract":
    print("The difference of the two numbers is: ", subtraction(x, y))
    
if input1 == "Multiply":
    print("The product of the two numbers is: ", multiplication(x, y))
    
if input1 == "Divide":
    print("The quotient of the two numbers is: ", division(x, y))