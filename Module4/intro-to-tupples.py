# tupples are similar to lists
# tupples are a collection of multiple elements, and all the elements can have the same or different data types

# tupples are created with round brackets ()
empty_tuple = ()

# to create a tupple with one element:
# option a
on_el_tupple_a = (1,)

# option b
one_el_tupple_b = 1,
# for option b, the comma is required for proper tupple syntax 

# for a tupple with multiple elements, the final comma is optional
three_el_tupple = 1, 2, 3,
print(three_el_tupple)

# mutability is an important difference between lists and tupples
# mutable: data can be freely updated anytime you want e.g lists
# immutable: data cannot be updated at any time e.g tupple

# tupples are immutable, however you can assign a new tupple to the same variable
user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980)

# tupple elements cannot be added to appended, would result in an error
user_data.append('teacher')

# tupple elements cannot be deleted, would result in an error 
del user_data[0]

# indexing and slicing can be used to get tupple elements
print(user_data[0]) 
# Katya

# indexing cannot be used to change individual elements
user_data[0] = 'Mark'


# strings are also immutable























