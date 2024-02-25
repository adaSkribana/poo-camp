#metodo constructor
class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return "{} tiene {}".format(self.nombre, self.año) #oredena el resultado le da coherencia 
    
    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)

doctor = Persona("jose", 26)
print(doctor.nombre, doctor.año)
print(doctor.descripcion)
print(doctor.comentario("Que wasaap"))