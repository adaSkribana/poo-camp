class CuentaBancaria():
    def __init__(self, numero_cuenta, titular, saldo):
        # Atributos que definen características de la clase:
        self._numero_cuenta = numero_cuenta  # Número de cuenta bancaria
        self._titular = titular              # Nombre del titular de la cuenta
        self._saldo = saldo                  # Saldo actual de la cuenta
    
    def depositar(self, cantidad):
        # Método que define el comportamiento de la clase al depositar dinero:
        self._saldo += cantidad  # Incrementa el saldo con la cantidad depositada
    
    def retirar(self, cantidad):
        # Método que define el comportamiento de la clase al retirar dinero:
        if cantidad <= self._saldo:
            self._saldo -= cantidad  # Reduce el saldo si hay fondos suficientes
        else:
            print("No hay suficiente fondos disponibles.")  # Mensaje si no hay suficientes fondos
    
    def mostrar_saldo(self):
        # Método que define el comportamiento de la clase al mostrar el saldo:
        return self._saldo  # Devuelve el saldo actual de la cuenta
    
    def __str__(self):
        # Método especial que define la representación en cadena de la clase:
        return (f"Número de cuenta: {self._numero_cuenta}, Titular: {self._titular}, Saldo: {self._saldo}")

# Creación de instancias de la clase CuentaBancaria:
cuenta1 = CuentaBancaria("123456789", "juan perez", 1000)
cuenta2 = CuentaBancaria("987654321", "maria Lopez", 500)

# Impresión de la información de las cuentas antes y después de operaciones:
print (cuenta1)  # Muestra la información de la cuenta1
cuenta1.depositar(500)  # Deposita 500 en cuenta1
print(cuenta1)  # Muestra la información actualizada de cuenta1
print (cuenta2)  # Muestra la información de la cuenta2
cuenta2.retirar(500)  # Retira 500 de cuenta2
print(cuenta2)  # Muestra la información actualizada de cuenta2
