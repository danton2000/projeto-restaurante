# Importando a classe Cardapia para pode utilizar seus atributos e metodos
from cardapio import Cardapio

# Instanciando a classe Cardapio e craindo um obj
cardapio = Cardapio()

from pedido import Pedido

from cartao import Cartao

from cliente import Cliente


def inicializa_cardapio():
    """Esta função utiliza o arquivo arqmenu.json para
    criar o cardápio com os itens.
    A função lê o arquivo JSON, instancia um cardápio, popula o cardápio e retorna um cardápio pronto.
    """
    import json

    arquivo = open("itens_cardapio.json", "r")
    dic_temp = json.load(arquivo)
    arquivo.close()

    cardapio.adicionarItem(list(dic_temp.keys()), list(dic_temp.values()))

    return cardapio


while True:
    print("--Menu--")
    print("1 - Adicionar item")
    print("2 - Ver Itens")
    print("3 - Remover item")
    print("4 - Criar Cartões")
    print("5 - Ver Cartões")

    opcao = input("Digite uma opção: ")

    inicializa_cardapio()

    if opcao == "1":
        item = input("Digite nome do item: ")

        preco = float(input("Digite o preço do item: "))

        # Adicionando um pedido manualmente com o preço
        cardapio.adicionarItem(item, preco, 1)

        #Verificar o adicionar itens pelo Json

    elif opcao == "2":
        # mostrar cartões
        for cartao in cartao.lista_cartoes:
            print(f"Cartão {cartao.numero}")

        # qual o numero do cartao?
        numero_cartao = int(input("Numero do cartão: "))

        # preciso descobrir o obj pelo numero do cartao
        cartao_escolhido = cartao.pegarCartao(numero_cartao)

        while True:
            # Pegando as informações do cliente para vincular ao cartão
            nome_cliente = input("Nome do Cliente: ")

            telefone_cliente = input("Telefone do Cliente: ")

            # Listando todos os itens do cardapio com os preços
            cardapio.listarItens()

            item_escolhido = int(input("Escolha 1 item: "))
            item_quantidade = int(input("Quantidade: "))

            # Pegando o item selecionando(pelo indice) utilizando a o metodo da classe Cardapio
            item_escolhido = cardapio.listarItem(item_escolhido)

            # nova instancia para os itens do pedido
            pedido = Pedido()

            # Escolendo o item para o pedido
            pedido.escolherItem(item_escolhido, item_quantidade)

            # Mostrnado o item para o pedido
            pedido.listarItem()

            # alterando os atributos do cartão escolhido(obj)
            cartao_escolhido.adicionarPedido(numero_cartao, pedido)

            continuar = input("Adicionar mais itens? (s/n): ")

            if continuar == "s":
                continue
            else:
                print(cartao_escolhido)

                cliente = Cliente(nome_cliente, telefone_cliente, cartao_escolhido)

                print(cliente)
                break

        print("Pedido Criado:")
        for item_pedido in cartao_escolhido.listarPedido()[1]:
            print(f"Pedido: {cartao_escolhido.listarPedido()[0]} - {item_pedido.item}")

    elif opcao == "3":
        index = int(input("Remover qual item: "))

        # Deletando um item do cardapio
        cardapio.excluirItem(index)

    elif opcao == "4":
        qtd_cartoes = int(input("Adicionar quantos cartões ? "))

        for x in range(qtd_cartoes):
            cartao = Cartao()

    elif opcao == "5":
        for cartao in cartao.lista_cartoes:
            print(f"Cartão {cartao.numero}")

    else:
        print("Opção invalida!")
