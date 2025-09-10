# Workspace for testing code:

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):  
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices [i-1]  
    return profit
print (f"\n The maximum amount of profit you can achieve is: {maxProfit([7,1,5,3,6,4])} USD")

def maxProfit(prices):
    hold = -prices[0]  # By buying the stock on day 0, so your profit is negative (you spent money)
    sold = 0          # - No transactions yet, so your profit is 0 if you're not holding any stock.
    for i in range(1, len(prices)): # Loop through each day starting from day 1 
        hold = max(hold, sold - prices[i])  # 2 Options. 1) Keep holding, profit doesn't change. 2) - Buy today, subtract today's price to simulate buying
        sold = max(sold, hold + prices[i])  # 2 Options 1) Continue not holding, profit doesn't change. 2) - Sell today, add today's price to simulate selling
    
    return sold
print (f"\n The maximum amount of profit you can achieve is: {maxProfit([7,1,5,3,6,4])} USD")