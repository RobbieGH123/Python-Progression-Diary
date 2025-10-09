## 5 Easy Leetcode Problems ~ some are being revisited

# 1. Two Sum:

def twosum(lst, target):                                     # Function


    for i in range(len(lst)-1):                              # Iterate through 0th index to second to last index
        for j in range(i+1, len(lst)):                       # Iterate through 1st index to last
            if lst[i] + lst[j] == target:                    # if: ith +i+jth index = target
               return i, j                                   # retuirn those index value
            
print(f"{twosum([2,7,11,15], 9)}")                           # ⇨ (0, 1)
print(f"{twosum([3, 2, 4], 6)}")                             # ⇨ (1, 2)
print(f"{twosum([3, 3,], 6)}")                               # ⇨ (0, 1)

# 121: Best Time to Buy and Sell Stock:

def maxProfit(prices):                                       # Function 0(n)²

    max_profit = 0                                           # Store Max Profit

    for i in range(len(prices)):                             # 1st iterator
        for j in range(i+1, len(prices)):                    # Second, nested, iterator i+1th index to last index
            if prices[j] > prices[i]:                        # If the new price is higher
                max_profit = max(max_profit, prices[j] - prices[i]) # Compare it to the stored maximum profit, if it is higher, upate max_profit
    return max_profit                                        # Once all of those iterations are done, return max_profit
print(f"The maximum amount of profit that you can achieve is {maxProfit([7,1,5,3,6,4])}") # ⇨ 5

def maxProfitOn(pricelst):                                   # Function O(n)

    """
    This is a second attempt on Leetcode 121, trying to solve it in O(n) time complexity, not O(n)²
    """

    max_profit = 0                                           # To store the max profit
    
    minimum = pricelst[0]                                    # Set the lowest price to the 0th index to begin
    for i in range(len(pricelst)):                           # For 0 -> last index

        if pricelst[i] < minimum:                            # If the ith price is the new lowest
            minimum = pricelst[i]                            # Update minimum with the value
        else:
            max_profit = max(max_profit, pricelst[i] - minimum) # Else test whether buying at the current minimum and selling on this ith day is the max profit
    return max_profit                                        # Return max_profit

print(f"The max amount of profit that you can achieve is: {maxProfitOn([2,1,4])}") # ⇨ 3

# 283: Move Zeroes

def moveZeroes(nums):                        # Function

    counter = 0                              # Manipulatable counter

    for i in range(len(nums)- 1):            # Iterator start to end-1
        if nums[counter] == 0:               # If the num at the counters index equals zero
            nums.pop(counter)                # Remove it
            nums.append(0)                   # Add 0 to the end of the list
        else: counter += 1                   # Else, add 1 to the counter and check again
    return nums                              # Return the new list
                    
print(f"The new, rearranged list is: {moveZeroes([0,0,1])}") # ⇨ [1, 0, 0]

# 26: Remove Duplicates from Sorted Array:

def removeDuplicates(nums):

    if not nums:                                              # If there is no list
        return 0                                              # Return 0
    
    k = 1                                                     # K = 1 because the first index is always unique by proxy

    for i in range (1, len(nums)):                            # Iterate through, start at 1
        if nums [i] != nums[k-1]:                             # If the ith index is unique
            nums[k] = nums[i]                                 # Set the number at 1 to the number found at i
            k += 1                                            # Increment k
    return k, nums                                            # Return the unique number counter and the new list

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# 169: Majority Element

def majorityElement(numbs):

    if not numbs:
        raise ValueError("You must provide a valid list input!")

    elements = {}
    length = len(numbs)

    for i in numbs:

        if i not in elements:
            elements[i] = 1
        else:
            elements[i] += 1

    max_key = max(elements, key=elements.get)
    if elements[max_key] > length // 2:
        return(f"The Majority Element in this example was: {max_key} and it appeared {elements[max_key]} times")
    else:
        return(f"There is no Majority Element, the number that occured the most was {max_key} and it only occured {elements[max_key]} times")
    
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([0,1,1,2,3,4,5,6,7,8,9,10]))
#print(f"The Majority Element was: {majorityElement([])}")



   
    