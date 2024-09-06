def max_product_sum(arr):
    n=len(arr)
    result= arr[0]
    for i in range(n):
        nul=arr[i]

        for j in range(i+1,n):
            result= max(result,nul)
            nul*= arr[j]

        result= max(result,nul)
    return result

arr=[1,-2,-3,0,7,-8,-2]
deck= max_product_sum(arr)
print(deck)