""" 41.  En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python."""
 

try:    #control por si error
    precio= float (input("Dime precio original del articulo (€): "))    #convertimos en decimal, pedimos precio
    tiene_cupon = input ("¿Tienes un cupon de descuento?  (si o no): "). strip(). lower()   #quitamos espacios principio y final y convertimos en minúsculas

    if tiene_cupon == "si":  
         descuento = float (input("Introduce el valor del cupon (€): "))
         if descuento > 0:
            precio_final = precio - descuento
            print(f" Se ha aplicado el descuento de {descuento}€")
         else:
                precio_final = precio
                print("El cupon no es valido, no se ha aplicado ningun descuento")
    else:
        precio_final = precio
        print("No se ha aplicado ningun descuento")
    
    print(f"El precio final de la compra es: {precio_final: .2f}€")       #mostramos sólo 2 decimales

except ValueError:
    print("Introduce un numero valido")      