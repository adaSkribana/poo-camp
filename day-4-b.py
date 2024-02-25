""" super() es una función incorporada en Python que se utiliza para llamar métodos y atributos de la clase base (superclase) desde una subclase. 
Se utiliza principalmente en la herencia de clases cuando necesitas llamar al constructor de la clase base o a métodos definidos en la clase base."""

class Persona:
    def __init__(self, nombre, profesion, fecha_nacimiento):
        self.nombre = nombre
        self.profesion = profesion
        self.fecha_nacimiento = fecha_nacimiento

class Presentacion(Persona):
    def __init__(self, nombre, profesion, fecha_nacimiento):
        super().__init__(nombre, profesion, fecha_nacimiento)

    def presentacion(self):
        print("{} nació el {} y es {}.".format(self.nombre, self.fecha_nacimiento, self.profesion))

class Mensaje(Persona):
    def __init__(self, nombre, profesion, fecha_nacimiento):
        super().__init__(nombre, profesion, fecha_nacimiento)

    def dice(self, mensaje):
        print("{} dice: {}".format(self.nombre, mensaje))

# Pedir al usuario que ingrese los datos
nombre = input("Ingrese el nombre: ")
profesion = input("Ingrese la profesión: ")
fecha_nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")

# Crear instancias de las clases Presentacion y Mensaje
persona_presentacion = Presentacion(nombre, profesion, fecha_nacimiento)
persona_mensaje = Mensaje(nombre, profesion, fecha_nacimiento)

# Mostrar presentación
persona_presentacion.presentacion()

# Pedir al usuario que ingrese un mensaje y mostrarlo
mensaje = input("Ingrese un mensaje: ")
persona_mensaje.dice(mensaje)
