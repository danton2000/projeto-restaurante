class Cardapio:
    """
    Class Cardapia
    Objetivo: adicionar itens e preços no cardpio, listar esses itens e excluir os itens.
    """

    def __init__(self):
        self.itens = []
        self.precos = []
        self.inicializa_cardapio()

    def inicializa_cardapio(self):
        """Este metodo utiliza o arquivo arqmenu.json para
        criar o cardápio com os itens.
        A metodo lê o arquivo JSON, instancia um cardápio, popula o cardápio e retorna um cardápio pronto.
        """
        import json

        arquivo = open("itens_cardapio.json", "r")
        dic_temp = json.load(arquivo)
        arquivo.close()

        # print(dic_temp)

        self.itens = list(dic_temp.keys())

        self.precos = list(dic_temp.values())

    def adicionarItem(self, item, preco):
        self.itens.append(item)

        self.precos.append(preco)

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
