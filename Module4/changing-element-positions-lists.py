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

# using python shortcut for swapping
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

# the shortcut (comma) above can also be used with swapping list elements
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

# you can also change element positions by sorting a list

# the sort method sorts a list of strings alphabetically and numbers from lowest to greatest

# sort with strings
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

# sort with numbers
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

# sort in reverse using a keyword argument
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

# using the sort method as above changes the list it belongs to, the operation cannot be undone
# if you want to keep the original list, use a general list function using 'sorted'
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)

# remember:

# list_name.sort() -- sorts the original list
# sorted(list_name) -- gives back a new, sorted list while keeping the original list unchanged
