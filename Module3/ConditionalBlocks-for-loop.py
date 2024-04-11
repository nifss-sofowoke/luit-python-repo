# the for loop and while loop can be converted into each other

# for loops are used to go through all the elements in a specific sequence

# sequences are special data structures that can store more than one value that can be browsed sequentially
# a string is a sequence type (contains sequence of characters)

# example

for letter in 'hello!':
    print('Current letter:', letter)
    
# in 'for'' loops conditions are checked for you internally
# unlike while loops where you have to specify conditions
# 'in'is used to introduce the range of possible values for sequence to be scanned
# python knows when to end a for loop
# iterating=scanning a sequence
# in the example above, there are 6 iterations

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')

for counter in range(1, 11, 4):
    print(counter)
print('Finished!')
# the range function generates all the desired integer value for the controoled variable
# start value is included
# default start value is 0
# stop value is not included
