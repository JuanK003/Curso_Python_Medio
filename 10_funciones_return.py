# Adding all the numbers from 1 to 9.
suma = 0
for x in range(1,10):
    suma += x
print(suma)

def sum_with_range(min, max):
    """
    Sum_with_range takes two numbers, min and max, and prints the sum of all numbers from min to max.
    
    :param min: the minimum number to start the range
    :param max: the maximum number to sum up to
    """
    sum = 0
    for x in range(min, max):
        sum += x
    print(sum)

mini = int(input('Introduzca el primer rango: '))
maxi = int(input('Introduzca el segundo rango: '))
sum_with_range(mini, maxi)

#-----------------------------------------------------------------------------------------------------------

def sum_with_range_with_return(min, max):
  # The above code is summing all the numbers between the range of the two numbers that the user
  # inputs.
    print(min, max)
    sum = 0
    for i in range(min, max):
        sum += i
    return sum

mini = int(input('Introduzca el primer rango: '))
maxi = int(input('Introduzca el segundo rango: '))
result = sum_with_range_with_return(mini, maxi)
print(result)