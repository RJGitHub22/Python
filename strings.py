import random
import sys
import os

long_string = "I tried to make out a life in the Midwest but the rust belt keeps breaking promises"

# outputs characters from 0 to 4
print(long_string[0:4])

# outputs last 5 characters
print(long_string[-5:])

# outputs up to last 5 characters
print(long_string[:-5])

# join strings
print(long_string[:2] + "am Soupy")

# capitalize first letter
print(long_string.capitalize())

# return index value from start of string
print(long_string.find("Midwest"))

# check if all characters in string are letters
print(long_string.isalpha())

# check if all characters are numbers
print(long_string.isalnum())

# find length
print(len(long_string))

# replace word with another
print(long_string.replace("Midwest", "Southwest"))

# split string into list
quote_list = long_string.split(" ") # put how words need to be separated
print(quote_list)
