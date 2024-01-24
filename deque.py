class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append(self, item):
        self.items = self.items + [item]

    def append_left(self, item):
        self.items = [item] + self.items

    def pop(self):
        if not self.is_empty():
            item = self.items[-1]
            self.items = self.items[:-1]
            return item
        else:
            print("O deque está vazio. Não é possível realizar o pop.")

    def pop_left(self):
        if not self.is_empty():
            item = self.items[0]
            self.items = self.items[1:]
            return item
        else:
            print("O deque está vazio. Não é possível realizar o pop no início.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("O deque está vazio. Não há elementos para visualizar.")

    def peek_left(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("O deque está vazio. Não há elementos no início para visualizar.")

    def size(self):
        return len(self.items)


def main():
    deque = Deque()

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar elemento no final do deque")
        print("2. Adicionar elemento no início do deque")
        print("3. Remover elemento do final do deque")
        print("4. Remover elemento do início do deque")
        print("5. Visualizar elemento do final do deque")
        print("6. Visualizar elemento do início do deque")
        print("7. Verificar se o deque está vazio")
        print("8. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            elemento = input("Digite o elemento a ser adicionado no final: ")
            deque.append(elemento)
        elif escolha == "2":
            elemento = input("Digite o elemento a ser adicionado no início: ")
            deque.append_left(elemento)
        elif escolha == "3":
            elemento_removido = deque.pop()
            if elemento_removido is not None:
                print("Elemento removido do final:", elemento_removido)
        elif escolha == "4":
            elemento_removido = deque.pop_left()
            if elemento_removido is not None:
                print("Elemento removido do início:", elemento_removido)
        elif escolha == "5":
            elemento_final = deque.peek()
            if elemento_final is not None:
                print("Elemento do final do deque:", elemento_final)
        elif escolha == "6":
            elemento_inicio = deque.peek_left()
            if elemento_inicio is not None:
                print("Elemento do início do deque:", elemento_inicio)
        elif escolha == "7":
            if deque.is_empty():
                print("O deque está vazio.")
            else:
                print("O deque não está vazio.")
        elif escolha == "8":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
