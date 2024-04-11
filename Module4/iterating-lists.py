# recall: sequences in python stores more than one value and can be browsed sequentiallt

# lists can be iterated as they are also sequences

# example
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current city:', city)
    
# the for loop is used to access the lists elements one by one using the controlled variable 'city'
# the for loop lists elements in the exact order provided
# in the example above you cannot access the element and the index

# to access the element and index, the 'len' function is used
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index], )
 
# example
 spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)   

# Define a list of spendings
# Initialize a variable to store the sum of spendings
# Add each spending amount to the sum
# sum = sum + spending