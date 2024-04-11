# default parameter values

# end and sep are keyword/named arguments
    # they are used at the end of a function invocation after all the positional arguments
    # they are always optional and always have a default value
    
print('Hello', 'How are you?', end='.', sep='-')
# 'Hello-How are you?.'
# in the print function above, the 'end' argument has the default value of a new line character
                            # the 'sep' argument has the default value of a wide space character
                            
# how keyword arguments work when you create your own function
# examples
def print_letter_count(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
print_letter_count('how many letter a are here?')
# 'Number of a is 3'
# in the example above, the function was invoked with only one value, the string, and 'a' is used as the default letter

# default values can be provided for both of the parameters
def print_letter_count(text='This is the default string to search', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
print_letter_count()
# 'Number of a is 2'
# the function above is invoked with no arguments because both parameters have default values

# summary:
# when defining a value and its parameter, you can mix parameters with and without default values
# positional arguments must appear before any named arguments