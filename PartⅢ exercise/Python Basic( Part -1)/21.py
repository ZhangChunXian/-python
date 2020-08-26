'''
21. Write a Python program to find whether a given number (accept from the user) 
is even or odd, print out an appropriate message to the user.
'''
# My solution
def return_even_or_odd(n):
    try:
        if n % 2 == 0:
            return 'The number is even.'
        else:
            return 'The number is odd.'
    except ValueError:
        print("please enter a integer: ")


try:
    given_number = int(input("please enter a number: "))
except (ValueError, SyntaxError, NameError):
    print("please enter a integer! ")
else:
    print(return_even_or_odd(given_number))

