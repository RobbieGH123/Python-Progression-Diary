                                                                      ## Day 28 Progression Test ##

# Reverse String Function

def reversestring(s):

    j = len(s) -1
    reversed_string = ''

    while j >= 0:
        reversed_string += (s[j])
        j -= 1
    return reversed_string

# Is_Palindrome?

def is_palindrome(s):

    reversestring(s)
    if s.lower() == reversestring(s).lower():
        print("Yes, that is a palindrome")
        return True
    else:
        print("No, that is not a palindrome")
        return False
is_palindrome("Racecar")

def two_sum(lst, target):
    left = 0
    for i in lst:
        while i <= len(lst) -2:
            if lst[left] + lst[i+1] == target:
                return left, i + 1
            else:
                i + 1
print(two_sum([0, 1, 2, 3, 4], 5))

## Fibonacci Number Function ## 

def fib_nums(n):

    fibbed = 0
    fib_list = []


    for i in range(fib_list):
        while i <= n:
            if i == 0:
                fib_list.append(0)
            if i == 1:
                fib_list.append(1)
            else:
             fib_list.append(fib_list[i-1] + fib_list[i-2])
        print(fib_list[i])
        return fib_list[i]
print(f" The fibonnaci number at n is {fib_nums(5)}")




            



