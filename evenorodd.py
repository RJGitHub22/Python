import random
import sys
import os

print("Please enter a number: ")

num = sys.stdin.readline()

if (int(num) % 4 == 0):
    print("You entered an even number that is divisble by 4")
elif (int(num) % 2 == 0):
    print("You entered an even number")
else:
    print("You entered an odd number")

print("\nEnter another number and we'll check if it can evenly divide the previous")

check = sys.stdin.readline()

if (int(num) % (int(check)) == 0):
    print("It divides evenly!")
else:
    print("It has a remainder...")
