# scope of a name = variable name
# the scope of a name is the part of the code where the name is properly recognizable and can be used

# you can define avariable outside a function because varaibles that exist outside a function like below have a scope insdie the function's body

def show_truth():
    mysterious_var = 'New Surprise!' #local variable in function
    print(mysterious_var)

mysterious_var = 'Surprise!' # global variable outside function
print(mysterious_var)
show_truth()
print(mysterious_var)
# Surprise!
# New Surprise!
# Surprise

# the code block above is an example of 'shadowing'
# the local variable shadowns the global variable
# the global variable is available before and after the function call hence 'surprise' on line 15 & 17
        # during the function call, it is shadowed by the local variable with the same name hence 'new surprise'

# shadowing prevents the modification of the values of your global variables by functions written by other people

# to modify a global vraiable within a function, use the 'global' keyword
def show_truth():
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)
# Surprise!
# New Surprise!
# New Surprise!

# the 'global' function means don't use shadowing for the variable 'mysterious_var'
# try to avoid using the 'global' keyword, it does more harm than good most times

# shadowing with lists
def show_truth():
    mysterious_var = ['New Surprise!'] #local variable
    print(mysterious_var)

mysterious_var = ['Surprise!'] #global variable
print(mysterious_var)
show_truth()
print(mysterious_var)
# ['Surprise!']
# ['New Surprise!']
# ['Surprise!']

def show_truth():
    mysterious_var.append('New Surprise!')
    print(mysterious_var)

mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)
# ['Surprise!']
# ['Surprise!', 'New Surprise!']
# ['Surprise!', 'New Surprise!']

# the assignment operator '=' is not used

# summary:
# if you assign a new list to the same variable in a function, shadowing works fine
# if you change a list using a method using square brackets or the 'del' instruction, the list outside the function will reflect the change
# also applies to dictionaries