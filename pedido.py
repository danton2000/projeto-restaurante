class Pedido():
    """
    Classe Pedido
    Objetivo: Registra o item selecionando para o pedido, cada instancia dessa classe é um pedido
    """
    def __init__(self):

        self.item = 0
        self.preco = 0
        self.quantidade = 0

    def escolherItem(self, cardapio, quantidade):

        # Inserindo as informação do item selecionado para o pedido
        self.item = cardapio[0]

        preco_total = float(cardapio[1]) * int(quantidade)

        self.preco = preco_total

        self.quantidade = quantidade

    def listarItem(self):

        return print(f"Pedido: {self.item} - Quantidade: {self.quantidade} - Preço: {self.preco}")




