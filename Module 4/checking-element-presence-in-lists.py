# remember: the 'in' keyword whn used in a loop indicates the range of possible values for a controlled variable
# example
for char in 'happy message':
    print(char)

# the 'in' operator can also be used to check whether a given element is present in a list
# example
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')
    
# the negated in operator, 'not in' 
# returns 'True' if element is not in list

# example
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')