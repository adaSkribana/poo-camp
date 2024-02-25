#herencia en unejemplo practico

class Calculadora:
    def __init__(self, numero):
        self.n= numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("Ingrese datos" +str(i+1)+"=")) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2) #Aca se establece el maximo


    def Suma(self):
       a,b = self.datos 
       s = a+b
       print("El resultado es: ", s)
       
    def Resta(self):
       a,b = self.datos 
       r = a-b
       print("El resultado es: ", r)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
    def cuadrada(self):
        import math
        a, = self.datos
        print("es resultado es: ",math.sqrt(a))
"""
ejemplo= Op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.Suma())

ejemplo1 = Raiz()
print(ejemplo1.cuadrada())"""

objeto = Op_basicas
print(isinstance(objeto, Op_basicas))

"""
isinstance() es una función incorporada en Python que se utiliza para verificar si un objeto es 
una instancia de una clase o de cualquier clase que herede de esa clase. 
Su sintaxis es la siguiente:

isinstance(objeto, clase)
Donde:

objeto: El objeto que se desea verificar.
clase: La clase o tipo de datos que se desea verificar si el objeto es una instancia de ella.
La función isinstance() devuelve True si el objeto es una instancia de la clase especificada 
o de cualquier clase que herede de esa clase, 
y False en caso contrario.


"""