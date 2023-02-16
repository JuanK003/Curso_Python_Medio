set_countries = {'bol', 'gua', 'mex'}

# Finding the length of the set.
size = len(set_countries)
print(size)

print('col' in set_countries)

# Adding the element 'pe' to the set.
set_countries.add('pe')
print(set_countries)

# Updating the elements 'ar', 'cr', and 'pe' to the set.
set_countries.update({'ar', 'cr', 'pe'})
print(set_countries)

# Removing the element 'pe' from the set.
set_countries.remove('pe')
set_countries.remove('ar')
print(set_countries)

# Removing the element 'guate' from the set.
set_countries.discard('gua')
print(set_countries)

set_countries.add('arg')
print(set_countries)

# Clearing the set.
set_countries.clear()
print(set_countries)