from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, telefone):
        self.nome = nome

        self.telefone = telefone

        self.cartao_consumo = None

    def finalizarConsumo(self, itens_consumidos):
        #Mostrar os itens consumidos do cartão
        for item_pedido in itens_consumidos[1]:
            print(f"Cartão: {itens_consumidos[0]} - {item_pedido.item} - {item_pedido.preco}")
        

    def realizarPedido(self, cartao):
        
        self.cartao_consumo = cartao

    def __repr__(self):
        return f"nome: {self.nome}, telefone: {self.telefone}, cartão: {self.cartao_consumo}"
