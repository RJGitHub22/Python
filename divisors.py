import random
import sys
import os

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

# Original
#for elem in listRange:
#    if num % elem == 0:
#        print(elem)

# Alternate
divisor = []

for elem in listRange:
    if num % elem == 0:
        divisor.append(elem)

print(divisor)
