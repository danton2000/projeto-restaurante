# Importando a classe Cardapia para pode utilizar seus atributos e metodos
from cardapio import Cardapio

# Instanciando a classe Cardapio e craindo um obj
cardapio = Cardapio()

from pedido import Pedido

from cartao import Cartao

from cliente import Cliente


while True:
    print("--Menu--")
    print("1 - Adicionar item cardápio")
    print("2 - Ver itens do cardápio")
    print("3 - Fazer Pedidos")
    print("4 - Remover item cardápio")
    print("5 - Criar Cartões")
    print("6 - Ver Cartões")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        item = input("Digite nome do item: ")

        preco = float(input("Digite o preço do item: "))

        # Adicionando um pedido manualmente com o preço
        cardapio.adicionarItem(item, preco)

    elif opcao == "2":
       
        while True:
        
            # Listando todos os itens do cardapio com os preços
            cardapio.listarItens()

            break

    elif opcao == "3":

        #Verificando se existe cartões instaciados
        try:
            cartao.lista_cartoes
        except:
            print("Não tem cartões disponiveis no momento.")
            continue

        # mostrar cartões ATIVO
        for cartao in cartao.lista_cartoes:

            if (cartao.ativo == True):
                print(f"Cartão {cartao.numero}")

        # qual o numero do cartao?
        numero_cartao = int(input("Numero do cartão: "))

        # preciso descobrir o obj pelo numero do cartao
        cartao_escolhido = cartao.pegarCartao(numero_cartao)

        # Pegando as informações do cliente para vincular ao cartão
        nome_cliente = input("Nome do Cliente: ")

        telefone_cliente = input("Telefone do Cliente: ")

        # Criando um cliente
        cliente = Cliente(nome_cliente, telefone_cliente)

        while True:
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

                cliente.realizarPedido(cartao_escolhido)

                print(cliente)

                #INATIVANDO o cartão após o pedido
                cartao_escolhido.desativarCartao()

                break

        print("Pedido Criado:")
        for item_pedido in cartao_escolhido.listarPedido()[1]:
            print(f"Cartão: {cartao_escolhido.listarPedido()[0]} - {item_pedido.item}")

    elif opcao == "4":
        index = int(input("Remover qual item: "))

        # Deletando um item do cardapio
        cardapio.excluirItem(index)

    elif opcao == "5":
        qtd_cartoes = int(input("Adicionar quantos cartões ? "))

        for x in range(qtd_cartoes):
            cartao = Cartao()

    elif opcao == "6":
        for cartao in cartao.lista_cartoes:
            print(f"Cartão {cartao.numero}")

    else:
        print("Opção invalida!")
