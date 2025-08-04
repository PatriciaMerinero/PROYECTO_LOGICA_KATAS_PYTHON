#13.Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()



def letras_mayus_minus (letras):
    letras_unicas = set(letras) #convertimos en set que quita duplicados
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))    # Creamos una lista de tuplas con cada letra en (mayúscula, minúscula)
    return resultado


conjunto = "Confía en tu código!"
resultado = letras_mayus_minus(conjunto)
print(resultado)

