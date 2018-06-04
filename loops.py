import random
import sys
import os

for x in range (0, 10):
    print(x, ' ', end="")

print('\n')

grocery_list = ['Juice', 'Eggs', 'Milk', 'Coffee', 'Bread']

for y in grocery_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print(x)

# creates list of lists
num_list = [[1,2,3], [10,20,30], [100,200,300]]

# cycles through list of lists
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

# WHILE LOOPS

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    # changer for the loop
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20):
    if(i%2 == 0):
        print(i)
# this breaks loop at 9 instead of continuing to 20
    elif(i == 9):
        break
    else:
        i += 1
        continue # skips rest of loop and goes back up to condition
    i += 1 # needed since previous changer only works on even numbers
