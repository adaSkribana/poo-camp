#metodo constructor
#modificar atributo

class Email:
    def __init__(self): 
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True
#objeto asigno = la clase
mi_correo = Email()
print(mi_correo.enviado) # El valor inicial de mi objeto
mi_correo.enviar_correo() #Pasando mi objeto por la funcion de mi clase ..
print(mi_correo.enviado) #Nuevo valor de mi objeto