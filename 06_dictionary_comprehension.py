'''
{key: value for var in iterable}
key: value → Elemento llave-valor
for var in iterable → Ciclo donde se extraen elementos de cualquier iterale
'''

# Creating a dictionary with the keys 1-10 and the values 2-20.
'''
dict = {}
for i in range(1, 11):
    dict[i] = i * 2

print(dict)
'''

'''
# Creating a dictionary with the keys 1-4 and the values 2-8.
dict = {i: i * 2 for i in range(1, 5)}
print(dict)
'''
import random

'''
# Creating a dictionary with the keys of the countries and the values of the population.
countries = ['col', 'mx', 'gt', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)
'''
'''
countries = ['col', 'mx', 'gt', 'pe']
population = {}
# Creating a dictionary with the keys of the countries and the values of the population.
population = {country: random.randint(1, 100) for country in countries}
print(population)
'''

names = ['Juan', 'Pedro', 'Manolo', 'Rony']
ages = [19, 55, 23, 22 ]

'''
{
    'Juan': 19,
    'Pedro': 55,
    'Manolo': 23,
    'Rony': 22
}
'''

# Creating a list of tuples.
print(list(zip(names, ages)))

# Creating a dictionary with the keys of the names and the values of the ages.
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)