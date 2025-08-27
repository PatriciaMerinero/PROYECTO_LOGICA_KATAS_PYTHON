





from functools import reduce #importo función reduce desde el módulo functools. Función acumulativa de izquiera a derecha

def convertir_a_numero(digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + int(digito), digitos, 0)   #toma lo acumulado, multiplicalo por 10 y + el digito actual


print(convertir_a_numero([5,7,2]))   
print(convertir_a_numero(['5','7','2']))  # dentro de la función int(dígito) en cada paso, cada string se convierte a entero
