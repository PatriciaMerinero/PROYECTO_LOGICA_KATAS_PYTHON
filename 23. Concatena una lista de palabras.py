# 23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce  #Importo reduce

palabras = [ "Verano", "caluroso", "practicando", "Python"]

frase_concatenada = reduce(lambda acumulado, siguiente :  acumulado + " " + siguiente, palabras)   # une palabra por palabra agrgando un espacio, va acumulando la frase


print(frase_concatenada)
