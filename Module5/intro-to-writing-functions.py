# functions are separated fragments of code

# you can create your own functions in python
# writing your own functions can help you divide your code into well isolated pieces and also make it easier to read
# it also improves efficiency when writing code

# how to create a simple function
# a function definition in python starts with the keyword 'def' (short for define)
# provide the function name you chose after a space
    # you can give any name to your function
    # function naming rules = naming variable rules
# provide a pair of round brackets after the function name followed by a colon
# on another indented line, start your function body
    # you need at leasta single indented instruction that will be executed everytime you invoke the function
    
# example
def greet ():
    print('Hello, my dear!')
    
greet()
greet()

# note: you can't invoke a function before you define it
# it's good practice to keep all your function definitions at the top of your file