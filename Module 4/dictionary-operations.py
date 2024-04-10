# dictionary operations:

# you can add elements to an empty dictionary
# example
grades = {}

# add elements to dictionaries using square brackets
grades['John'] = 'A-'
grades['Amy'] = 'B'
print(grades)
# {'John': 'A-', 'Amy': 'B'}

# you can update the dictionary using the same syntax
grades  ['Amy'] = 'A'
print(grades)
# {'John': 'A-', 'Amy': 'A'}

# you can also use the 'update method'
grades.update({'John':'A'})
print(grades)
# {'John': 'A', 'Amy': 'A'}

# use the 'len' function to check the number of key value pairs in a dictionary
print(len(grades))
# 2

# use 'in' operator to check if a given key is present in a dictionary
if 'John' in grades:
    print('John got:', grades['John'])
# John got: A

# use the 'del' operator to delete a key alongside its value
del grades['John']
print(grades)
# {'Anne': 'A'}

# to iterate a dictionary, you can:

# use a for loop
for el in grades:
    print(el)
# John
# Anne

# use the 'keys' method
for el in grades.keys():
    print(el)
# same result as above

# to get access to the values alone, you can use:
# the 'values' method
for el in grades.values():
    print(el)
# A- B

# to get access to both the keys and the values, use:
# the 'items' method
for person, grade in grades.items():
    print(person, 'got', grade)
# John got A-
# Anne got B

