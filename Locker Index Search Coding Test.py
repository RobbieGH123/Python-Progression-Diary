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

def number_fifty_finder_two(numbers):
    numbers.sort()
    counter_two = 0
    left = 0
    right = len(numbers) - 1
    if not numbers:
        print("There is no list given")
        return counter_two + 1
    while left <= right:
        counter_two += 1 
        midpoint = (left + right) // 2
        if numbers[midpoint] == 50:
            print(f"50 was found in {counter_two} steps")  # Changed this line
            return counter_two
        elif numbers[midpoint] > 50: 
            right = midpoint - 1
        else: 
            left = midpoint + 1

    print(f"In {counter_two} steps it is conclusive that $50 is not within the list")  # Changed this line
    return counter_two
number_fifty_finder_two([10, 20, 30, 40, 60, 70, 80, 90])  # Will print "not found" message
number_fifty_finder_two([10, 20, 30, 40, 50, 60, 70, 80])  # Will print "found" message



  


