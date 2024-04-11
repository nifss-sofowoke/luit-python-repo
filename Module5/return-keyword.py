# how to return a meaningful value from a function

# use the keyword 'return'

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print (average)
    
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    
# brackets are not used around the keyword return, it is not a function
# by modifying the function, it no longer prints the average to the output, it doesn't cause any effect
# it now returns a meaningful value

print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))
# The average is: 7.24

# you can store the result in a variable
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')
# The average is too high!

# the keyword return gives the result, but it also immediately exits the function
# therefore, any instruction after the return statement will be ignored
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')

get_average([2])


def is_first_last_equal(number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_last_equal([10, 20, 30, 40, 10]))
# True

print(is_first_last_equal([10, 20, 30, 40, 50]))
# False

print(is_first_last_equal([]))
# passing an empty list as the argument returns an index error

# if the code is modified however, 
def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_last_equal([]))
# 'None'