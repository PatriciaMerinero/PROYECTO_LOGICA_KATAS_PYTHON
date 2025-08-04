# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos [572]. Usa la función reduce()



from functools import reduce #importo función reduce desde el módulo functools. Función acumulativa de izquiera a derecha

def convertir_a_número (digitos):
    cadena_números= reduce(lambda acumulado, número: acumulado + str(número), digitos, "") # recorre la lista de dígitos y va acumulando 
    return int(cadena_números)


print (convertir_a_número([5, 7, 2]))