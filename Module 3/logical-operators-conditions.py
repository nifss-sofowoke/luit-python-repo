#logical operators used in python
#
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# == equals
# != not equals

# example
password = input('Do you know the secret password?')
if password != '--secret':
    print('not correct')
else:
    print('correct password')
    
# when python sees a condition with one of the logical operators,
# it checks whether the condition is met or not
# the result is always a boolean value
# a boolean variable could be
# True or False (do not put them in quotes & must start with caps)

if True:
    print('Condition met')
# condition met

if False: 
    print('Condition met')
# code not executed

if 2 == 2:
    print('true')
#true

if 1 == 2:
    print('true')
    
if 2 == 2.0:
    print('true')
#true