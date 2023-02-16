# Imprime donde se está ejecutando el archivo
import sys
print('\nUsando la libreria SYS =>',sys.path)

# Importa la librería para expresiones regulares
import re
text = 'Mi número de teléfono es 123456789, el código del país es 52, mi número de la suerte es 9'

result = re.findall('[0-9]+', text)
print('\nUsando la libreria RE =>',result)

# Importando la librería time
import time

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print('\nUsando la libreria TIME =>', timestamp)
print('Usando la libreria TIME =>', result)

# Importando la librería collections
import collections

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 1, 3, 1, 3, 5, 6, 7, 7, 7, 8]
counter = collections.Counter(numbers)
print('\nUsando la libreria COLLECTIONS =>', counter)