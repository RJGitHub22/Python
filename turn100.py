import random
import sys
import os

print('What is year were you born?')

year = sys.stdin.readline()

age = 2018 - int(year)
hundred = int(year) + 100

print('You will turn ' + str(age) + ' this year' )
print('You will turn 100 in the year ' + str(hundred))

line = 'You will turn 100 in the year ' + str(hundred) + "\n"
print("How many times do you want to print the the previous line?")

times = sys.stdin.readline()

print(int(times) * line)
