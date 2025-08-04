#15. Crea una función lambda que  sume 3 a cada número de una lista dada.



lista_números =[3, 27, 12, 43, 47, 82]

resultado = list(map(lambda número: número + 3, lista_números ))

print (resultado)