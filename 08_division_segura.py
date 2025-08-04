# 8.  Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.


'''manejo de errores: try ... except ... else :
intentamos ejecutar un bloque de código que podría lanzar una excepción. Si la excepción se produce se captura con un bloque except. En el bloque else, se coloca el código que se ejecutará si no se produce ninguna excepción en el bloque try. Sólo se ejecutará si no ejecuta ningún except antes.'''


try:                                                                                            #código que puede fallar
    num_1 = float(input("primer número"))                              #convierte el input en número decimal
    num_2 = float(input("segundo número"))      
    
    resultado = num_1 / num_2
except ValueError:                                                                   #recibe valor de tipo correcto pero con valor inapropiado        
    print("Error: Debes introducir valores numéricos.")
except ZeroDivisionError:                                                       #se intenta dividir un número por 0
    print("Error: No se puede dividir por cero.")
else:                                                                                        #se ejecuta si no se produce ninguna excepción en el bloque try. Sólo se ejecutará si no ejecuta ningún except antes.
    print(f"Correcto. El resultado es: {resultado}")                   #f sustituye la variable por su valor

