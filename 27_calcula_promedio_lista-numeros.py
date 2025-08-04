# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio (lista_numeros):
    if len(lista_numeros) == 0:
        return 0
    return sum(lista_numeros) / len(lista_numeros)





numeros= [25, 27, 13, 82, 5555.25, 5]
promedio= calcular_promedio(numeros)



print(promedio)