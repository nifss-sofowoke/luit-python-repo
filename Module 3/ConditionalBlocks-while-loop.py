# loops are used to repeat an instruction or many instructions

# basic while syntax:
# whilecondition:
    #do_something()
    #do something2()
# means as long as the condition is met, call 'do something' & 'do something2' repeatedly

# example
counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')

# don't forget about incrementing (+=) the value in the loop
# you would get an infinite loop (condition is always true) if you don't increment

# while loops are often used when you don't know how many times to execute the loops body
# often when working with user input

secret_number = 14
print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')

