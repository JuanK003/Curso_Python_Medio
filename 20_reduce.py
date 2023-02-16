# La función Reduce() trata de reducir a un único valor

import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
    """
    "reduce() applies a function to each item in a list, and returns a single value."
    
    The accum() function is called for each item in the list. The first time it's called, the counter is
    set to the first item in the list, and the item is set to the second item in the list. The second
    time it's called, the counter is set to the result of the previous call, and the item is set to the
    third item in the list. This continues until the end of the list is reached
    
    :param counter: The first parameter is the accumulator. It's the value that gets returned from the
    previous iteration
    :param item: The first item in the list
    :return: The result of the accum function.
    """
    print('counter =>', counter)
    print('item =>', item)
    return counter + item

result = functools.reduce(accum, numbers)

print('Resultado usando una función =>',result)

result2 = functools.reduce(lambda counter, item: counter + item, numbers)
print('\nResultado usando lambda =>', result2)