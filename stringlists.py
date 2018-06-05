import random
import sys
import os

test_string = input('Enter in a word and check if it is a palindrome: ')
test_string = str(test_string)

# this is an example of string reversal
reverse = test_string[::-1]

if test_string == reverse:
    print('It is a palindrome')
else:
    print('It is not a palindrome')
