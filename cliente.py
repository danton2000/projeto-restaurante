class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome

        self.telefone = telefone

        self.cartao_consumo = None

    def finalizarConsumo(self):
        #Mostrar os itens consumidos do cartão
        
        pass

    def realizarPedido(self, cartao):
        
        self.cartao_consumo = cartao

    def __repr__(self):
        return f"nome: {self.nome}, telefone: {self.telefone}, cartão: {self.cartao_consumo}"
