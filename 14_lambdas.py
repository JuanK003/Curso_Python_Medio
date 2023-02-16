def increment(x):
    """
    Increment takes in a number and returns that number plus one.
    
    :param x: The variable that will be incremented
    :return: the value of x + 1.
    """
    return x + 1

# Creating a function that takes in a variable x and returns x + 1.
increment_v2 = lambda x : x + 1

result = increment(11)
print(result)

result = increment_v2(20)
print(result)

#============================================
# Creating a function that takes in two variables and returns a string with the two variables.
full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'

text = full_name('juan carlos', 'palacios escobar')
print(text)