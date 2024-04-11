# methods in python are a type of function that 'belong' to specific data
# methods exists alongside the data it belonhs to
# if there's no data, you can't use the methods function
# unlike functions like 'print' or 'input' that are not tied/owned by a data


# to add an element to a list, you can use the append methood 
book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4)
print(book_ratings)

# the append method belongs to the book_ratings list

# methods are invoked using its name and a pair of brackets with arguments inside
# unlike functions, methods are invoked with a '.' after the function the work on

# to add an element to other places in a list
# use the 'insert' method
book_ratings = [7, 9, 5, 6, 8]
book_ratings.insert(1, 10)
print(book_ratings)

# the insert invocation above add the value of 10 (second argument) to the position of index 1