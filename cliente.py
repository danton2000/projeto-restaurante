class Cliente:
    def __init__(self, nome, telefone, cartao):
        self.nome = nome

        self.telefone = telefone

        self.cartao_consumo = cartao

    def finalizarConsumo(self):
        pass

    def realizarPedido(self):
        pass

    def __repr__(self):
        return f"nome: {self.nome}, telefone: {self.telefone}, cartão: {self.cartao_consumo}"
