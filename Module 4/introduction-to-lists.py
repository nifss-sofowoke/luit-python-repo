# basic data types: (integers, floats, booleans, strings) are called 'basic' because you can only store one value at a time inside them.

# complex data types aka collections aka container data types are used to solve the problem of 'basic' data types.

# collection is a data type in python that can store more than one value in a single variable

# 3 types of collections
# 1 lists
# 2 tupples
# 3 dictionaries 

# Lists
# used to store multiple values of the same type of data e.g multiple floats/integers

# example
# to make a list of top cities
city_1 = 'New York City'
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix'

# declare an 'empty list' using a pair square brackets
empty_list = []
# tip: immediately think of a list when you see a declaration in [] separated by commas

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)

# note: the elements in a list are numbered and indexed
# note: list indices start at 0 (not 1)

# to output a specific element in the list and not the entire list, provide the element's index in a pair of square brackets a.k.a 'Indexing'
print(top_cities[2])

# trying to access an element that doesn't exist using an index leads to an error
print(top_cities[6])

# you can also use negative indices to access elements from the list
# python reads the list from the back
print(top_cities[-2])
print(top_cities[-5])
# think of it as a number line with both a positive and negative side and 0 in the middle

# you can also access a few elemnts from a list using 'Slicing'
# the colon is used for slicing
print(top_cities[0:2])

# in slicing:
# the above outputs the first and second cities on the list
# the first index is the first element to include in the slice and the second index is the first element to not include
# therefore, list only elements with index 0-1 

# remember: 1st index INCLUSIVE, 2nd index EXCLUSIVE
# similar to 'range functions' in loops

# more slicing

print(top_cities[:2])
# omitting first index means from the start of the list to the excluded element

print(top_cities[0:])
# omitting second index means until the end of the list

print(top_cities[:])
# omitting both indexes means all the elements

# an empty list would be outputted when you slice indexes that do not exist
print(top_cities[10:15])

# accessing a single element produces a string value
print(top_cities[0])

# using slicing gives you a list with a single string inside
print(top_cities[0:1])

