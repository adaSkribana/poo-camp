class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        """
        Método __len__():
        - Devuelve la longitud de la lista cuando se llama a la función incorporada len() sobre el objeto.
        """
        return len(self.elementos)

    def __getitem__(self, index):
        """
        Método __getitem__():
        - Permite acceder a los elementos del objeto mediante indexación.
        - Se llama automáticamente cuando se accede a un elemento del objeto utilizando la notación de corchetes [].
        """
        return self.elementos[index]

# Crear una instancia de la clase MiLista
mi_lista = MiLista([1, 2, 3, 4, 5])

# Obtener la longitud de la lista personalizada utilizando len()
print(len(mi_lista))  # Salida: 5

# Acceder a los elementos de la lista personalizada mediante indexación
print(mi_lista[0])  # Salida: 1 es decir el elemento de mi listo en posicion 0
print(mi_lista[2])  # Salida: 3 es decir el elemento de mi lista en posicion 2 
"""
entonces:
Al llamar el metodo getitem dentro de la clase luego permite que mediante un print y corchetes al final de mi objeto
pueda acceder al elemento de la posicion señalada
"""
