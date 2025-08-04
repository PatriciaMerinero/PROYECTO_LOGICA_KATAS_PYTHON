 #11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.


try:   #pueden introducir datos no válidos
    edad = int(input("Introduce tu edad: ")) #pide edad y convierte en nº entero

    if edad < 0 or edad > 120:  
        print("Edad fuera del rango permitido (0-120).")
    else:
        print(f"Edad introducida correcta: {edad} años")

except ValueError:   # si en try el dato no es válido
    print("Error: Debes introducir un dato válido.")
