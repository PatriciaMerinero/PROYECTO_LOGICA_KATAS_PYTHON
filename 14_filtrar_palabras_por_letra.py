# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()



def filtrar_por_letra (lista_palabras, letra):
    letra=letra.lower() #convierte en minúsculas
    resultado = list(filter(lambda palabra: palabra[0].lower()==letra, lista_palabras)) #convertimos en lista, accedemos a la primera letra de las palabras, convierte en minúscula y compara con v
    return resultado

palabras= [ "Sol", "Vacaciones", "Calor", "Playa", "Verde", "Libertad" ]
letra_especifica = "v"

resultado= filtrar_por_letra (palabras, letra_especifica)
print(resultado)
