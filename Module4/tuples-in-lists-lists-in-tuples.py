# python allows you to put lists in tuple elements, and vice versa

# tuples in lists
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)

# you can put the tuples about various cities in a list
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]

# you can work with this tuple-in-list the same way you work with lists

for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])
    
    
# lists in tuples
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
# in the example above, we have a tuple of information about 'John', and one of the tuple elements is a list of his weight changes
# even though the tuple is immutable, you can add new elements to the list measurements

user_data[3].append(79.6)
print(user_data)
# Name: London , Country: UK , Population: 8.98
Name: Canberra , Country: Australia , Population: 0.4
Name: Algiers , Country: Algeria , Population: 3.9
# ('John', 'American', 1964, [77.0, 78.2, 77.5, 79.6])