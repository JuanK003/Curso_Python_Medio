def message_creator(text):
   # Escribe tu solución 👇
   message = {'computadora': 'Con mi computadora puedo programar usando Python', 
              'celular': 'En mi celular puedo aprender usando la app de Platzi', 
              'cable': '¡Hay un cable en mi bota!'
            }
   
   if text in message.keys():
       return message[text]
   
   else:
       return 'Artículo no encontrado' 

text = str(input('Elige un artículo => ').lower())
response = message_creator(text)
print(response)