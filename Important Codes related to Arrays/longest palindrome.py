def is_palindrome(num):
    return str(num)==str(num)[::-1]

def longest_palindrome(arr):
    longest_palindrome= None
    for num in arr:
        if is_palindrome(num):
            if longest_palindrome is None or num>longest_palindrome:
                longest_palindrome=num

    return longest_palindrome

arr= [121,131,123321,123456654321]

result= longest_palindrome(arr)
print(result)

