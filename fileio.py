import random
import sys
import os

# create and open file
test_file = open("test.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("text to add to file\n", 'UTF-8')) # need bytes and UTF-8 there to write

test_file.close

test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

# remove file
os.remove("test.txt")
