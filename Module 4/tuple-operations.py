# tupples are immutable unlike lists
# once created, tupple elements can't be changed

# tupple operations:
# len function: to count the number of elements in a tupple
user_data = ('John', 'American', 1964)
print(len(user_data))

# in & not in operators
user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US!')
    
# for loop to iterate a tuple
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)
    
# using the '+' opeartor to add tuples together
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)
# this produces a new tuple

# tuples can also be multiplied by an integer like lists
# to repeat tuple elements
numbers = (0, 1) * 10
print(numbers)  


# when to use lists vs tuple

# lists are typically used in situations when you want to have many values of the same data type
    # when the values represent examples of the same class or phenomenon
# example
male_name = ['Adam', 'Jerry', 'Mark']

# tuples are often used when you want to group together values of different types that are somehow related
    # and together they form some sort of structure/bigger data.
# example
user_data = ('John', 'American', 1964)



# tuples are also used to perform certain python operations quicker
# swapping the variables of two elements in lists
first = 5
second = 7
first, second = second, first