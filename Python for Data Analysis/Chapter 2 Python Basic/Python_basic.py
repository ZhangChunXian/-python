#%%
# Attributes and methods
a = 'foo'

getattr(a, 'split')


#%%
def is_iterable(object):
    try:
        iter(object)
        return True
    except TypeError:   #not iterable
        return False

is_iterable('a string')

#%%
is_iterable([1, 2, 3])

s = r'this\has\no\special\characters'

s
#%%
list1 = [1, 2, 3]

list2 = list1.copy()

if list1 is list2:
    print("same id")
else:
    print("different id")

#%%
list2 = list1.reverse()
print(list2)