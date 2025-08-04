# 16.  Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()


def palabras_mas_largas (texto, n):
    palabras = texto.split()
    resultado=list(filter(lambda palabra:len(palabra) >n, palabras))
    return resultado


frase = "El saber no ocupa lugar"
n= 4

resultado = palabras_mas_largas (frase, n)
print (resultado)

