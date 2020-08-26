'''
24. Write a Python program to test whether a passed letter is a vowel or not.
'''

# my solution
def test_vowel_letter(str):
    if len(str) >= 2:
        return 'Please enter a single letter!'
    elif str in ['a', 'e', 'i', 'o', 'u']:
        return 'The letter is a vowel!'
    else:
        return 'The letter is not a vowel!'

print(test_vowel_letter('c'))

# The Sample Solution
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('a'))
