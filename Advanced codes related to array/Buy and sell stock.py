def stock(arr):
    n= len(arr)
    min_price = min(arr)
    i = arr.index(min_price)
    max_profit=0
    max_profit_after_min=0
    for j in range(i+1,n):
        max_profit_after_min= max(max_profit_after_min,arr[j])
        profit = max_profit_after_min - min_price
        
        # Update max profit if this profit is greater
        max_profit = max(max_profit, profit)

    return max_profit

# Example usage
prices = [10, 7, 5, 8, 11, 9]
profit = stock(prices)
print(f"Maximum profit: {profit}")