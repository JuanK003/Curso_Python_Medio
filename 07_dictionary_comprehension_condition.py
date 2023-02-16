'''
{key: value for var in iterable if condition}
key: value → Elemento llave-valor
for var in iterable → Ciclo donde se extraen elementos de cualquier iterale
if condition → Condición opcional para filtrar elementos
'''
import random as ra

# Creating a dictionary with the countries as keys and the populations as values.
countries = ['col', 'mx', 'gt', 'pe']
populations = {country: ra.randint(1, 100) for country in countries}

print(populations)

result = {country: population for(country, population) in populations.items() if population > 20}
print(result)

# Creating a dictionary with the vowels of the text as keys and the vowels in uppercase as values.
text = 'Hola, soy Juan Carlos'
dict = { carac: carac.upper() for carac in text if carac in 'aeiou'}
print(dict)