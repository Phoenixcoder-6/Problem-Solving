def count_numbers(string):
    count=0
    for num in string:
        if num.isdigit():
            count+=1
    return count

string="ankita99Ghosh01"
res= count_numbers(string)
print(res)