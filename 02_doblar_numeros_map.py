#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

lista_numeros= [1,2,3,5,20,50,100]

lista_numero_dobles= list(map(lambda valor: valor* 2, lista_numeros))

print(lista_numero_dobles)
