# 3 Medium Leetcode Problems:

# PROBLEM 1: Longest Substring without Repeating Characters:

def longest_substring(s): # Creating a function
    left = 0              # Left Tracker
    max_length = 0        # Longest Substring Tracker
    seen =set()           # Records letters we have seen

    for right in range(len(s)):  # Scans through every letter in the input
        while s[right] in seen:  # If the newest letter has already been seen
            seen.remove(s[left]) # Remove the leftermost letter
            left += 1            # Move left index 1 to the right

        seen.add(s[right])      # If the newest letter has not been seen, add it to 'seen'

        current_length = right - left + 1             # The current substring will be the right index - left index + 1
        max_length = max(max_length, current_length)  # Compares which one is higher, the previous maximum substring or the current substring
    return max_length                                 # Returns the answer length of the previous line
print(longest_substring('abcdefghghjkl'))             # Example input to the function paramater to test whether the code is functioning as designed and intended.

# ++++++++++++++++++++++++++++++

# Learnt how to use Seen
# Learnt how to use Max

# 122: Best Time to Buy and Sell Stock II

prices = [7,1,5,3,6,4]
profit = 0
for i in (range(len(prices))):
    if prices[i] > prices[i-1]:
        profit += i - (i-1)
print(profit)
    

        


    
    


            
 

      



        