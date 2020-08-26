'''
number = int(input("Sample value of n is "))
number_init = number

numbers_sum = 0

for i in range(1,4,1):
    numbers_sum = numbers_sum + number
    number = number*10 + number_init

print(f"Expected Result: {numbers_sum}")
'''

# The Sample Solution
a = int(input('Input an integer: '))
n1 = int("%s"%a)
n2 = int("%s%s"%(a,a))
n3 = int("%s%s%s"%(a,a,a))
print(n1+n2+n3)


