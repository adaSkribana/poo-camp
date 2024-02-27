class Persona():
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    @property
    def nombre(self):
        return self._nombre
    def edad(self):
        return self._edad
    def altura(self):
        return self._altura
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    def edad(self, nueva_edad):
        self._nombre = nueva_edad
    def altura(self, nueva_altura):
        self._nombre = nueva_altura


trabajador = Persona("Juan Perez", 30, 175)
print(f"Trabajador/a {trabajador.nombre} tiene {trabajador.edad} añor y mide {trabajador.altura} cm.")
