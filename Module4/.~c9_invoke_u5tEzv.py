# swapping the position of elements

# wrong method
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first = second
second = first
print('After swapping:', first, second)
# both varibles end up with the same value after swapping

# swapping the value of two variables require using an additional third variable
# save the value of the first variable to the temp. variable to prevent it from getting lost

# right method
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)

# using python shortcut for sw