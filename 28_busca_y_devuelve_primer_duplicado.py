# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado (lista):
    vistos =set()   #registramos elementos ya vistos
    for elemento in lista :
        if elemento in vistos:
            return elemento # si ya esta visto es el primer duplicado
        vistos.add(elemento)
    return None # si no hay duplicado =none



numeros= [25, 58, 62, 5555.58, 4, 5, 25]
duplicado = primer_duplicado(numeros)

print(duplicado)

