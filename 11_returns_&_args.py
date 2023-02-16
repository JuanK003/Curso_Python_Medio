def find_volume(length, width, depth):
    """
    Given a length, width, and depth, find the volume of a box.
    
    :param length: 3
    :param width: 2
    :param depth: 5
    :return: The volume of a box with length 3, width 2, and depth 5.
    """
    return length * width * depth

result = find_volume(3, 2, 5)
print(result)

#-----------------------------------------------------------------------------------------------------------

def volume2 (length=1, width=1, depth=1):
    """
    The function volume2() has three parameters, length, width, and depth, and returns the product of
    the three parameters
    
    :param length: 1, defaults to 1 (optional)
    :param width: 19, defaults to 1 (optional)
    :param depth: 1, defaults to 1 (optional)
    :return: 19
    """
    return length * width * depth

result = volume2(width=19)
print(result)

#-----------------------------------------------------------------------------------------------------------

def volume3 (length=1, width=1, depth=1):
    """
    The function volume3() returns a tuple of three values: the volume of a box, the width of the box,
    and the string 'hola'
    
    :param length: 1, defaults to 1 (optional)
    :param width: 19, defaults to 1 (optional)
    :param depth: 1, defaults to 1 (optional)
    :return: a tuple with the result of the multiplication, the width and the text 'hola'
    """
    return length * width * depth, width, 'hola'

result, width, text = volume3(width=19)
print(result)
print(width)
print(text)