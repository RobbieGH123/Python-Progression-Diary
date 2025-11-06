# Small project
# I have just watched the Harvard lecture demonstrating searching through doors for the number 50 and am going to attempt to code it, returning the steps and index location.

def number_fifty_finder(numbers): # Creates the function

 numbers.sort() # Sorts the list into numeric order
 print(numbers) # Testing that the sort worked
 print(len(numbers))
 counter = 0    # Steps counter
 for value in numbers: # Checks the value of each number in the, now sorted, numbers list.
    if value == 50:    # If the value is 50
      return counter   # Return the counter ending the function call
    counter += 1       # Else, add one to the counter (Look at the indentation)
print(f"\n The 50 dollar bill was found in  {number_fifty_finder([15, 5, 10, 30, 35, 50, 80, 65, 100])} steps") # Final test to see if it works, with a list input.

# Now I am going to attempt to code a function that will find in the smallest number of steps possible, by looking in the middle and searching based off of the feedback of that choice.

def number_fifty_finder_two(numbers):     # Creating the function
    numbers.sort()                        # Sorts the list into numeric order
    counter_two = 0                       # Setting up a step counter
    left = 0                              # Using one tracker beginning at index 0
    right = len(numbers) - 1              # Another at the end of the list
    if not numbers:                       # If the list is empty
        print("There is no list given")   # Tell the user that there is no list
        return counter_two + 1            # Return the step counter, thus ending the function
    while left <= right:                  # If there is a list, establishes a while loop, until left is greater than right
        counter_two += 1                  # Adds a step to the counter
        midpoint = (left + right) // 2    # Calculates the midpoint and rounds it
        if numbers[midpoint] == 50:       # If the value found at the position of the midpoint equals 50
            print(f"$50 was found in {counter_two} steps")  # Inform the user that it was found in this many steps
            return counter_two            # Return counter_two, thus ending the function.
        elif numbers[midpoint] > 50:      # Else, if the value at the midpoint is greater than 50
            right = midpoint - 1          # Search the left side because we know it is sorted
        else:                             # Else, (if it is less than 50)
            left = midpoint + 1           # Search the right side, because again, we know it is sorted

    print(f"In {counter_two} steps it is conclusive that $50 is not within the list")  # This line should only run if 50 is not found as it if after the while loop
    return counter_two                                                                 # If 50 is not found, exit the function.
number_fifty_finder_two([10, 20, 30, 40, 60, 70, 80, 90])  # Test demonstrating - Prints "not found" message
number_fifty_finder_two([10, 20, 30, 40, 50, 60, 70, 80])  # Test demonstrating - Prints "found" message



  


