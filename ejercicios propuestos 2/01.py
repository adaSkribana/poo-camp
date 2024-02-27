class Perros():
    def __init__(self, nombre):
        self._nombre = nombre  # Se inicializa el atributo protegido _nombre

    # Getter para obtener el nombre del perro
    @property
    def nombre(self):
        return self._nombre

    # Setter para modificar el nombre del perro
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

# Crear un objeto perro1 de la clase Perros
#objeto = clase("atributo")
perro1 = Perros("pukki")

# Acceder al nombre del perro usando el getter
print(f"Nombre original: {perro1.nombre}")  # Salida: pukki

# Modificar el nombre del perro usando el setter
perro1.nombre = "pascall"

# Acceder al nombre del perro modificado
print(f"Nombre modificado: {perro1.nombre}")  # Salida: nuevo_nombre


"""
En Python, la convención de nombres con un guion bajo al principio (_nombre) indica que un atributo es "protegido", evitando su modificación directa. 
El acceso controlado a través de métodos getter y setter proporciona una forma de leer y escribir valores de manera controlada, promoviendo la encapsulación al ocultar los detalles internos de implementación de la clase Perros. 
La encapsulación, un principio de la programación orientada a objetos, implica ocultar los detalles internos de un objeto y solo exponer una interfaz para interactuar con él, facilitando el manejo y la protección de los datos. 
Estos principios, aunque Python no tiene atributos completamente privados, simulan la privacidad y fomentan la encapsulación en la programación orientada a objetos
"""