import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
        'Country': 'Guatemala',
        'Population' : '5000'
    },
    {
        'Country': 'Colombia',
        'Population' : '200'
    }
]

country = input('Elige cualquiera de estos dos paises (Guatemala, Colombia) => ').title()
result = utils.population_by_country(data, country)
print(result)