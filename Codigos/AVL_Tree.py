class Node:
    def __init__(self, label, parent=None):
        self.label = label
        self._parent = parent
        self._left = None
        self._right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        if not self.root:
            self.root = Node(label)
        else:
            self._insert(label, self.root)

    def _insert(self, label, current_node):
        if label < current_node.label:
            if current_node._left:
                self._insert(label, current_node._left)
            else:
                current_node._left = Node(label, current_node)
                self._inspect_insertion(current_node._left)
        elif label > current_node.label:
            if current_node._right:
                self._insert(label, current_node._right)
            else:
                current_node._right = Node(label, current_node)
                self._inspect_insertion(current_node._right)
        else:
            print("Value already in tree!")

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node._parent is None: return
        path = [cur_node] + path

        left_height = self.get_height(cur_node._parent._left)
        right_height = self.get_height(cur_node._parent._right)

        if abs(left_height - right_height) > 1:
            path = [cur_node._parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height 
        if new_height > cur_node._parent.height:
            cur_node._parent.height = new_height

        self._inspect_insertion(cur_node._parent, path)

    def _rebalance_node(self, z, y, x):
        if y == z._left and x == y._left:
            self._rotate_right(z)
        elif y == z._left and x == y._right:
            self._rotate_left(y)
            self._rotate_right(z)
        elif y == z._right and x == y._right:
            self._rotate_left(z)
        elif y == z._right and x == y._left:
            self._rotate_right(y)
            self._rotate_left(z)
        else:
            raise Exception('_rebalance_node: z, y, x node configuration not recognized!')

    def _rotate_left(self, z):
        sub_root = z._parent
        y = z._right
        t2 = y._left
        y._left = z
        z._parent = y
        z._right = t2
        if t2 != None: t2._parent = z
        y._parent = sub_root
        if y._parent == None:
                self.root = y
        else:
            if y._parent._left == z:
                y._parent._left = y
            else:
                y._parent._right = y
        z.height = 1 + max(self.get_height(z._left),
            self.get_height(z._right))
        y.height = 1 + max(self.get_height(y._left),
            self.get_height(y._right))

    def _rotate_right(self, y):
        sub_root = y._parent
        z = y._left
        t3 = z._right
        z._right = y
        y._parent = z
        y._left = t3
        if t3 != None: t3._parent = y
        z._parent = sub_root
        if z._parent == None: 
            self.root = z
        else:
            if z._parent._left == y:
                z._parent._left = z
            else:
                z._parent._right = z
        y.height = 1 + max(self.get_height(y._left),
            self.get_height(y._right))
        z.height = 1 + max(self.get_height(z._left),
            self.get_height(z._right))

    def get_height(self, cur_node):
        if cur_node is None: return 0
        return cur_node.height

    def get_root(self):
        return self.root.label

    def inorder_traversal(self, start, traversal):
        """Inorder traversal of our tree."""
        if start:
            traversal = self.inorder_traversal(start._left, traversal)
            traversal += (str(start.label) + '-')
            traversal = self.inorder_traversal(start._right, traversal)
        return traversal
    
    def preorder_traversal(self, start, traversal):
        """Preorder traversal of our tree."""
        if start:
            traversal += (str(start.label) + '-')
            traversal = self.preorder_traversal(start._left, traversal)
            traversal = self.preorder_traversal(start._right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        """Postorder traversal of our tree."""
        if start:
            traversal = self.postorder_traversal(start._left, traversal)
            traversal = self.postorder_traversal(start._right, traversal)
            traversal += (str(start.label) + '-')
        return traversal

if __name__ == "__main__":
    # Menu of options
    def menu():
        avl = AVLTree()
        while True:
            print("\nAVL Tree\n"
                  + "\n\t1. Is the tree empty? "
                  + "\n\t2. Add Nodes "
                  + "\n\t3. Inorder Traversal "
                  + "\n\t4. Get Root "
                  + "\n\t5. Exit")
            opc = int(input("\nChoose an option: "))
            if opc == 1:
                if avl.root is None:
                    print("The tree is empty.")
                else:
                    print("The tree is not empty.")
            elif opc == 2:
                node = int(input("\nEnter the node value: "))
                avl.insert(node)
            elif opc == 3:
                print("Inorder Traversal: ", avl.inorder_traversal(avl.root, ""))
            elif opc == 4:
                if avl.root is None:
                    print("The tree is empty.")
                else:
                    print("Root of the tree: ", avl.get_root())
            elif opc == 5:
                break
            else:
                print("Invalid option. Please enter a number between 1 and 5.")

    menu()