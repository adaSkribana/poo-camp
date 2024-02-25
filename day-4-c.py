class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        """
        Método __repr__():
        - Devuelve una representación formal de cadena de texto del objeto.
        - Se utiliza principalmente para representar el objeto de forma precisa para fines de depuración y desarrollo.
        """
        return f"Persona({self.nombre}, {self.edad})"

    def __str__(self):
        """
        Método __str__():
        - Devuelve una representación legible de cadena de texto del objeto.
        - Se utiliza para representar el objeto de una manera más amigable y legible.
        """
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)

# Imprimir la representación formal del objeto utilizando __repr__()
print(repr(persona))  # Salida: Persona(Juan, 30)

# Imprimir la representación legible del objeto utilizando __str__()
print(str(persona))   # Salida: Nombre: Juan, Edad: 30
