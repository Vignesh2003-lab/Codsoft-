def calculator(num1, num2, operator):
    if operator == '+':
        print("Sum:", num1 + num2)
    elif operator == '-':
        print("Difference:", num1 - num2)
    elif operator == '*':
        print("Product:", num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print("Quotient:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator")

# User inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Call the function
calculator(num1, num2, operator)
