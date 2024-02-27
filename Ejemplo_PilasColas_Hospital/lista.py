# Importacion de clases

from node import Nodo  # Importamos la clase Nodo de nodo.py

# Clase SingleLinkedList (lista simplemente enlazada)


class SingleLinkedList:  # Creamos la clase SingleLinkedList que permitirá crear listas simplemente enlazadas

    # Método init para inicializar el constructor de la clase SingleLinkedList
    def __init__(self):
        self.head = None
        self.size = 0

    # Método push para ingresar por cabeza un nodo

    def push(self, dato):  # Recibe el dato que se ingresará en un nodo
        if self.head is None:  # Si la lista está vacía, se ingresa el nodo en la cabeza de la lista
            self.head = Nodo(dato)
        else:  # Si no, se hace el siguiente proceso:
            newNode = Nodo(dato)  # Se guarda el nuevo nodo en la variable newNode
            newNode.next = self.head  # Hacemos que el nuevo nodo apunte a la "antigua" cabeza de la lista
            self.head = newNode  # Movemos el apuntador self.head al nuevo nodo (basicamente, será la nueva cabeza)
        self.size += 1  # Aumentamos el tamaño de la lista en 1 en ambos casos

    # Método encolar para ingresar por cola un nodo

    def encolar(self, dato):  # Recibe el dato que se ingresará en un nodo
        if self.head is None:  # Si la lista está vacía, se ingresa el nodo en la cabeza de la lista
            self.head = Nodo(dato)
        else:  # Si no, se hace el siguiente proceso:
            newNode = Nodo(dato)  # Se guarda el nuevo nodo en la variable newNode
            control = self.head  # Creamos la variable control para recorrer la lista empezando por la cabeza

            while control.next is not None:  # recorremos la lista hasta llegar al ultimo elemento (al que apunta a None)
                control = control.next  # Actualizamos la variable control con su siguiente en cada iteración

            control.next = newNode  # Hacemos que el apuntador del último nodo apunte al nuevo nodo
            # De esta forma, el nuevo nodo queda como el último

            # Nota: El proceso de recorrer la lista no es necesario si ya tenemos guardado el apuntador al último nodo
            # en ese caso solamente se tendría que hacer un proceso similar al del método push

        self.size += 1  # Aumentamos el tamaño de la lista en 1 en ambos casos

    # Método Pop para sacar un nodo por cabeza

    def pop(self):  # No recibe parámetros
        if self.head is None:  # Si la lista está vacía, no retorna nada
            return None
        else:  # Si no, se hace el siguiente proceso:
            nodeOut = self.head  # Guardamos la cabeza en nodeOut
            self.head = self.head.next  # Movemos el apuntador de la cabeza a su siguiente
            self.size -= 1  # Restamos 1 al tamaño de la lista
            return nodeOut  # Retornamos la "antigua" cabeza

    # Método desencolar para sacar un nodo por cabeza
    def desencolar(self):  # Como hace lo mismo que pop, simplemente llamamos al método pop
        return self.pop()  # Retornamos lo que nos retorna pop

    # Método para imprimir la lista
    def printList(self):  # No recibe parámetros
        control = self.head  # Creamos una variable de control para recorrer la lista, empezando por la cabeza
        while control: # Mientras control no sea None, imprimimos el nodo (se imprime lo que retorna el __str__ de la clase Nodo)
            print(control)
            control = control.next  # Actualizamos la variable control para que sea su siguiente en cada nueva iteración
