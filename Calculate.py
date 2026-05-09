# Simple Arithmetic Calculator

# ask user for two numbers

# ask user for operator

# perform calculation

# display result

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


operator = input("Enter operator (+, -, *, /): ")


if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    result = "Invalid operator"


print("Result:", result)
