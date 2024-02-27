
class Nodo:  # Creamos una clase nodo para guardar a la persona

    # Método init para inicializar el constructor de la clase Nodo
    def __init__(self, dato):   # En el método init recibimos a la persona (dato)
        self.dato = dato   # Guardamos a la persona en el atributo dato
        self.next = None  # Apuntador hacia None

    # Método str que retorna los datos que se mostrarán cuando se imprima un objeto de la clase Nodo
    def __str__(self):
        return self.dato.__str__()  # Al imprimir el nodo, nos imprime los datos de la persona
