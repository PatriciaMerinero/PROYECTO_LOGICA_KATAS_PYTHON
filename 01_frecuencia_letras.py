#Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionariocon las frecuencias de cada letra en la cadena. Los espacios no deben de ser considerados.



def contar_frecuencias_letras(texto):
    frecuencias = {} # Diccionario vacío
    for letra in texto:  
        if letra != " ":    #no cuenta los espacios como letra
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias


cadena_de_texto = "Buenos días por la mañana"
diccionario = contar_frecuencias_letras(cadena_de_texto)
print(diccionario)






