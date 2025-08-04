"""" 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , procesar_texto . contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función 
Código a seguir:
 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
 2. Crear una función reemplazar_palabras para remplazar una que devolver el texto con el remplazo de palabras.
 3. Crear una función palabra_original del texto por una palabra_nueva . Tiene eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
 Caso de uso:
 Comprueba el funcionamiento completo de la función procesar_texto"""


# Función contar_palabras

def contar_palabras(texto):
    palabras= texto.lower().split()  #convertimos a minúsculas, divido texto en palabras. Diccionario para contar cuantas veces aparece cada palabra
    conteo = {}
    for palabra in palabras:
        conteo [palabra] = conteo.get(palabra, 0) +1
    return conteo
    
# Función reemplazar palabras

def reemplazar_palabras(texto, palabra_original, palabra_nueva):  #Defino función
    return texto.replace (palabra_original, palabra_nueva)  #replace busca apariciones de la palabra original y las reemplaza

# Función eliminar_palabra

def eliminar_palabra(texto, palabra_a_eliminar):     #defino función
    palabras= texto.split()    #divide texto en lista de palabras, separa por espacios
    resultado=[p for p in palabras if p != palabra_a_eliminar]  #lista por comprensión, solo incluye a aquellas que no son iguales a palabra_a_eliminar
    return ' ' . join(resultado) # une las palabras de la lista, con espacio = nueva cadena de texto sin la palabra eliminada

# Función de procesar_texto, segun lo que indiquemos 

def procesar_texto (texto, opción, *args):   #defino función, recibe: texto que se procesa, que operación voy a hacer y lista de argumentos extra
    if opción == "contar":                                 # Condición: si es contar, llama a función contar_palabras
        return contar_palabras(texto)
    elif opción == "reemplazar" and len(args) == 2:    #Condición: si es reemplazar y hay 2 argumentos extra en args, 0 palabra a buscar, 1 palabra nueva
        return reemplazar_palabras (texto, args [0], args[1])
    elif opción == "eliminar" and len (args) == 1: # Condición: si es eliminar y hay 1 argumento extra, pasa texto y la palabra a eliminar
        return eliminar_palabra(texto, args[0])
    else:                                                  #Si no se cumplen las condiciones anteriores devuelve Opción no válida
        return "Opción no válida"
    


texto = "El verano se me está haciendo eterno"



print (procesar_texto(texto, "contar"))

print (procesar_texto(texto, "reemplazar", "verano", "invierno"))

print (procesar_texto(texto, "eliminar", "me"))

