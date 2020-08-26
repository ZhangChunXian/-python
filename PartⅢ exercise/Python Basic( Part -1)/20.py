'''
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string
'''

# my solution
def duplicate_string(n, str):
    for i in range(n):
        print(str,end='')

duplicate_string(2, 'abc')

# The Sample Solution
def larger_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result
