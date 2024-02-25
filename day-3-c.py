#Herencia
"""
class nombresubclase:(nombreclasesuperior):

class ClaseBase:
    Cuerpo de la clase base

class Derivadoclase(clasebase):
    Cuerppo clase derivada    
        """

class Pokemon:
    def __init__(self, nombre ,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def description(self):
        return "{} es un pokemon tipo: {}".format(self.nombre, self.tipo)
    
class Pikachu(Pokemon):
    def attack(self, attack):
     return "{} tipo ataque: {}".format(self.nombre, attack)

class Charmander(Pokemon):
    def attack(self, attack):
     return "{} tipo ataque: {}".format(self.nombre, attack)

nuevo_pokemon = Pikachu("boby", "electrico")
print(nuevo_pokemon.description()) # siempre para llamar una funcion debes finalizar con ()
print(nuevo_pokemon.attack("Rayo-attack")) # esta funcion requiere un argumento para atribuir a nuestro objeto

