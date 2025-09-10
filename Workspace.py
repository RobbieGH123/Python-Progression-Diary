# Workspace for testing code:

print("--- Testing raise ---")

def withdraw(amount):
    if amount < 0:
        # This line creates and throws an error on purpose
        raise ValueError("You can’t withdraw a negative amount!")
    return f"You withdrew £{amount}"

try:
    # This will trigger the raise because -50 is invalid
    print(withdraw(-50))
except ValueError as e:
    print("Caught an error:", e)

print("Program still running after handling the error.")

#-------------------------------------------------------------------------#

try:
    Age = input("How old are you? ")
    Age = int(Age)
except ValueError:
    print("That is not a valid Number")
else:
    print(f"You are {Age} years old")
finally: 
    print("Program is complete")

#----------------------------------------------------------#

print("--- Exercise 3: File handling ---")

try:
    file = input("Which file would you like to open: ")
    f = open(file, "r") 
except FileNotFoundError:
    print("Your file can not be found, please make sure your file name is correct")
except PermissionError:
    print("You have not been granted access to this file")
except Exception:
    print("Something unexpected occured")
else: 
    content = f.read()
    print(content)
    f.close()
finally:
    print("Goodbye")





     

