#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.


#Primero defino listas antes de aplicar función lambda

lista1 = [1, 100, 2000, 30000, 4000000]
lista2 = [20, 40, 35.5, 25000, 47]

suma_listas= list(map(lambda elemento1, elemento2: elemento1+elemento2, lista1, lista2))     #lambda+ 2 elementos, map aplica lambda a cada par de elementos de ambas listas, convertimos en lista

print(suma_listas)


