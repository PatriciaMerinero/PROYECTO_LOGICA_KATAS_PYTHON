# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()



def diferencia_listas (lista1, lista2):
    return list(map(lambda x, y: x - y , lista1, lista2))


lista1 = [20, 50, 70, 83]
lista2= [25, 15, 80, 23]

resultado= diferencia_listas (lista1, lista2)
print (resultado)

