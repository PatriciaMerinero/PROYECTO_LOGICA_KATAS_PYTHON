#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

def enmascarar (valor):
    texto= str(valor) # convertimos en string
    longitud= len(texto)

    if longitud <=4:
        return texto # si tiene 4 o menos caracteres, no enmascara
    
    oculto= "#" * (longitud-4) #repite #
    visible= texto [-4:] #toma los ultimos 4 por la derecha

    return oculto + visible

variable = 258446641145  #+ de 4
resultado = enmascarar(variable)


print(resultado)


variable = 2584 # con 4
resultado = enmascarar(variable)


print(resultado)