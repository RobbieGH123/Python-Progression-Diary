# String Processor Challenge:
# Function that returns the amount of vowels in a string:

def vowelcount(inpstr):                                                                                                            # Function
 vowel_tally = 0                                                                                                                   # Counter

 for char in inpstr:                                                                                                               # Iterator
         if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":       # If vowel
             vowel_tally += 1                                                                                                      # Counter + 1
 return vowel_tally                                                                                                                # After Iterator, return
print(f"{vowelcount("atmosphere")}")                                                                                               # Test-run

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## String Reverser Function ##

def stringreverser(tgtstr):                               # Function
    j = len(tgtstr) - 1                                   # Assigns J the value of the last integer
    reversed = ""                                         # Empty String to record the reversed string
    if tgtstr == "":                                      # If the input is empty
            return "You have submitted no input"          # return message
    else:                                                 # If not empty
     for item in tgtstr:                                  # Iterator
         reversed += tgtstr[j]                            # Creates the reversed string
         j -= 1                                           # Move J one to the left
    return reversed                                       # Return the reversed string
print (f"\n {stringreverser("")}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
## Palindrome Checker #

def palindromechecker(pldstr):                                                                  # Function, utilising the previous reverse string function
    reversed_string = stringreverser(pldstr)                                                    # Assigns the reversed string to the variable "reversed_string"
    if pldstr.lower() == reversed_string.lower():                                               # If the function input is the same reversed and ordinary
        print("\nThat is a Palindrome!")                  
    else:
        print("\nThat is not a Palindrome")
    return f"The original string was: {pldstr}. The string, reversed, is: {reversed_string}" 
palindromechecker("Racecar")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Global and Local Variables ##                                                          # Function to show how the keyword "global" is utilised

x = 10                                                                                    # Creates two global variables, x and y. 
y = 10

def scopedemo():                                                                          # Now, going inside of a function, global variables don't work... unless
    global x                                                                              # Imports the Global Variable "x" as x
    x = x + 5                                                                             # Shows that I can now manipulate inside of the function
    print(f"\nWith global keyword, x is now {x}")                                         # Utilising the Global Keyword, I have now managed to assign x as 15
    try:                                                        
     y = y + 5
    except UnboundLocalError:                                                             # Stops the error from crashing the program.
        print("Without global keyword, Python encounters an error - cannot modify y")     # Without utlising global keyword, I cannot manipulate y
scopedemo()                                                                               # Runs the function
print(f"After the function - Global x: {x}")                                              # Print the value of x after the function
print(f"After the function - Global y: {y}")                                              # Print the value of y after the function

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

## Exploring Memory Behaviour with Lists ## 

# Mutable objects (list, dict, set):               # Changes inside of the function DO affect the original

my_list =[1, 2, 3]                                 # Create a list

def modify_list(lst):                              # Function to modify lists
    lst.append(4)                                  # Add '4' to the list
    print(f"\nInside function {lst}")                # Print the new lists value, inside of the function -> [1, 2, 3, 4]

modify_list(my_list)                               # Call the function with my_list as its paramater
print(f"Outside function {my_list}")               # Print the new lists value, outside of the function -> [1, 2, 3, 4]

# Versus Immutable objects (int, string, tuple):   # Changes inside of the function DO NOT affect the original

my_number = 10                                     # Creates an integer variable

def modify_number(num):                            # Function to modify numbers
    num = num + 5                                  # Add 5 to the number
    print(f"\nInside function {num}")              # Print the new numbers value, inside of the function -> 15

modify_number(my_number)                           # Call the function my_number as its paramater
print(f" Outside function {my_number}")            # Print the new number value, outside of the function -> 10... Notice how Python treats numbers and lists differently

def memory_demo(a_number, a_list):

    print(f"\nAt the beginning of the function, Number: {a_number}, List: {a_list}")

    a_number = a_number + 5
    a_list.append(10)

    print(f"Inside of the function, Number: {a_number}, List: {a_list}")
    
original_number = 50
original_list= [1, 2, 3, 4, 5, 6]
memory_demo(original_number, original_list)
print(f"After the function Number: {original_number}, List: {my_list}")


    



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#