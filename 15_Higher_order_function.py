def increment(x):
    """
    High_ord_func takes a function as an argument and returns a function.
    
    :param x: 2
    :return: 4
    """
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment)
print(result)

#===========================================

# Creating a lambda function that takes in a value and returns that value + 1.
increment_v2 = lambda x : x + 1

high_ord_func_v2 = lambda x, func: x + func(x)

result_v2 = high_ord_func_v2(2, increment_v2)
print(result_v2)

# The above code is using a lambda function to pass in a function as an argument to another function.
result_v3 = high_ord_func_v2(2, lambda x : x + 2)
result_v4 = high_ord_func_v2(2, lambda x : x * 5)

print(result_v3)
print(result_v4)