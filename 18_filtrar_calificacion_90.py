
# 18. Escibe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90


#lista de diccionarios información estudiantes

estudiantes = [
    {"nombre": "Esther", "edad": 47, "calificación": 95 },
    {"nombre": "Bárbara", "edad": 35, "calificación": 80},
    {"nombre": "Alexandra", "edad": 32, "calificación": 75},
    {"nombre": "Cristóbal", "edad": 42, "calificación": 93},
    {"nombre": "Alberto", "edad": 43, "calificación": 40}
]

def mejor_nota (estudiante):     #determina si un estudiante tiene nota >= 90
    return estudiante ["calificación"] >= 90


mejores_estudiantes = list(filter(mejor_nota, estudiantes))   #obtenemos estudiantes detacados

print("alumnos con calificación mayor o igual a 90:")
for estudiante in mejores_estudiantes:
    print(estudiante)