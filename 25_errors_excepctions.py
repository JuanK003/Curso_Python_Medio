#print(0/0)) # SyntaxError: unmatched ')'

#print(0/0) # ZeroDivisionError: division by zero

#print(result) #NameError: name 'result' is not defined

'''
suma = lambda x, y: x + (y * 2)
# Checking that the result of the function suma is equal to 4.
assert suma(2,2) == 4 # AssertionError
print('hola')
'''

'''
age = 10
if age < 18:
    # Raising an exception.
    raise Exception('No se permite menores de edad') #Exception: No se permite menores de edad
'''