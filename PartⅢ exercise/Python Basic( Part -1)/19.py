'''
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.
'''
'''
given_string = input("Please give me a string: ")

if given_string[0] == 'I' and given_string[1] == 's':
    print(given_string)
else:
    new_string = 'Is' + given_string
    print(new_string)
'''

# The Sample Solution
def new_string(str):
    if len(str) >= 2 and str[:2] == 'Is':
        return str
    return "Is" + str
    