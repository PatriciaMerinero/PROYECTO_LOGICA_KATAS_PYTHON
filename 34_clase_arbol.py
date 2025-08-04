""" 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
 Código a seguir:
 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
 Caso de uso:
 1. Crear un árbol.
 2. Hacer crecer el tronco del árbol una unidad.
 3. Añadir una nueva rama al árbol.
 4. Hacer crecer todas las ramas del árbol una unidad.
 5. Añadir dos nuevas ramas al árbol.
 6. Retirar la rama situada en la posición 2.
 7. Obtener información sobre el árbol """


class Arbol:    #creo clase árbol con tronco y ramas
    def __init__(self):    #inicio tronco con longitud 1 y  lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):   #aumenta longitu del tronco 1 unidad
        self.tronco +=1

    def nueva_rama(self):  #añade una rama con longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):    #aumenta longitud de las ramas 1 unidad
        self.ramas = [rama + 1 for rama in self.ramas] 
    
    def quitar_rama(self, posición):    # elimina la rama en una posición específica si existe, condición

        if 0<= posición < len(self.ramas):
            self.ramas.pop (posición)
        else:
            print(f"No existe rama en la posición {posición}")

    def info_arbol (self): # devuelva información del árbol
        return{
            "longitud_tronco": self.tronco,
            "número_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
    

arbol= Arbol()   #crea Árbol (tronco=1, ramas[])

arbol.crecer_tronco()  #el tronco ahora mide 2

arbol.nueva_rama()    #añadimos rama long=1

arbol.crecer_ramas()   #todas las ramas crecen 1

arbol.nueva_rama()   #añadimos rama
arbol.nueva_rama()   #añadimos otra rama

arbol.quitar_rama(2)    #quitamos la tercera rama(2)

info= arbol.info_arbol()
print("información del arbol:", info)



