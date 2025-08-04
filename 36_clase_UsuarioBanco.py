"""36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
 Código a seguir:
 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante Implementar el método True y False .
 2. Implementar método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
 Caso de uso:
 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
 2. Agregar 20 unidades de saldo de "Bob".
 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
 4. Retirar 50 unidades de saldo a "Alicia"
 """

class UsuarioBanco:     #clase UsuarioBanco
    def __init__(self, nombre, saldo_inicial, tiene_cuenta_corriente= True):   # método espacial iniciación, crea objeto, usuario, dinero con el que empieza, si tiene cuenta. Guardamos valores
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.tiene_cuenta_corriente= bool(tiene_cuenta_corriente)

    def retirar_dinero(self, cantidad):     # método retirar dinero, condición si no tiene cuenta corriente y dinero suficiente se lanzan errores, si cumple, imprime mensaje
        if not self.tiene_cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente salodo para retirar {cantidad}")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}€. Saldo actual: {self.saldo}€")   

    def agregar_dinero(self, cantidad):    #Método agregar dinero, condiciones, no puede añadir 0 o -. Si cumple, imprime mensaje confirmación
        if cantidad <=0:
            raise ValueError("La cantidad a aumentar debe ser positiva")
        self.saldo += cantidad
        print(f"{self.nombre} ha recibido {cantidad}€. Saldo actual: {self.saldo}€")
              
    def transferir_dinero (self, otro_usuario, cantidad): #Método transferir dinero, condición ambos con cuenta, si no tiene dinero se lanza error, si por el contrario hace transferencia imprime mensaje operación exitosa y nuevo saldo
        if not self.tiene_cuenta_corriente or not otro_usuario.tiene_cuenta_corriente:
            raise ValueError("Ambos usuarios deben de tener cuenta corriente para transferir dinero")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para transferir {cantidad}")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
        print (f"{self.nombre} ha transferido {cantidad}€ a {otro_usuario.nombre}")
        print (f"Saldo actual de {self.nombre}: {self.saldo}€, Saldo actual de {otro_usuario.nombre}: {otro_usuario.saldo} €")


    
# Creo usuarios Alicia y Bob con los saldos
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# Agrego 20 unidades a Bob
bob.agregar_dinero(20)

# Bob transfiere 80 a Alicia
try:
    bob.transferir_dinero(alicia, 80)
except ValueError as error:
    print(f"Error en la transferencia: {error}")

# Alicia retira 50
alicia.retirar_dinero(50)
