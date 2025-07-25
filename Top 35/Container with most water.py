def max_area(tank):
    left= 0
    right= len(tank)-1
    max_area=0

    while left < right:
        width = right - left
        min_height= min(tank[left], tank[right])
        max_area= max(max_area, width * min_height)

        if tank[left] < tank[right]:
            left +=1
        else:
            right -=1

    return max_area


height = [1,8,6,2,5,4,8,3,7]
res= max_area(height)
print(res)
