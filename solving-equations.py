import math

print("Welcome to the calculator! I am able to Solve Systems of Equations, To start please input two equations in the form of y = kx + b")

input1 = str(input("Enter the first equation: y="))
input2 = str(input("Enter the second equation: y="))
input3 = int(input("Enter the first equations constant: "))
input4 = int(input("Enter the second equations constant: "))
input5 = int(input("Enter the first equations slope: "))
input6 = int(input("Enter the second equations slope: "))

if input1 == input2:
    print("Infinitely many solutions")

def Stage1(input1, input2):
    return input1, input2

print(input2,"=", input1)

def Stage2(input1, input2, input3, input4, input5, input6):
    input