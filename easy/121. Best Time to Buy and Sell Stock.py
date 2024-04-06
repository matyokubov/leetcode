#Input
prices = [7,1,5,3,6,4]

#Logic
def main(prices):
    left, right = 0, 1
    maxProfit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            # What if you sell it
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            # If left isn't profitable, then right is lower
            # So left as right might be profitable
            left = right
        right+=1
    return maxProfit
        
#Output
print(main(prices))
