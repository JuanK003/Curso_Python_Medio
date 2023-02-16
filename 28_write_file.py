'''
# Opening the file in read and write mode.
with open('./text.txt', 'r+') as file:
    # Printing the content of the file.
    for i in file:
        print(i)
        
    # Adding a new line to the file.
    file.write('\nsoy franchesco')
    file.write('\nnuevo')
    file.write('\nSIIUUU')
'''

# Opening the file in write mode and assigning it to the variable file.
with open('./text.txt', 'w+') as file:
    # Printing the content of the file.
    for i in file:
        print(i)
        
    # Adding a new line to the file.
    file.write('soy franchesco')
    file.write('\nnuevo')
    file.write('\nSIIUUU')