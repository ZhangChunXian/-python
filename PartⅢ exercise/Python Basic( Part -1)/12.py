'''
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''


import calendar

yy = int(input("Please input the year: "))
mm = int(input("Please input the month: "))

print(calendar.month(yy, mm))