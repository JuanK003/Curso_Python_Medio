"""
    Map() takes a function and an iterable as arguments, and returns a new iterable with the function
    applied to each argument
    
    :param item: This is the item that we're going to be adding taxes to
    :return: A new list with the same items as the old list, but with a new key/value pair.
    
items = [
    {
        'product': 'shirt',
        'price' : 100,
    },
    {
        'product' : 'pants',
        'price' : 300
    },
    {
        'product': 'tennis',
        'price' : 250,
    }
]

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print('New List')
print(new_items)
print('\nOld list')
print(items)
"""

#==========================================================

'''
Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.

La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada.
'''

def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda x : x * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)