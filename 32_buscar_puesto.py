#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto (nombre_completo, lista_empleados):   #definimos función
    nombre_completo= nombre_completo. strip(). lower() #strip eliminamos espacios al finalo y al principio del texto, lower convertimos en minusculas

    for nombre, puesto in lista_empleados:            #recorremos cada tupla de la lista (nombre, puesto)
        if nombre. strip(). lower()== nombre_completo: #comparamos
            return f" {nombre} trabaja como {puesto}" #si coincide devuelve nombre+ puesto
    return f" {nombre_completo. title()} no trabaja aqui " # si no coincide devuelve mensaje



empleados=[                                                            #lista con colección de tuplas
    ("Patricia Merinero", "Analista Fraude"),
    ("Gema Perez", "Directora Financiera"),
    ("Pedro Gómez", "CEO"),
    ("Jaime Serrano", "Analista Comite")
]



print(buscar_puesto("Patricia Merinero", empleados))
print (buscar_puesto("Ana Perez", empleados))
