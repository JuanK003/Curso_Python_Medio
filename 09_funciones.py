def my_print():
    """
    `my_print()` is a function that prints the string 'This is my print'
    """
    print('This is my print')

my_print()

def new_print(text):
    """
    > The function `new_print` takes a string as an argument and prints it
    
    :param text: The text to be printed
    """
    print(text)
    
message = input('Introduce un texto ⇒ ')
new_print(message)

def suma(a, b):
# Asking for two numbers and then printing the sum of them
    print(a + b)
    
num = int(input('Introduce un número entero ⟹ '))
num2 = int(input('Introduce otro número entero ⟹ '))
suma(num, num2)