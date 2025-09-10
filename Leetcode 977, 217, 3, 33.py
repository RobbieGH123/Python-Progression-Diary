# 4 Leetcode Problems

# 977 - Squares of a Sorted Array:
# Given an ascending list, including negatives, return the square list in ascending order.

def ascending_square_list(nums): # Function with the list as the parameter

    right = len(nums) - 1                                               # Right counter
    left = 0                                                            # Left Coounter
    new_nums = [None] * len(nums)                                       # New list, assigned the length of the existing lift, using PHs. 
    for i in range(len(nums)):                                          # Iterate through the list, i starts at 0 -> 1 etc.
        if nums[left] * nums[left] < nums[right] * nums[right]:         # If left no.^2 is smaller than right no.^2
            new_nums[len(nums) - 1 - i] = nums[right] * nums[right]     # Set the rightermost index to right no. squared. 
            right -= 1                                                  # Set right counter to NEW far side of the list.
        elif nums[left] * nums[left] > nums[right] * nums[right]:       # If right no.^2 is smaller than left no.^2
            new_nums[len(nums) - 1- i] = nums[left] * nums[left]        # Set the rightermost index to left no. squared.
            left += 1                                                   # Set left counter to NEW near side of the list.
        else:                                                           # Else (If equal)
            new_nums[len(nums) - 1 - i] = nums[left] * nums[left]       # Just use the left side
            left += 1                                                   # Set left counter to NEW near side of the list.
    return new_nums                                                     # End function once for loop is over
print(ascending_square_list([-4,-1,0,3,10]))          ## Example ##
        
# 217: Contains Duplicates - Scan through lists, seeing if they contain any duplicates.

def duplicate_search(lst):                                 # Function, list parameter

    seen = set()                                           # Records letters seen
    for item in lst:                                       # Iterate through every item in the list
        if item in seen:                                   # If the item has already been sen
            print("There are duplicates in this list")     
            return True                                    # Exit the function, returning True
        else:                                              # If not
            seen.add(item)                                 # Add it to the seen set 
    print("There are no duplicates in this list")
    return False                                           # Return False
print(duplicate_search([1,2,3]))              ## Example ##

# 3: Longest Substring Without Repeating Characters                        # REVISIT -------

def longest_substring(subs):

  left = 0 
  right = 0
  current_length = 0
  max_length = 0
  seenb = set()

  for i in subs:
      while subs[right] in seenb:
          seenb.remove(subs[left])
          left += 1
          current_length -= 1
          max_length -= 1
      else:
          seenb.add(subs[right])
          right += 1
          max_length += 1
          current_length = right - left
  return seenb, max(max_length, current_length)
print(f"\n The longest substring was with a length of {longest_substring("pwwkew")}")

# 33. Search in Rotated Sorted Array
# Given a list that has been sorted, then chopped, find a number within. i.e 1 2 4 3 5 8 6 7 10 9 -> 1 2 3 4 5 6 7 8 9 10 -> 8 9 10 1 2 3 4 5 6 7. Find 7

def rotated_array_search(rotar, target):    # 2 Parameter function
    left = 0                                # Left Counter
    right = len(rotar) - 1                  # Right Counter

    while left <= right:                    # Whie left is smaller than or equal to right
        mid = (left + right) // 2           # The midpoint is inbetween them

        if rotar[mid] == target:            # If the midpoint IS the target
            return mid                      # Return the value of mid

        # If Left half is sorted
        if rotar[left] <= rotar[mid]:
            if target >= rotar[left] and target < rotar[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if target <= rotar[right] and target > rotar[mid]:
                left = mid + 1
    return -1

arr = [4,5,6,7,0,1,2]
target = 2
pos = rotated_array_search(arr, target)
print(f"The target {target} is at index {pos}")