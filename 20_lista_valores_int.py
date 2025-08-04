# 20. Crea una lista con elementos tipo integer y string obtén una nueva lista solo con los valores int. Usa la función filter()


elementos = ["Verano", 25, 58, 25.4, "Sol", "Tinto de Verano", "Playa"]
valores_enteros = list(filter(lambda valor: type(valor) == int, elementos)) #  recibe cada valor de la lista elementos, comprueba si es int, devuelve true o false, con filter solo deja los que cumplen int, convertimos en lista
print( valores_enteros)