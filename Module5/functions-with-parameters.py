# parameters are values that you pass to a function

# example
# to find the average from multiple values in a list, you can use the following code
input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

sum = 0.0
for number in input_numbers:
    sum += number
average = sum / len(input_numbers)
print(average)
# 7.24

# to turn the code above into a function

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)
get_average([5.0, 3.5, 7.8, 9.9, 10.0])

# the 'input_numbers' in brackets is a parameter
# a parameter can onlybe defined inside a pair of brackets after the function name and it only exists inside a given function
# a value is assigned to the parameter when the function is invoked
# in the example above, the list of numbers is an argument (the get_average function is called with this argument and the value of the argument is assigned to the parameter 'input_numbers')


# you can define functions with more than one parameter
# example: a function that takes a string and counts the no of times the letter appears in the string

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
print_letter_count('Welcome', 'e')

print_letter_count('People say nothing is impopssible, but I do nothing every day.', 'a')
    
# order of arguments is important
print_letter_count('e', 'Welcome')
# 'Number of Welcome is 0'

# positional arguments: the argument values are assigned to the parameters based on their position
# most frequently used argument

# python also allows for 'named arguments'
print_letter_count(text='Welcome', letter='e')

print_letter_count(letter='e', text='Welcome')
# 'Number of e is 2'

# in the named arguments above, we specify which value should go to which parameter