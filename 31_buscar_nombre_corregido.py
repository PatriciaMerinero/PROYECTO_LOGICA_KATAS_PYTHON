# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    
    entrada = input("Dime lista de nombres: ").strip()  #escribimos nombres
    if not entrada:
        print("La lista está vacía.")
        return False

    lista_nombres = [n.strip().lower() for n in entrada.split(",") if n.strip()]

    
    nombre = input("¿Qué nombre estás buscando?: ").strip().lower()
    if not nombre:
        print("No escribiste un nombre a buscar.")
        return False

    
    if nombre in lista_nombres:
        print(f"El nombre '{nombre}' fue encontrado en la lista.")
        return True
    else:
        print(f"El nombre '{nombre}' no está en la lista.")
        return False

buscar_nombre()