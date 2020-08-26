'''
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''
#%%
# The Sample Solution
print(abs.__doc__)

b = [1, 2, 3]
b?

print?
#%%
def add_number(a, b):

    # Add two numbers together

    # Returns
    # -------
    #the_sum : type of argument

    return a + b
    '''
    try some different to test
    '''

add_number?
#%%
print("hello world", "hello", "world", sep = '&', end = '^', flush = True)
print("try")
#%% 
import numpy as np

print(b)

#%%import numpy as np
import numpy as np

print(b)

%paste
#%%
a = np.random.randn(100, 100)

%timeit np.dot(a,a)