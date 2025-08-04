# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitudes_palabras(frase):
    palabras = frase.split()  # Divide la frase en palabras usando los espacios, método split, separa el texto cada vez que encuentra un espacio en blanco
    return list(map(len, palabras))  # Aplica len() a cada palabra, convertimos en lista


frase = "Cada día es un nuevo input(), tú decides el output"
resultado = longitudes_palabras(frase)
print(resultado)