#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.


def anagramas (palabra1, palabra2):

    palabra1= palabra1. lower() #convierte en minusculas
    palabra2 = palabra2. lower()

    return sorted(palabra1) == sorted(palabra2) #convierte en lista ordenada y compara. 


palabra1="Patricia"
palabra2= "aparitci"

print(anagramas(palabra1,palabra2))


palabra1="Patricia"
palabra2= "Python"

print(anagramas(palabra1,palabra2))