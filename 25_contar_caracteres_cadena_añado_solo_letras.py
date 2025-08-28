# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_carácteres (frase):
    return len(frase)          #cuenta todo, letras, espacios....


frase = "El verano es para descansar y cargar pilas"
total_carácteres = contar_carácteres (frase)


print( "Caracteres:",contar_carácteres(frase))


def contar_letras (frase):
    return sum(letra.isalpha() for letra in frase) #cuenta solo letras.

print("Solo letras:", contar_letras(frase))
