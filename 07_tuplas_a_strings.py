# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def convertir_a_strings(lista_tuplas):
    return list(map(lambda tupla: " ".join(tupla), lista_tuplas)) # uno los elementos con espacio


tuplas = [("Me", "esta",  "costando"), ("la", "misma", "vida"), ("aprender", "Python")]
resultado = convertir_a_strings(tuplas)
print(resultado)


