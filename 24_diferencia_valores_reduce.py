# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce #importo reduce

valores =[500, 20, 85, 1200, 300, -5000.25]

diferencia_total = reduce (lambda acumulado, siguiente: acumulado - siguiente, valores) #restamos cada valor acumulativamente (el orden importa)

print( diferencia_total)


