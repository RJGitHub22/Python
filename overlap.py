import random
import sys
import os

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = range(1, random.randint(1,50))
b = range(1, random.randint(1,40))

new = []

for num in a:
    if num in b:
        if num not in new:
            new.append(num)

print(new)

# Another example using names

students = ['Joshua', 'Lani', 'Manuel', 'Nikki']
name = input('Type a name to check: ')

if name in students:
    print('This student is enrolled!')
else:
    print('This student is not enrolled')
