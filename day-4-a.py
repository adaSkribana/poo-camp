#herencia en unejemplo practico

class Calculadora:
    def __init__(self, numero):
        self.n= numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("Ingrese datos" +str(i+1)+"=")) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)


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

ejemplo= Op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.Suma())

ejemplo1 = Raiz()
print(ejemplo1.cuadrada())