class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome

        self.telefone = telefone

    def __repr__(self):
        return f"nome: {self.nome}, telefone: {self.telefone}"

