'''
[element: for element in iterable]
element → Es el elemento
for element in iterable → Ciclo donde se extraen elementos de cualquier iterable
'''

# Creating a list of numbers from 1 to 10.
numbers = []

for element in range(1, 11):
    numbers.append(element)
    
print(numbers)

# A list comprehension.
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

# Creating a list of names that contain the letter J.
# E X A M P L E

names = ['Juan','Mario', 'Joel', 'Luis',
         'Pedro', 'Jose']

new_names = []

for i in names:
    if 'J' in i:
        new_names.append(i)
        
print(new_names)

new = [i for i in names if 'J' in i]
print(new)

#=======================
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [i for i in numbers if i % 2 == 0]

print('v2 =>', even_numbers_v2)