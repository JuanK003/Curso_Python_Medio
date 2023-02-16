# Printing the numbers from 1 to 10.
for i in range(1, 11):
    print('Usando un for => ',i)
    
# Creating an iterator object.
my_iter = iter(range(1,4))
print('\nUsando iter => ',my_iter)

# Creating an iterator object.
print('\nUsando next para iter =>',next(my_iter))
print('\nUsando next para iter =>',next(my_iter))
print('\nUsando next para iter =>',next(my_iter))