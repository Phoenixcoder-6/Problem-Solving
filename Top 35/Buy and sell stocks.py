def stock_profit(prices):
    min_price= min(prices)
    min_index= prices.index(min_price)
    rest= prices[min_index+1 :]
    if not rest:
        return prices[min_index], prices[min_index]  # No data after buy day
    max_price = max(rest)
    return prices[min_index], max_price

arr=[7,2,3,5,4,6]
res1,res2= stock_profit(arr)
print(res1,res2)
