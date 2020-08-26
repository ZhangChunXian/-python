'''
Write a Python program to compute the greatest common divisor (GCD) of two positive integers
'''

# my solution
def  compute_the_great_common_divisor_of_two_positive_integers(a, b):
    max_divisor = 1
    for i in range(min(a, b)):
        if a % (i+1) == 0 and b % (i+1) == 0:
            max_divisor = i+1
    return max_divisor

print(compute_the_great_common_divisor_of_two_positive_integers(12,6))
print(compute_the_great_common_divisor_of_two_positive_integers(4,6))

