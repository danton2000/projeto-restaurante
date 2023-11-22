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

# Adicionar o pedido no cartao para o numero do cartao
# Adicionar os cartões criados em uma lista tb, cartões para serem utilizadas
# Criar cartões, informar a qtd
# Menu cartões, com os cartões disponiveis
# Montar Cartão 
# Montar Convidado

# 1 cartão pode ter varios pedidos

# lista de obj nos cartoes(pedido)
# 1 Pedido por vez

# Digitar o numero do cartão ao fazer o pedido
# listar itens(pedido) do cartao

#lista com os obj cartoes com o seus numeros
#cliente: nome, telefone, numero do cartão

#substituir dados escritos por arquivos

#Gerenciar o arquivo? tirar itens no arquivo e adicionar

#Encapsulamento nos atributos
