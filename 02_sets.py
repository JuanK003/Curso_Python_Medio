set_countries = {'col', 'mex', 'bol'}
print(set_countries)

set_numbers = {1, 2, 3, 4, 5, 6}
print(set_numbers)

set_types = {1, 'hola', False, 1.22}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

# Creating a set from a tuple.
set_from_tuples = set(('abc', 'ghj', 'iok'))
print(set_from_tuples)

# Creating a list of numbers, then creating a set from that list, then printing the set, then creating
# a list from the set, then printing the list.
numbers = [1, 2, 3, 4, 1, 2, 3, 4, 5]
set_from_numbers = set(numbers)
print(set_from_numbers)

unique_nums = list(set_from_numbers)
print(unique_nums)