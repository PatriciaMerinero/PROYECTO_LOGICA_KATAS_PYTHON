# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre () :
    try:  #manejamos errores si hay
        entrada = input ("Dime lista de nombres: ") #escribimos nombres
        lista_nombres = [nombre. strip(). lower() for nombre in entrada. split(",")]   #strip quita espacios al principio y final de cada nombre, split crea lista dividiento la cadena por comas, convertimos en minúsculas



        nombre= input("Que nombre estas buscando?: "). strip().lower() #pedimos nombre a buscar, strip quitamos espacios, convertimos en minúsculas


        if nombre in lista_nombres:   #condición

            print( f"El nombre '{nombre}' fue encontrado en la lista.")  # si esta en la lista lo muestra

        else:
            raise ValueError( f"El nombre '{nombre}' no está en la lista.") #si no esta, lanza error y activa except
    
    except ValueError as error: #si lanza error, muestra error
        print("Error: ", error)


buscar_nombre()


