class Cardapio:
    """
    Class Cardapia
    Objetivo: adicionar itens e preços no cardpio, listar esses itens e excluir os itens.
    """

    def __init__(self):
        self.itens = []
        self.precos = []

    def adicionarItem(self, item, preco, flag=0):
        print(flag)

        if flag == 1:
            self.itens.append(item)

            self.precos.append(preco)
        else:
            # Dados recebidos pelo Json
            self.itens = item

            self.precos = preco

    def listarItens(self):
        print("")
        print("Listando os itens:")
        for index, item in enumerate(self.itens):
            print(f"{index} - {item} - Preço R$ {self.precos[index]}")

        print("")

    def listarItem(self, index):
        return self.itens[index], self.precos[index]

    def excluirItem(self, index_item):
        self.itens.pop(index_item)
        self.precos.pop(index_item)
        return print("Item removido")
