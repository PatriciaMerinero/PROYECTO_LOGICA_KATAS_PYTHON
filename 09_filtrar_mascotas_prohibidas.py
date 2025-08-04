# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()


# Usando lambda y filter

def filtrar_nombre_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))    #devuelve true solo para las mascotas permitidas. Deja fuera a las que están en la lista de mascotas prohibidas


mascotas = ["Urón", "Gato", "Iguana", "Loro", "Mapache", "Conejo", "Tigre", "Perro" ]
resultado = filtrar_nombre_mascotas(mascotas)
print(resultado)  
