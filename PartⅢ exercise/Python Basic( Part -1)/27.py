'''
27. Write a Python program to concatenate all elements in a list into a string and return it
'''
# my solution
def put_all_elements_in_a_list_into_a_string(list):
    new_string = ''
    for element in list:
        new_string += str(element)
    return new_string

print(put_all_elements_in_a_list_into_a_string([1,5,12,2]))
