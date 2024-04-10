# to create a long list, use 'list comprehension'

# using a for loop  with the append method is inefficient; syntax is long
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# use 'list comprehension' instead

# example
numbers = [i for i in range(1, 101)]
print(numbers)

numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)