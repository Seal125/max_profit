'''
PEDAC Process

P - Buy the lowest price first, then sell for the highest price. Smallest number has to go first. Can't find the smallest and the largest number at the same time. In accordance to time, we can buy whenever we want, but it's best to then look for the maximum profit with what you bought.

E - stock_prices = [1, 7, 30, 66, 20, 56]
    get_max_profit(stock_prices) == 65 #because we buy for $1 and sell for $66

    get_max_profit([300,100,120,21,0,12]) = 20
    get_max_profit([100,120,21,300,0,12]) = 279
    ***get_max_profit([300,120,100,21,12]) == -9 #when there is no profit, we have to find the lowest loss of profit
    get_max_profit([12,30,1,24,0,2]) == 23
    get_max_profit([10,15,7,25,8]) == 18

D - List

A -
    0. Declare variable `max-profit` = list[1] - list[0]
    1. Loop through list (i)
      a. For each element, loop from the next index to the end of the list (j)
        i. if list[j] - list[i] > `max-profit`
            then max_profit = list[j] - list[i]
    return max-profit
'''

def get_max_profit(prices):
    maxprofit = prices[1] - prices[0]

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > maxprofit:
                maxprofit = prices[j] - prices[i]

    return maxprofit

print(get_max_profit([300,100,120,21,0,12]) == 20)
print(get_max_profit([100,120,21,300,0,12]) == 279)
print(get_max_profit([300,120,100,21,12]) == -9) #when there is no profit, we have to find the lowest loss of profit
print(get_max_profit([12,30,1,24,0,2]) == 23)
print(get_max_profit([10,15,7,25,8]) == 18)


#Better Solution - Method 2

def max_profit(prices):
    maxprofit = prices[1] - prices[0]
    minprice = prices[0]

    for i in range(1, len(prices)):
        if (prices[i] - minprice) > maxprofit:
            maxprofit = prices[i] - minprice
        if prices[i] < minprice:
            minprice = prices[i]

    return maxprofit

print(max_profit([5, 12, 7, 2, 20]))