# you can use indexing and slicing with strings to read individual/group of characters

# example
fav_band = 'Green Day'
print(fav_band[6])
# D

print(fav_band[:6])
# Green

# Note: you cannot use indexing to change individual characters within a string
fav_band[6] = 'M'
# this would result in an error

# strings also have methods like lists
# strings have methods that transforms them and results in a new string

# upper and lower methods
text = 'please capitlise me'
text_cap = text.upper()
print(text_cap)
# PLEASE CAPITLISE ME

# string have methods that return true or false
# the 'isnumeric' method checks whether strimg contains digits only
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')
    
# 'islower' -- verifies if string contains all lowercase characters
