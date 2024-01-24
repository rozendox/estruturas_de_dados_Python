class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, "BLACK")
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, key):
        new_node = Node(key, "RED", self.NIL, self.NIL, None)
        self._insert(new_node)

    def _insert(self, z):
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = "RED"
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)

        self.root.color = "BLACK"


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(f"Key: {node.key}, Color: {node.color}")
        inorder_traversal(node.right)


def print_menu():
    print("\nEscolha uma opção:")
    print("1. Inserir chave na árvore")
    print("2. Visualizar árvore")
    print("3. Sair")


if __name__ == "__main__":
    rb_tree = RedBlackTree()

    while True:
        print_menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            chave = int(input("Digite a chave a ser inserida: "))
            rb_tree.insert(chave)
            print(f"Chave {chave} inserida na árvore Rubro-Negra.")
        elif escolha == "2":
            print("\nÁrvore Rubro-Negra:")
            inorder_traversal(rb_tree.root)
        elif escolha == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
