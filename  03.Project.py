# Simple Calculator

# Get user input
num1 = float(input("Enter First Number: "))
operator = input("Enter Operator (+,-,*,/): ")
num2 = float(input("Enter Second Number: "))

# Calculate and display result
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid Operator")
