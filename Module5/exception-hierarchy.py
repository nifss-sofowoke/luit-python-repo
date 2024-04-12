# exception hierarchy

# at the top of the hierarchy is the 'BaseException'
    # the baseexception serves more as a template for other more specific exception types
    # is is typically only used as a template for internal python exceptions
    # templates that are not very specific concrete exceptions are called abstract or obstructive
    
# one level below is: 'Exception', 'SystemExit' and 'Keyboardinterrupt'
# Systemexit is an exception raised when the special method 'sys.exit'
    # it is used to terminate/closure program
    # sys.exit allows you close your program manually
    
import sys

user_name = input('What is your name? ')
if user_name == '':
  print('Empty name? I cannot work with that. I am closing the program. Bye!')
  sys.exit()
print('Hello,', user_name)
print('Let us get started...')
# providing an empty string causes the program to system exit, which immediately terminiates the program


# keyboardinterrupt exception is raised when a user presses a key combination that causes an interrupt to the executing script
while True:
  print('hi!')
  
# exception is a template for many of python's built in exceptions e.g valueerror, zerodivision error, arithmetic error etc
    # can be used as a template for your own exceptions
    
# beneath the second row, there's 'arithmeticerror' 'lookuperror', 'typeerror', 'valueerror'
# lookuperror
    # under lookuperror exists 'indexerror', and 'keyerror'
    # indexerror and keyerror appear when you work with collections like lists or dictionaries
    
# indexerror example
programming_languages = ["Java", "Python", "C++"]
print(programming_languages[10])

# keyerror example (dictionary)
ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
ages['Michael']


# typeerror indicates that the type of data you're trying to use is not correct in the given context
# example
age = input('What is your age? ')
print('In 10 years, you will be', age + 10)
# input always returns a sting unless specified to return an integer so trying to add a string + integer results in a type error


# valueerror exception is raised when a function or method receives an argument of the correct type, but with an actual value that is invalid for some reason
# example
age = int(input('What is your age? '))