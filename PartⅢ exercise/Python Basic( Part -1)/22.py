'''
22. Write a Python program to count the number 4 in a given list.
'''


# my solution
def count_number_4(numbers):
    amount = 0
    for number in numbers:
        if number == 4:
            amount += 1
    return amount

print(count_number_4([1,4,6,7,4]))