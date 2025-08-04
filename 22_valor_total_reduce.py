#22. Dada una lista numerica, obten el producto total de los valores de dicha lista. usa la funcion reduce()

from functools import reduce #importamos reduce

numeros=[ 25, 27, 13, 12, 58, 90, 25.5]
producto_total = reduce(lambda acumulado, siguiente: acumulado * siguiente, numeros) #reduce con lambda que multiplica dos valores

print("total:", producto_total)




