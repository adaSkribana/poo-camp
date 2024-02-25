class Diccionario:
    def __init__(self):
        self._palabras_vocales = {}  # Diccionario para almacenar palabras que comienzan con vocales
        self._palabras_consonantes = {}  # Diccionario para almacenar palabras que comienzan con consonantes

    def almacenar_palabra(self, palabra, tipo):
        """Método para almacenar una palabra en el diccionario."""
        if tipo == 'vocal':
            self._palabras_vocales[palabra] = True
        elif tipo == 'consonante':
            self._palabras_consonantes[palabra] = True

    def ver_palabras(self):
        """Método para mostrar las palabras almacenadas."""
        print("Palabras almacenadas que comienzan con vocales:")
        # Imprime las palabras almacenadas que comienzan con vocales separadas por comas
        # El método join()...
        print(", ".join(self._palabras_vocales.keys()))

        print("\nPalabras almacenadas que comienzan con consonantes:")
        # Imprime las palabras almacenadas que comienzan con consonantes separadas por comas
        # El método join() se utiliza para concatenar elementos de una secuencia con un separador específico.
        # En este caso, self._palabras_consonantes.keys() devuelve una vista de todas las claves en el diccionario _palabras_consonantes.
        # Estas claves se unen utilizando ", " como separador para formar una sola cadena.
        # Luego, la cadena resultante se imprime utilizando la función print().
        print(", ".join(self._palabras_consonantes.keys()))

    def __setattr__(self, nombre_atributo, valor):      
        """
        Método para asignar dinámicamente atributos.
        Este método se llama cuando se intenta asignar un valor a un atributo del objeto.
        En este caso, se sobrescribe para permitir la asignación dinámica de palabras a los diccionarios _palabras_vocales y _palabras_consonantes.
        Si el nombre del atributo comienza con '_palabras_vocales' o '_palabras_consonantes', el método asigna el valor correspondiente al diccionario respectivo.
        Si el nombre del atributo no coincide con ninguno de estos, se genera un error.
        """
        if nombre_atributo.startswith('_palabras_vocales') or nombre_atributo.startswith('_palabras_consonantes'):
            super().__setattr__(nombre_atributo, valor)  # Utiliza super() para llamar al método __setattr__() de la clase base
        else:
            raise AttributeError("No se pueden agregar atributos adicionales.")  # Genera un error si se intenta agregar un atributo no permitido

    def __getattr__(self, nombre_atributo):
         
        """
        Método para acceder a atributos dinámicamente.
        Este método se llama cuando se intenta acceder a un atributo que no existe en el objeto.
        En este caso, se sobrescribe para permitir el acceso dinámico a los diccionarios _palabras_vocales y _palabras_consonantes.
        Si el nombre del atributo comienza con '_palabras_vocales', el método devuelve el diccionario _palabras_vocales.
        Si el nombre del atributo comienza con '_palabras_consonantes', el método devuelve el diccionario _palabras_consonantes.
        Si el nombre del atributo no coincide con ninguno de estos, se genera un error.
        """
        if nombre_atributo.startswith('_palabras_vocales'):
            return self._palabras_vocales  # Devuelve el diccionario _palabras_vocales
        elif nombre_atributo.startswith('_palabras_consonantes'):
            return self._palabras_consonantes  # Devuelve el diccionario _palabras_consonantes
        else:
            raise AttributeError("El atributo solicitado no existe.")  # Genera un error si se intenta acceder a un atributo inexistente

# Crear una instancia de la clase Diccionario
diccionario = Diccionario()

while True:
    try:
        print("\n--- Menú ---")
        print("1. Almacenar palabra")
        print("2. Ver palabras almacenadas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabra = input("Ingrese la palabra: ")
            tipo = input("¿Comienza con vocal o consonante? (vocal/consonante): ").lower()
            diccionario.almacenar_palabra(palabra, tipo)
            print("Palabra almacenada exitosamente.")

        elif opcion == '2':
            diccionario.ver_palabras()

        elif opcion == '3':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    except Exception as e:
        print(f"Se produjo un error: {e}")
