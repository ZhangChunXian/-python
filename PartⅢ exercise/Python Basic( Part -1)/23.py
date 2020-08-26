'''
23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2.
'''

def get_n_copies_of_the_first_2_characters_of_a_string(n, str):
    return_string = ''
    if len(str) < 2:
        for i in range(n):
            return_string += str
    else:
        for i in range(n):
            return_string += str[:2]
    return return_string

print(get_n_copies_of_the_first_2_characters_of_a_string(9, 'a'))

