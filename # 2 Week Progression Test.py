# 2 Week Progression Test

# Print the numbers 1-20:
print(list(range(1, 21)))

# Print only the even numbers

empty_list = []

for i in range(1, 21):
    if i % 2 == 0:
     empty_list.append(i)

print(empty_list)

# Count how many numbers between 1 and 100 are divisble by 7

c = 0

for i in range(1, 101):
   if i % 7 == 0:
      c += 1
   
print(f" The amount of numbers divisble by 7 between 1 and 100 is: \n {c}")

# Guess the number game: while loop, closes if correct:

import random

number = int(random.randint(1, 10))

while True:
 guessed_number = int(input("I am thinking of a number between 1 and 10, guess it: "))
 if guessed_number == number:
   break
 else: print("Incorrect, guess again.")
   
print("Correct")

# Explaining the differences between: for VS while, if VS elif VS else, break VS continue:
# for goes through a variable or list, allowing you to check if a condition is true however, while repeats a loop until something occurs, allowing the loop to break or finish
# if loops stay open even if the checked condition is true or false, allowing you to manipulate lists and variables, elif says "if that wasnt true, check whether this is true", else says "if that condition isn't true and that condition isn't true, then you must do this."

def number_of_steps(num):
 steps = 0
 while num != 0:
   if num % 2 == 0:
     num //= 2
    
   else:
     num -= 1
   steps += 1
 return steps
print(f'Number becomes 0 in {number_of_steps(200)} steps')

# Count the Number of Digits in a Number, Given an integer num, return the number of digits in num that divide num.

def is_number_divisible(number):
  digit_counter = 0
  for digit in str(number):
   if int(digit) != 0 and number % int(digit) == 0:
    digit_counter += 1
  return digit_counter
print(f' Number is divisible by {is_number_divisible(1248)} of its own digits')
 
def steps_to_zero(numero):
    steps = 0
    starting_step = 1
    while numero != 0:
        if numero % 2 == 0:
            numero //= 2
            print(f" \nThis was Step {starting_step} and the number is now: {numero}")
        else:
            numero -= 1
            print(f" \nThis was Step {starting_step} and the number is now: {numero}")
        steps += 1
        starting_step += 1
    return steps

print(f'\nThere are {steps_to_zero(2000)} steps required before 2000 becomes zero.')

# LeetCode 122: Best Time to Buy and Sell a Stock II. #Greedy

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):  
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices [i-1]  
    return profit
print (f"\n The maximum amount of profit you can achieve is: {maxProfit([7,1,5,3,6,4])} USD")

#Rewritten for all scenarios.

def maxProfit(prices):
    hold = -prices[0]  # By buying the stock on day 0, so your profit is negative (you spent money)
    sold = 0          # - No transactions yet, so your profit is 0 if you're not holding any stock.
    for i in range(1, len(prices)): # Loop through each day starting from day 1 
        hold = max(hold, sold - prices[i])  # 2 Options. 1) Keep holding, profit doesn't change. 2) - Buy today, subtract today's price to simulate buying
        sold = max(sold, hold + prices[i])  # 2 Options 1) Continue not holding, profit doesn't change. 2) - Sell today, add today's price to simulate selling
    
    return sold
print (f"\n The maximum amount of profit you can achieve is: {maxProfit([7,1,5,3,6,4])} USD")

#




