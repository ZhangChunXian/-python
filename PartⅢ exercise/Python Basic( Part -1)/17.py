'''
17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 
'''

def near_thousands(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n) <= 100))

given_number = float(input("Please enter a number: "))
print(near_thousands(given_number))