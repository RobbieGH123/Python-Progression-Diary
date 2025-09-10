def print_flat(lst): # Defines a function called print_flat
    for item in lst: # Goes through each item in 1st
        if isinstance(item, list): # If the item is a list
            print_flat(item)  # Repeat the function with item as the paramater input
        else: # Otherwise
            print(item) # Print the item.
    # This allows Python to handle nested lists.

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(flatten(item))  # Recursive case
        else:
            result.append(item)          # Base case
    return result
print(flatten([1, [2, [3, 4]], 5]))
# Output: [1, 2, 3, 4, 5]
