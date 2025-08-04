# 40.  Escribe una función que tome dos parámetros: "triangulo" ) y figura (una cadena que puede ser "rectangulo" , "circulo" o datos (una tupla con los datos necesarios para calcular el área de la figura)

def calcular_area (figura, datos):   #defino función
    if figura == "triangulo":     #triangulo= 1/2*base*altura
        base, altura = datos
        return 0.5* base* altura
    elif figura == "rectangulo":    #rectangulo= base*altura
        base, altura = datos
        return base* altura
    elif figura =="circulo":      #circulo= pi *radio 2
        radio , = datos     # , espero solo un dato de la tupla
        pi = 3.14
        return pi * radio ** 2
    else:                                        #mensaje si figura no definida
        return "Figura no reconocida"
    

print(calcular_area("triangulo", (4, 6)))      
print(calcular_area("rectangulo", (5, 10)))   
print(calcular_area("circulo", (3,)))          
print(calcular_area("hexagono", (5,)))         


