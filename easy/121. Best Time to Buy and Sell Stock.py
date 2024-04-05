#Input
prices = [7,6,4,3,1]

#Logic
def main(prices):
    def findTheIndexOfTheMinValue(prices):
        ir = 0
        res = prices[ir]
        for i in range(len(prices)):
            if i!=len(prices)-1:
                if not res<=prices[i+1]:
                    res = prices[i+1]
                    ir = i+1
        return ir
    def findTheIndexOfTheMaxValue(prices):
        ir = 0
        res = prices[ir]
        for i in range(len(prices)):
            if i!=len(prices)-1:
                if not res>=prices[i+1]:
                    res = prices[i+1]
                    ir = i+1
        return ir
    idxMinPrice = findTheIndexOfTheMinValue(prices)
    if idxMinPrice!=len(prices)-1:
        pricesOfFuture = prices[idxMinPrice+1:]
        idxMaxPrice = findTheIndexOfTheMaxValue(pricesOfFuture)
        profit = pricesOfFuture[idxMaxPrice] - prices[idxMinPrice]
    else: profit = 0
    return 0 if profit<=0 else profit
        
#Output
print(main(prices))
