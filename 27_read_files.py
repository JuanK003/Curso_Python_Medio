#file = open('./text.txt')

'''
# Printing the content of the file.
print('Usando read() => ',file.read())
'''

'''
# Printing the content of the file line by line.
print('\nUsando readline() =>', file.readline())
print('\nUsando readline() =>', file.readline())
print('\nUsando readline() =>', file.readline())
'''

'''
for i in file:
    print('Usando for => ',i)
    
file.close()
'''

with open('./text.txt') as file:
    for line in file:
        print(line)