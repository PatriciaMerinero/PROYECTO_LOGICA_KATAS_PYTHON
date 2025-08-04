# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

lista_palabras = ["mar", "sol", "verano", "tinto", "descanso", "vacaciones", "proyectos", "sueños"]



palabra_objetivo = "os"

def palabras_que_contengan_palabra_objetivo (lista_palabras, palabra_objetivo):
    resultado= list(filter(lambda palabra: palabra_objetivo in palabra, lista_palabras))
    return resultado

resultado=palabras_que_contengan_palabra_objetivo(lista_palabras, palabra_objetivo)
print (resultado)
