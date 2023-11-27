class Cartao():
    #atributo de classe
    numero_cartao = 100
    
    lista_cartoes = []

    def __init__(self):

        self.numero = Cartao.numero_cartao
        self.itens_pedido = []
        self.ativo = True

        Cartao.numero_cartao += 1

        Cartao.lista_cartoes.append(self)

    def ativarCartao(self):

        pass

    def desativarCartao(self):

        self.ativo = False

    def pegarCartao(self, numero):

        for cartao in Cartao.lista_cartoes:
            
            if(cartao.numero == numero):
                return cartao

    def adicionarPedido(self, numero, pedido):
       
        self.numero = numero
       
        self.itens_pedido.append(pedido)


    def listarPedido(self):

        return self.numero, self.itens_pedido
