# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.


def determinar_noche_o_dia (hora):     #Definimos función con parámetro hora
    if 6 <= hora < 12:                             #si la hora esta entre 6 (inclusive) y 12 (exclusivo), es por la mañana
        return "es de día, por la mañana"
    elif 12 <= hora <20:                          # si la hora esta entre 12 y 20 (exclusivo), es por la tarde
        return "es por la tarde"
    elif (20 <= hora <= 23) or (0 <= hora<6):   #si la hora esta entre 20 y 23 (inclusive) o entre 0 y 5 (inclusive), es de noche
        return "es de noche"
    else:
        return "La hora no es válida, debe de ser entre 0 y 23h" # si la hora no esta entre 0 y 23 devuelve mensaje de error
    
try:                                                                                   #puede fallar el código
    entrada= input ("Introduce la hora, de 0 a 23h: ")        #pedimos hora
    hora= int(entrada)                                                          #convertimos en entero
    print (determinar_noche_o_dia(hora))


except ValueError:                                                                #Si la hora que pedimos no es válida salta a except y da mensaje de error
    print("Introduce una hora válida entre 0 y 23h") 