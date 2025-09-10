num1 = float(input("Enter First Number: "))
op = input("Enter Operator (+,-,*,/): ")
num2 = float(input("Enter Second Number: "))

operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2
}

if op in operations:
    print(f"{num1} {op} {num2} = {operations[op]}")
else:
    print("Invalid Operator")
