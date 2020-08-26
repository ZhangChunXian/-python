'''
42. Write a Python program to determine 
if a Python shell is executing in 32bit or 64bit mode on OS.
'''

# The Sample Solution
import struct
print(struct.calcsize("P") * 8)