class MiIterador:
    def __init__(self, datos):
        """
        Constructor de la clase Mi_iterador.
        
        Args:
            datos (list): Lista de datos sobre la cual se iterará.
        """
        self.datos = datos  # Almacena la lista de datos
        self.indice = 0  # Inicializa el índice en 0 al principio

    def __iter__(self):
        """
        Método especial __iter__.
        
        Returns:
            self: Devuelve una referencia al propio objeto, lo que permite que el objeto sea iterable.
        """
        return self

    def __next__(self):
        """
        Método especial __next__.
        
        Returns:
            resultado: Devuelve el siguiente elemento en la secuencia de datos.
        
        Raises:
            StopIteration: Lanza una excepción cuando el iterador ha llegado al final de la secuencia.
        """
        if self.indice < len(self.datos):  # Si el índice es menor que la longitud de los datos
            resultado = self.datos[self.indice]  # Obtiene el elemento en la posición actual del índice
            self.indice += 1  # Incrementa el índice para apuntar al siguiente elemento
            return resultado  # Devuelve el elemento obtenido
        else:
            raise StopIteration  # Lanza una excepción indicando que el iterador ha llegado al final de la secuencia

# Crear una instancia de la clase Mi_iterador con una lista de datos
iterador = MiIterador([1, 2, 3, 4, 5])

# Utilizar el objeto mi_iterador en un bucle for para iterar sobre los elementos
for elemento in iterador:
    print(elemento)  # Imprime cada elemento obtenido del iterador

"""Comment
Una clase en sí misma no crea objetos iterables. 
Sin embargo, puedes hacer que los objetos de una clase sean iterables implementando el método __iter__() en la clase. 
Este método permite que los objetos de la clase sean utilizados en un bucle for u otras expresiones de iteración.
el método __iter__() se utiliza para hacer que los objetos de una clase sean iterables,
mientras que el método __next__() se utiliza para obtener el siguiente elemento en la secuencia cuando se utiliza un iterador sobre esos objetos. 
El método __next__() no se puede utilizar sin la implementación previa del método __iter__().
fin comment
"""