# dictionaries are collections used to store key value pairs

# example
emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel.com'
}
print(emails['Mark Steel'])
# the example above uses dictionary as a phone book.

# to access specific values in a dictionary, provide the key within the same square brackets as above

# example: language dictionary
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pájaro'
     }
  print(spanish_animals['bird'])   
  
# rules to follow when creating dictionaries:

#1 dictionaries are created with curly brackets
#2 inside the curly brackets you provide a key-value pair, colon, and then a value for the key
#3 add a comma to introduce another key value pair

#4 each key must be unique, you can't have more than one identical key
# python replaces the old value with the new one
# example
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pájaro',
    'bird': 'el ave'
    }
print(spanish_animals['bird'])

# note: when you use quare brackets to find the value of a key, it works one way
# you can't provide a value to find its key, it would return an error
print(spanish_animals['el perro'])
# a dictionary is a one way tool

# keys used in dictionaries can be any other immutable data type apart from strings like integers, floats, tuples BUT not lists
# example
tennis_ranking = {
    1: 'Ashleigh Barty',
    2: 'Naomi Osaka',
    3: 'Simona Halep'
    }
# the keys are integers

tennis_ranking = {
    [1]: 'Ashleigh Barty',
    [2]: 'Naomi Osaka',
    [3]: 'Simona Halep'
    }
# TypeError: unhashable type: 'list'

# while a list can't become a key, it can be a value in dictionary
# example
city_ratings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanoi': [7, 6, 4, 5],
    'Manila': [6, 6, 4, 4, 5]
    }


