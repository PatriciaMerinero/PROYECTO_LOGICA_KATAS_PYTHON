# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.





def calcular_promedio(lista_numeros):  # función
    if not lista_numeros:
        return None        #si lista_numero esta vacía = none
    return sum(lista_numeros) / len(lista_numeros)   #suma valores/ cuenta elementos



lista_numeros = [1, 5, 85, 258, 5.45]  #lista de numeros con datos

resultado = calcular_promedio(lista_numeros)

if resultado is None:
    print("No se puede calcular el promedio de una lista vacía.")
else:
    print(f"El promedio es: {resultado}")




lista_numeros = [] #lista de números vacía

resultado = calcular_promedio(lista_numeros)

if resultado is None:
    print("No se puede calcular el promedio de una lista vacía.")
else:
    print(f"El promedio es: {resultado}")