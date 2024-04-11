# functions can typically
# 1 cause some effect
# 2 return a meaningful value

# print function causes an effect, it doesn't return a meaningful value
print('Hello') 

# len function doesn't cause an effect but returns a meaningful value, the number of elements in a string
length = len('hello')

# input function both causes an effect (by prompting the user to provide a value), and returns the value.
number = input('What is the number?')

# although the main role of print is to cause an effect and does not return any 'meaningful' value, it returns a 'special return value'
# example
print_return = print('Hello world')
print(print_return)
# 'Hello world'
# 'None'

# none is a special value in python
# it is used to describe a null value or no value at all

# none is not zero
# none is not false
# none is not the same as an empty string

x = None

if x:
    print("None is True")
elif x is False:
    print ("None is False")
else:
    print("None is not True, or False, None is just None")
# 'None id not True, or False, None is just None'

x = None
if x is None:
    print('yes')
if x == None:
    print('it does')
# 'yes' # 'it does'

# you can assign none to a variable
# you can check if the value of a variable equals none

# none is a value returned implicitly by values that do not return anything meaningful
def greet():
    print('hello!')

x = greet()
print(x)
# 'hello!' # 'none'