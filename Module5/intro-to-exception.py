# when you make an error in python, it gives a descriptive output that tells you what is wrong with your code e.g what line the error is 

# syntax error is a very common error in python

# value error is also a type of error that occurs when an object is given the incorrect value or if the value is missing altogether.

# both syntax and value errors are exceptions
# an exception is an event that occurs during the execution of a program, that disrupts the normal flow of program instructions

# when python encounters an unwanted event, it raises an exception and stops the program.

# to handle exceptions so the program can run normally, use 'try except'.

# example
value = int(input('Enter an integer: '))
print('The inverse of', value, 'is', 1/value)
# entering anything other than an integer outputs a valueerror

# to fix this code so when a user enters a value other than an integer, the program still runs normally, 'try except' is used
try:
    value = int(input('Enter an integer: ')) # code that could raise an exception
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so I will not calculate the inverse') # code that handles the exception
    
# the code above produces the output 'you did not provide a number..' when a user inputs 0
# to fix this
# note the specific names of the exceptions thrown when the user provides something that's not a number and when the user provides zero
# the two exceptions are a zerodivision error and a valueerror

#. expand the tri-except construction to distinguish between the two situations
try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
# a second except branch was provided and both branches have their exception names specified

# note:
# no of except branches are unlimited
# however, none of the exceptions can be specified more than once

# you can add a general except block (with no except name) to protect the program from exceptions that you don't think about
try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry')
