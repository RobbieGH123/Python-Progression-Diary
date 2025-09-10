# Reviewing Dictionaries and Sets:

########## Dictionaries ##########

counts = {"a": 1, "b": 2}         # Establishes a Dictionary
counts.get("c", 0)                # returns 0 if "c" isn’t in dict
counts["c"] = 0                   # Inserts the Key 'C' into 'counts' with the value 3.
for key, value in counts.items(): # Grab each Key Value pair in 'counts'
    print(key, value)             # Print them in the format 'Key, Value'
if "a" in counts:                 # Checks if the string a is in counts.
    pass

############## Sets ##############

nums = {1, 2, 5}                  # Establishes a Set (Notice - Sets don't have value pairs)
nums.add(3)                       # Adds 3 to the Set
nums.remove(2)                    # Removes 2 from the Set
if 3 in nums:                     # Checks if 3 is in the list, nums.
  pass 

odds = {1, 3, 5}
evens = {2, 4, 6}
print(odds | evens)               # Union - only once per character
print(odds & evens)               # Intersection - No Numbers are found in both so it will print "set()"
print(odds - {1})                 # Removes 1 from the set 'odds'

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

############# TwoSum #############

def TwoSum(nums, target):                     # Creates the function, two 2 parameters
   nums_indexes = {}                          # Empty Dictionary
   for i, num in enumerate(nums):             # For each number, is nums, enumerate | Assigns the index to i and the value to num
      complement = target - num               # Works out the difference between the current number and the target
      if complement in nums_indexes:          # If the required number is already in the index
       return [nums_indexes[complement], i]   # Returns the index of the complement and the index of the current number
      else:                                   # If the complement is not in the list
         nums_indexes[num] = i                # Add the current number found at with its Value Pair, i for the index.
print(f"\n {TwoSum([2,7,11,15], 9)}")         # Returns the index of 2 and 7

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
 
########## Group Anagrams ##########

def anagrams(word_list):                                        # Anagaram with the incoming list as the parameter
   groups = {}                                                  # Empty Dictionary, allowing instant lookup (O1)
   for word in word_list:                                       # For each word in the given list
      sorted_word = tuple(sorted(word))                         # Sort it and change it into a tuple instead of a list
      if sorted_word in groups:                                 # If the sorted word is in the Dictionary
         groups[sorted_word].append(word)                       # Add Dictionary Key: Sorted Word Value: Word
      else:                                                     # If it is not in the Dictionary
        groups[sorted_word] = [word]                            # Create a new Key and add that word as the Value.
   return list(groups.values())                                 # Return the Dictionary Values in list format.
print(anagrams(["eat","tea","tan","ate","nat","bat"]))          # Test run with this list.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
      
########### Happy Number ###########

# Happy Numbers Problem:
# A happy number is a number that eventually reaches 1
# when replaced by the sum of the squares of its digits.    E.g 19 -> 82 -> 68, -> 100 -> 1 
# If it loops endlessly in a cycle that does not include 1, 
# it is not a happy number.
# This program checks whether a given number is happy.

def Happy_Numbers(n):                               # Creation of the function
   seen = set()                                     # Seen - used in this instance so that we don't get stuck in a loop
   while n != 1 and n not in seen:                  # While the result does not equal 1 and is not a continuous loop
      squared_sum = 0                               # Sum of the digits squared
      for digit in str(n):                          # Loop over each digit in n, squaring the digit
         digit_sq = int(digit) * int(digit)         # Add together the Squared Results
         squared_sum += digit_sq                    # Record it in the empty variable
      n = squared_sum                               # Now that the for loop is over, I assign the value back to n, for the while condition
      seen.add(n)                                   # Add the Squared Total to Seen
   return n == 1                                    # Return True - if n equals 1
print(Happy_Numbers(2))                             # Test with the input | 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 136 -> 46 -> 52 -> 29 -> 85 -> 89... 89 duplicate, false.
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

### Longest Consecutive Sequence ###

# Given a list
# In O(n) time --- Therefore no sorting
# Return the length of the longest consecutive sequence

def longest_sequence(unsorted_array):
   max_length = 0
   set_array = set(unsorted_array)
   for number in set_array:
      if number -1 not in set_array:
         counter = 1
         while number + 1 in set_array:
          counter += 1
          number += 1
         max_length = max(max_length, counter)
   return max_length
print(longest_sequence([100, 4, 200, 1, 3, 2]))



     

