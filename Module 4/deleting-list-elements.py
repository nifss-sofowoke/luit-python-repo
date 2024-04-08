# to delete an element in a list, use the 'del' instruction
# example

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[2]
print(top_cities)

# when an element is deleted from a list as above, all values to the right are shifted left to prevent emoty spaces in the list
print(top_cities[2])
# chicago takes the spot and index of singapore


# to delete some elements from the list and keep some, use:
# use the 'del' instruction plus slicing

# example: keeping the 1st 3 elements and deleting the remaining 2
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[3:]
print(top_cities)

# deleting all elements in the list:
# use del plus a slice with both indices omitted
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[:]
print(top_cities)
# returns an empty list

# del can also be used to delete the list itself
# use del without slicing/indices
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities
print(top_cities)
# returns an error because variable is no longer available