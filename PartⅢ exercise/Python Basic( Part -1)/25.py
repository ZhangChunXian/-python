'''
25. Write a Python program to check whether a specified value is contained in a group of values.
'''

# my solution
def check_Whether_value_in_list(value, list):
    if value in list:
        return True
    else:
        return False

print(check_Whether_value_in_list(3, [1,5,8,4]))