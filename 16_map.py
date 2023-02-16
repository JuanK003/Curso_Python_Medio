# Su función principal es hacer transformaciones

# Creating a new list called numbers_v2 and appending the values of the numbers list multiplied by 2.
numbers = [1, 2, 3, 4, 5]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)
 
print(numbers)    
print(numbers_v2)

#===========================================

# Creating a new list called numbers_v3 and appending the values of the numbers list multiplied by 2.
numbers_v3 = list(map(lambda i : i * 2, numbers))
print('\n')
print(numbers)
print(numbers_v3)

#===========================================
# Adding the values of n1 and n2.
n1 = [1, 2, 3, 4]
n2 = [5, 6, 7, 8, 9]

result = list(map(lambda x, y : x + y, n1, n2))
print('\n')
print(n1)
print(n2)
print(result)