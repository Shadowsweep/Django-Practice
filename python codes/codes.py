## stating with dictionary 

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Original dictionary:", my_dict)

# Modifying the dictionary
my_dict['age'] = 26  # Updating value
my_dict['country'] = 'USA'  # Adding new key-value pair
print("Modified dictionary:", my_dict)

# Array (list) example
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Modifying the list (mutable)
my_list[0] = 10  # Updating value
my_list.append(6)  # Adding new element
print("Modified list:", my_list)

# Immutable example (tuple)
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Indexing example
print("First element of list:", my_list[0])
print("First element of tuple:", my_tuple[0])

# Dictionary to tuple
dict_items = my_dict.items()
dict_tuple = tuple(dict_items)
print("Dictionary to tuple:", dict_tuple)

# Tuple to dictionary
tuple_data = (('name', 'Bob'), ('age', 30), ('city', 'Los Angeles'))
tuple_dict = dict(tuple_data)
print("Tuple to dictionary:", tuple_dict)