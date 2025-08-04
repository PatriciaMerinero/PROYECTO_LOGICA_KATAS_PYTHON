#19. Crea una función lambda que filtre los número impares de una lista dada


numeros= [1, 20, 5, 27, 12, 3, 43, 47, 83]
numeros_impares= list(filter(lambda numero: numero % 2 != 0, numeros)) # filter y lambda para quedarnos con los impares, si el numero no es divisible /2= impar, recorre cada numero de la lista y aplica condición, convierte en lista.
print(numeros_impares)

