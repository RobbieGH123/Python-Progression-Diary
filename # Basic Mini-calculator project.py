def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "You cannot divide by 0" if b == 0 else a / b

operation = input("Choose operation: Addition, Subtraction, Multiplication, Division: ").strip().lower()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "addition":
    result = add(num1, num2)
elif operation == "subtraction":
    result = subtract(num1, num2)
elif operation == "multiplication":
    result = multiply(num1, num2)
elif operation == "division":
    result = divide(num1, num2)
else:
    result = "Invalid operation selected"


if isinstance(result, str):
 print(result)
else:
 print(f"\nThe result is: {result}")

