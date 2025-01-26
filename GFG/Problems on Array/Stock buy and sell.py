def stock_buy(arr):
    n=len(arr)
    if n==0:
        return 0
    
    min_ele=arr[0]
    profit=0

    for price in arr:
        if price< min_ele:
            min_ele= price
        profit=max(profit, price-min_ele)

    return profit, arr[min_ele]


arr=[2,3,5,1,5,7,8,9]
result, position= stock_buy(arr)
print("Profit is:",result,"Stock buy at position:",position)