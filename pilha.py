class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items = self.items + [item]

    def pop(self):
        if not self.is_empty():
            item = self.items[-1]
            self.items = self.items[:-1]
            return item
        else:
            print("A pilha está vazia. Não é possível realizar o pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("A pilha está vazia. Não há elementos para visualizar.")

    def size(self):
        return len(self.items)


def main():
    pilha = Pilha()

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar elemento à pilha")
        print("2. Remover elemento do topo da pilha")
        print("3. Visualizar elemento do topo da pilha")
        print("4. Verificar se a pilha está vazia")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            elemento = input("Digite o elemento a ser adicionado: ")
            pilha.push(elemento)
        elif escolha == "2":
            elemento_removido = pilha.pop()
            if elemento_removido is not None:
                print("Elemento removido:", elemento_removido)
        elif escolha == "3":
            elemento_topo = pilha.peek()
            if elemento_topo is not None:
                print("Elemento do topo da pilha:", elemento_topo)
        elif escolha == "4":
            if pilha.is_empty():
                print("A pilha está vazia.")
            else:
                print("A pilha não está vazia.")
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
