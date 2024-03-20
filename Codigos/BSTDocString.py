class Node:
    """
    Representa un nodo en un árbol binario de búsqueda.

    Atributos:
        value: El valor almacenado en el nodo.
        left (Node): Referencia al hijo izquierdo del nodo.
        right (Node): Referencia al hijo derecho del nodo.
        parent (Node): Referencia al nodo padre.
        is_root (bool): Indica si el nodo es la raíz del árbol.
        is_left (bool): Indica si el nodo es un hijo izquierdo.
        is_right (bool): Indica si el nodo es un hijo derecho.
    """

    def __init__(self, value=None, parent=None, is_root=False, is_left=False, is_right=False):
        """Inicializa el nodo con los valores dados."""
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.is_root = is_root
        self.is_left = is_left
        self.is_right = is_right

class BST:
    """
    Representa un árbol binario de búsqueda.

    Métodos públicos:
        append: Añade un nuevo valor al árbol.
        empty: Comprueba si el árbol está vacío.
        traverse_inorder: Recorre el árbol en in-order.
        traverse_preorder: Recorre el árbol en pre-order.
        traverse_posorder: Recorre el árbol en post-order.
        search: Busca un valor en el árbol.
    """

    def __init__(self):
        """Inicializa el árbol binario de búsqueda con una raíz nula."""
        self.root = None

    def empty(self):
        """Retorna True si el árbol está vacío, False de lo contrario."""
        return self.root is None

    def __place(self, value):
        """
        Encuentra la posición adecuada en el árbol para insertar un nuevo valor.

        Args:
            value: El valor a insertar.

        Returns:
            El nodo bajo el cual se debe insertar el nuevo valor.
        """
        aux = self.root
        while aux is not None:
            temp = aux
            if value <= aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp

    def append(self, value):
        """
        Inserta un valor en el árbol.

        Args:
            value: El valor a insertar.
        """
        if self.empty():
            self.root = Node(value=value, is_root=True)
        else:
            node = self.__place(value)
            if value <= node.value:
                node.left = Node(value=value, parent=node, is_left=True)
            else:
                node.right = Node(value=value, parent=node, is_right=True)

    def traverse_inorder(self, node):
        """
        Recorre el árbol en in-order (izquierda, raíz, derecha) e imprime los valores.

        Args:
            node: El nodo desde donde empezar el recorrido.
        """
        if node:
            self.traverse_inorder(node.left)
            print(node.value)
            self.traverse_inorder(node.right)

    def traverse_preorder(self, node):
        """
        Recorre el árbol en pre-order (raíz, izquierda, derecha) e imprime los valores.

        Args:
            node: El nodo desde donde empezar el recorrido.
        """
        if node:
            print(node.value)
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_posorder(self, node):
        """
        Recorre el árbol en post-order (izquierda, derecha, raíz) e imprime los valores.

        Args:
            node: El nodo desde donde empezar el recorrido.
        """
        if node:
            self.traverse_posorder(node.left)
            self.traverse_posorder(node.right)
            print(node.value)

    def search(self, node, value):
        """
        Busca un valor en el árbol.

        Args:
            node: El nodo desde donde empezar la búsqueda.
            value: El valor a buscar.

        Returns:
            El nodo que contiene el valor, o None si el valor no está en el árbol.
        """
        if node is None:
            return None
        else:
            if node.value == value:
                return node
            elif value <= node.value:
                return self.search(node.left, value)
            else:
                return self.search(node.right, value)


if __name__ == "__main__":
    def menu():
        """
        Menú interactivo para el manejo del árbol binario de búsqueda.

        Permite al usuario elegir entre agregar datos, verificar si el árbol está vacío,
        realizar recorridos (in-order, post-order, pre-order) y buscar un valor específico en el árbol.
        """
        bst = BST()

        try:
            while True:
                print("\nElementos\n"
                      + "\n\t1. Agregar Datos "
                      + "\n\t2. ¿Está vacío el árbol? "
                      + "\n\t3. Recorrer en orden "
                      + "\n\t4. Recorrer en post-orden "
                      + "\n\t5. Recorrer en pre-orden "
                      + "\n\t6. Buscar "
                      + "\n\t7. Salir ")

                opt = int(input("Ingrese su opción: "))

                if opt == 1:
                    data = int(input("Ingrese el dato a anexar al árbol: "))
                    bst.append(data)
                elif opt == 2:
                    print("Sí" if bst.empty() else "No")
                elif opt == 3:
                    bst.traverse_inorder(bst.root)
                elif opt == 4:
                    bst.traverse_posorder(bst.root)
                elif opt == 5:
                    bst.traverse_preorder(bst.root)
                elif opt == 6:
                    data = int(input("Ingrese el dato a buscar en el árbol: "))
                    result = bst.search(bst.root, data)
                    print(result if result else "Dato no encontrado")
                elif opt == 7:
                    print("Tchau!")
                    break
                else:
                    print("Ingresaste una opción errónea")

        except Exception as e:
            print("\n Solo se permiten caracteres numéricos")
            print(e)

    menu() 
