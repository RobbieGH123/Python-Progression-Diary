# Calculator 2 (Functions Review)

def add(a, b):
 sum = a + b
 return sum

def subtract(a, b):
      subtracted = a - b
      return subtracted

def multiply(a, b):
      multiplied = a * b
      return multiplied

def divide(a, b):
      try:
       divided = a / b
      except ZeroDivisionError:
       divided = ("You cannot divide by Zero")
      return divided


def calculator():
    answer = input("Addition, Subtraction, Multiplication or Division: ")
    answer = answer.lower()
    try:
     a = int(input("Input your first number: "))
    except ValueError:
       print("Not a valid number")
       return
    try:
     b = int(input("Input your second Number: "))
    except ValueError:
       print("Not a valid number")
       return

    if answer == "addition" or answer =="add" or answer == "plus":
       print(add(a, b))
      
     
    elif answer == "subtraction" or answer == "subtract" or answer == "minus":
     print (subtract(a,b))
            
    elif answer == "multiplication" or answer == "multiply" or answer == "times":
     print(multiply(a, b))

    elif answer == "division" or answer == "divide":
     print(divide(a,b))
calculator()



