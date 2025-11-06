## Test Document ## 

## Trying to sort a list with nested lists##
 
nested_list = [[3, 4], [1, 2], [5, 0]]
print(nested_list[0])
nested_list.remove[0]
print(nested_list)
sorted_list = sorted(nested_list, key=lambda x: x[0])  # Sort by first element
print(sorted_list)

sorted_list = sorted(nested_list, key=lambda x: x[1])  # Sort by second element
print(sorted_list)

