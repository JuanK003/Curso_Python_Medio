price = 100 # scope global

def increment():
    price = 200
    result = price + 10 # limited scope under the context of this function
    return(result)
    
print(price)
price_2 = increment()
print(price_2)