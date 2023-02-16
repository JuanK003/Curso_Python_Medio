items = [
    {
        'product': 'shirt',
        'price' : 100,
    },
    {
        'product' : 'pants',
        'price' : 75
    },
    {
        'product': 'tennis',
        'price' : 232,
    },
    {
        'product' : 'jacket',
        'price' : 123
    }
]

#prices = [200, 150, 464, 246]

prices = list(map(lambda item: item['price'], items))
print(prices)

#==========================================================
def add_taxes(item):
    """
    For each item in the list, add a new key called 'taxes' and set it to the price times .19.
    
    :param item: the item in the list
    :return: A list of dictionaries with the key 'taxes' and the value of the price * .19
    """
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)

#==========================================================
