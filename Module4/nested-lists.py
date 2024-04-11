# avoid mixing different data types as elements in a list
# all the elemnts of a list should have the same data type

# lists can have other lists as elements

# example
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

print(cells[0]) #to access the first element on the list
# ['A1', 'A2', 'A3']

cells[0][0] # to access specific elements in the sub-list
# 'A1'
cells[1][2]
# 'B3'

# using a for loop to iterate the list and print its elemnts
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
# Element: ['A1', 'A2', 'A3']
# Element: ['B1', 'B2', 'B3']

# to access individual string elements in the sub-list
# use nested for loops
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
# Element: A1
# Element: A2
# Element: A3
# Element: B1
# Element: B2
# Element: B3

# nested lists are used to represent multidimensional tables in computer programming

table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
# A1 A2 A3 
# B1 B2 B3

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)