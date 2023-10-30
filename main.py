# Importando o arquivo que tem as informações dos itens e preços
from informacaoes import *
# Tratando essas informações e inserindo em 2 listas
itens = aux_itens.split(';\n')
precos = aux_precos.split('\n')

# Importando a classe Cardapia para pode utilizar seus atributos e metodos
from cardapio import Cardapio

# Instanciando a classe Cardapio e craindo um obj
cardapio = Cardapio()

# Percorrendo a lista dos itens e desmembrando ela para pegar cada item e seu indice
for index, item in enumerate(itens):
    
    # Adicionando o item no cardapio e com o preço, uitilizando a lista  de preços e acessando pelo indice do item
    cardapio.adicionarItem(item, precos[index])

from pedido import Pedido

from cartao import Cartao

while True:

    print("--Menu--")
    print("1 - Adicionar item")
    print("2 - Ver Itens")
    print("3 - Remover item")
    print("4 - Criar Cartões")
    print("5 - Ver Cartões")

    opcao = input("Digite uma opção: ")

    if(opcao == "1"):

        item = input("Digite nome do item: ")

        preco = float(input("Digite o preço do item: "))

        # Adicionando um pedido manualmente com o preço
        cardapio.adicionarItem(item, preco)

    elif(opcao == "2"):

        # mostrar cartões
        for cartao in cartao.lista_cartoes:
            print(f"Cartão {cartao.numero}")

        # qual o numero do cartao?
        numero_cartao = int(input("Numero do cartão: "))

        #preciso descobrir o obj pelo numero do cartao 
        cartao_escolhido = cartao.pegarCartao(numero_cartao)

        while True:

            # Listando todos os itens do cardapio com os preços
            cardapio.listarItens()

            item_escolhido = int(input("Escolha 1 item: "))
            item_quantidade = int(input("Quantidade: "))

            # Pegando o item selecionando(pelo indice) utilizando a o metodo da classe Cardapio
            item_escolhido = cardapio.listarItem(item_escolhido)

            #nova instancia para os itens do pedido
            pedido = Pedido()

            # Escolendo o item para o pedido
            pedido.escolherItem(item_escolhido, item_quantidade)

            # Mostrnado o item para o pedido
            pedido.listarItem()
            
            #alterando os atributos do cartão escolhido(obj)
            cartao_escolhido.adicionarPedido(numero_cartao, pedido)

            continuar = input("Adicionar mais itens? (s/n): ")

            if continuar == 's':
                continue
            else:
                break


        print("Pedido Criado:")
        for item_pedido in cartao_escolhido.listarPedido()[1]:
            print(f"Pedido: {cartao_escolhido.listarPedido()[0]} - {item_pedido.item}")

    elif(opcao == "3"):

        index = int(input("Remover qual item: "))

        # Deletando um item do cardapio
        cardapio.excluirItem(index)

    elif(opcao == "4"):
        
        qtd_cartoes = int(input("Adicionar quantos cartões ? "))

        for x in range(qtd_cartoes):
            cartao = Cartao()
            
    elif(opcao == "5"):

        for cartao in cartao.lista_cartoes:
            print(f"Cartão {cartao.numero}")
            
    else:
        print("Opção invalida!")
