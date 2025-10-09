## 4th Week Function Review

def primenum(x):

    n = 2
    if x < 2:
       return False
    while n * n <= x:

     if x % n == 0:
       return False
     
     n += 1
    return True
print(primenum(37))

#=====================================================================================================================================================================#
     
def listmax(lst):
   """
   >>> listmax([1, 33, 20, 17, 302, 73, 59, 8])
   302
   """
   max_list = lst[0] 

   for item in lst:
      if item > max_list:
         max_list = item
   return max_list
print(f"The highest integer in this list is: {listmax([1, 2, 4, 2, 3, 7, 5, 8])}")

#=====================================================================================================================================================================#

def factorial(num):
   
    """
    Return the factorial of a non-negative integer.

    >>> factorial(4)
    24
    >>> factorial(0)
    1
    """

   
    if num < 0:
      raise ValueError("Factorials cannot be negative")
    if num == 0:
      return 1
    if num == 1:
      return 1
    else:
      return num * factorial(num-1)
   
help(factorial)
print(factorial(6))


#=====================================================================================================================================================================#
      
def fizzbuzz(n):
    """
    By calling fizzbuzz with an integer, this function will iterate through every number from 1 to the inputted number, returning "Fizz" if the number is divisible by 3
    Buzz if the number is divisble by 5, Fizzbuzz if divsible by 3 and 5, else, it will just return the number, also has error handling
    """

    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Cannot input a negative number")
    else:
   
       for _ in range (1,n+1):
      
        if _ % 5 == 0 and _ % 3 ==0:
         print("FizzBuzz")
        elif _ % 3 == 0:
         print("Fizz")
        elif _ % 5 == 0:
         print("Buzz")
        else:
         print(_)
    
    return
fizzbuzz(16)

#=======================================================================================================================================================================#

def word_count(txt):
 
    """
    The word_count function takes the words in a string or list, adding them to a dictionary,
    counting the amount of times each word appears in the input
    """

    word_counts = {}

    if isinstance(txt, str): 
        txt = txt.lower().split()
    
    elif isinstance(txt, list):
        txt = [word.lower() for word in txt]

    for word in txt:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print(f"{word_count(('Hello my name is Samuel, last week I adpoted a dog called Micheal, he is a labrador'))}")
print(f"{word_count(["Hello", "my", "name", "is", "Samuel", "last", "week", "I", "adpoted", "a", "dog", "called", "Micheal", "he", "is", "a", "labrador"])}")

#=======================================================================================================================================================================#

def sum_nested(lst):
   
    """
    This function aims to add all of the numbers within a list, accounting for nested lists via a recursive function call. Returning the amount as manipulatable data
    >>> sum_nested([1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]])
    55
    """
    total = 0
    for i in lst:
      if isinstance(i, list):
         total += sum_nested(i)
      else:
         total += i
    return total
print(sum_nested([[1,2],[2,3]]))
