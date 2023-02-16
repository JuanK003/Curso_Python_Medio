def get_population():
    keys = ['GT', 'COL']
    values = [5000, 200]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
