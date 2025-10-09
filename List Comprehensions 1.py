#=================================================================This file is to introduce list comprehensions:========================================================#


# Create a list of square numbers 1 - 20:

square_list = [num * num for num in range(1, 21)]
print(square_list)


# Create a list, extracting the even numbers only: 

evens_list = [num for num in range (1, 21) if num % 2 == 0]
print(evens_list)


# Create a list, flattening a nested list:

flat_list = [item for sublist in [[1, 2], [3, 4], [5, 6]] for item in sublist]
print(flat_list)


# Lambda introduction, should be used in place of normal functions. 


# Lambda double function:

double = lambda x: x * 2
print(double(8))


# Lamba greater than 10 function:

greater_than_ten = lambda x: x > 10
print(greater_than_ten(11))


# Map introduction # On the left side - lambda. On the right side - list. 

# Map:

map_introduction = list(map(greater_than_ten, range(1, 16)))
print(map_introduction)


# Filter introduction # On the left side - lambda. On the right side - list. 

filter_introduction = list(filter(greater_than_ten, range(1, 16)))
print(filter_introduction)


# Now I am going to re-write this list comprehension using a lambda/filter function:

evens_list = [num for num in range(1, 21) if num % 2 == 0]


evens = lambda x: x % 2 == 0 # Lambda function that checks whether x is even. 
evens_list_two = list(filter(evens, range(1, 21))) # Lambda and filter to cancel out odds. 
print(evens_list_two)


# Now I am going to re-write this list comprehension using a lambda/map function:

square_list = [num * num for num in range(1, 21)]


squared = lambda x: x * x # Lambda function that squares x.
square_list_two = list(map(squared, range(1, 21)))
print(square_list_two)


# Filter out words that are 5 or less letters using lambda and filter function:

words = ["cat", "elephant", "dog", "butterfly", "ant", "python"]

five_filter = lambda x: len(x) > 5
five_letter = list(filter(five_filter, words))
print(five_letter)


# Everything multiplied by 3:

numbers = [1, 4, 7, 12, 15, 18, 23, 30]
multiply_three = lambda x: x * 3
three_times_numbers = list(map(multiply_three, numbers))
print(three_times_numbers)


# Filter -> Lambda:

prices = [12.50, 8.75, 15.20, 6.30, 22.10, 9.80]
price_check = lambda x: x > 10
prices_above_ten = list(filter(price_check, prices))


twenty_percent = lambda x: x * 1.2
twenty_percent_tip = list(map(twenty_percent, prices_above_ten))
print(twenty_percent_tip)


