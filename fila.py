class Fila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items = self.items + [item]

    def dequeue(self):
        if not self.is_empty():
            item = self.items[0]
            self.items = self.items[1:]
            return item
        else:
            print("A fila está vazia. Não é possível realizar o dequeue.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("A fila está vazia. Não há elementos para visualizar.")

    def size(self):
        return len(self.items)


def main():
    fila = Fila()

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar elemento à fila")
        print("2. Remover elemento do início da fila")
        print("3. Visualizar elemento do início da fila")
        print("4. Verificar se a fila está vazia")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            elemento = input("Digite o elemento a ser adicionado: ")
            fila.enqueue(elemento)
        elif escolha == "2":
            elemento_removido = fila.dequeue()
            if elemento_removido is not None:
                print("Elemento removido:", elemento_removido)
        elif escolha == "3":
            elemento_inicio = fila.peek()
            if elemento_inicio is not None:
                print("Elemento do início da fila:", elemento_inicio)
        elif escolha == "4":
            if fila.is_empty():
                print("A fila está vazia.")
            else:
                print("A fila não está vazia.")
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
