# to copy a list into a new variable

# when copying the content of a variable into another operator using an assignment operator,
# both variables would have the same value but they are independent of each other
# updating the content of one variable after the copy does not affact the other variable

# example
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)
# Daenerys Targaryen Jon Snow

# rules in lines 3-5 applies to integers, floats but not lists

list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
# Original: [-5, 2, 3]
# New: [-5, 2, 3]
# the new list is modified after updating the original list

# why?
# in complex data types like lists, the name of the list does not point to the actual list in the computer memory
# rather, the name of the list is the memory location where the list is stored
# these are known as references

# to actually make a copy of list so 2 variables have 2 separate lists that can be modified independently,
# use SLICING

# example
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
# Original: [-5, 2, 3] 
# New: [1, 2]

# summary
# to create a new variable that points to the same list:
list_original = [1, 2, 3]
list_new = list_original

# to copy a list and have 2 diff list with 2 diff variables:
list_original = [1, 2, 3]
list_new = list_original[:]
