#Herencia
"""
class nombresubclase:(nombreclasesuperior):

class ClaseBase:
    Cuerpo de la clase base

class Derivadoclase(clasebase):
    Cuerppo clase derivada    
        """

class Pokemon:
    pass
    def __init__(self, nombre ,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def description(self):
        return "{}es un pokemon tipo: {}".format(self.nombre, self.tipo)
    
class Pikachu(Pokemon):
    def attack(self, tipe_Attack):
     return "{} tipo ataque: {}".format(self.nombre, tipe_Attack)

class Charmander(Pokemon):
    def attack(self, tipe_Attack):
     return "{} tipo ataque: {}".format(self.nombre, tipe_Attack)

nuevo_pokemon = Pikachu("bby", "electrico")
print(nuevo_pokemon.tipe_attack)

#no corre revisar