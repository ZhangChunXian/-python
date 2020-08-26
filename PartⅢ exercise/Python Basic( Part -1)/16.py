'''
 Write a Python program to get the difference between a given number and 17, 
 if the number is greater than 17 return double the absolute difference.
'''

given_number = float(input("Please enter the number: "))

if given_number >= 17:
    print(2*abs(float(given_number-17)))
else:
    print(abs(float(given_number - 17)))
