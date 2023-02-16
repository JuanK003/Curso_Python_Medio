# Trying to divide by zero and catching the error.
try:
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

try:    
    # Checking that 1 is not equal to 1, and if it is not, it will print the message 'Uno no es igual que
    # uno'.
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        # Raising an exception.
        raise Exception('No se permite menores de edad') #Exception: No se permite menores de edad
except Exception as error:
    print(error)

#-----------------------------------------------------------------------------------------------------------------------

# Trying to divide by zero, checking that 1 is not equal to 1, and raising an exception if age is less
# than 18.
try:
    print(0 / 0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        # Raising an exception.
        raise Exception('No se permite menores de edad') #Exception: No se permite menores de edad
except Exception as error:
    print(error)
    
except AssertionError as error:
    print(error)
    
except ZeroDivisionError as error:
    print(error)