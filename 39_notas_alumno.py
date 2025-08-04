"""39.  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
 1. 0 / 69 insuficiente
 2. 70 / 79 bien
 3. 80 / 89 muy bien
 4. 90 / 100 excelent"""


def calificación_alumno (nota) :   #defino función
    if 0 <=nota <= 69:  #condición
        return "insuficiente"
    elif 70 <= nota <= 79: #condición
        return "bien"
    elif 80 <= nota <= 89: #condición
        return "muy bien"
    elif 90 <= nota <= 100: #condición
        return "excelente"
    else:                                   #si no se cumple lo anterior da mensaje de error
        return "no has introducido bien la nota, no es válida"
    
try:
    entrada = input("Introduce la nota del alumno del 0 al 100: ")    #pide nota
    nota= int(entrada)
    print (calificación_alumno(nota))

except ValueError:                               #el dato introducido no es válido lanza error con mensaje
    print ("Tienes que introducir un número entero válido. Gracias")
    