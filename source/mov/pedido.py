"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: pedido.py - Controle Principal dos pedidos
Autor.......: Mateus Pompermayer
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Abrir - Versao 1.00
              2020-05-10 - [R02] Criação da função Abertos - Versao 1.00
              ...
"""
from source.lib import library
from source.db import db_pedido
from source import user

#Funcao menu dos Pedidos
def Abrir (Table):
    if Table == 0:
        opcao = 1
        while opcao != 0:
            try:
                print('\n******************* PEDIDOS ********************')
                print('   [1] - Fazer Pedido')
                print('   [0] - Voltar')
                opcao = int(input('Digite a opção desejada: '))
                if not 0 <= opcao <= 1:
                    raise ValueError("\n           ***** Valor Inválido *****")
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                if opcao == 1:
                    Fazer_Pedido(True, None)
                    opcao = 0
    elif Table == 1:
        opcao = 1
        while opcao != 0:
            try:
                print('\n******************* PEDIDOS ********************')
                print('   [1] - Consultar')
                print('   [2] - Fechar Pedido')
                print('   [3] - Excluir')
                print('   [0] - Voltar')
                opcao = int(input('Digite a opção desejada: '))
                if not 0 <= opcao <= 3:
                    raise ValueError("\n           ***** Valor Inválido *****")
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                if opcao == 1:
                    Abertos('Consultar')
                    opcao = 0
                elif opcao == 2:
                    Abertos('Atualizar')
                    opcao = 0
                elif opcao == 3:
                    Abertos('Excluir')
                    opcao = 0

##########################################################################################################################################################################################################################################

#Funcao para consultar, fechar(deixar o status como entregue), e excluir o pedido
def Abertos(Type):
    print('\n           ***** Pedidos Abertos *****')
    if Type == 'Consultar':
        Select = True
        while Select:
            try:
                print('\n   [1] - Um Pedido')
                print('   [2] - Todos Pedidos')
                print('   [0] - Voltar')
                opcaoselect = int(input("Digite a opção desejada: "))
                if not 0 <= opcaoselect <= 2:
                    raise ValueError("\n           ***** Valor Inválido *****")
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")

            else:
                if opcaoselect in range(0, 3):
                    if (opcaoselect == 1):
                        Codigo = True
                        while Codigo:
                            try:
                                PedidoCodigo = int(input('\n    Digite o Codigo do Pedido...........: '))
                            except:
                                print("\n           ***** Valor Inválido *****")
                            else:
                                #Chamada da funcao Select do arquivo db_pedido, para exibir pedido referenciado pelo id
                                db_pedido.Select(PedidoCodigo, 'Pedido')
                                Codigo = False
                                Select = False
                    elif (opcaoselect == 2):
                        # Chamada da funcao Select do arquivo db_pedido, para exibir todos pedidos com status true
                        db_pedido.Select('Todos', 'Pedido')
                        Select = False
                    elif (opcaoselect == 0):
                        Select = False

    if Type == 'Atualizar':
        Atualizar = True
        while Atualizar:
            try:
                print('\n   [1] - Pedido')
                print('   [0] - Voltar')
                opcaoatualizar = int(input("Digite a opção desejada: "))
                if not 0 <= opcaoatualizar <= 1:
                    raise ValueError("\n           ***** Valor Inválido *****")
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")

            else:
                if opcaoatualizar in range(0, 2):
                    if (opcaoatualizar == 1):
                        Codigo = True
                        while Codigo:
                            try:
                                PedidoCodigo = int(input('\n    Digite o Codigo do Pedido...........: '))
                            except:
                                print("\n           ***** Valor Inválido *****")
                            else:
                                # Chamada da funcao Select do arquivo db_pedido, para exibir pedido referenciado pelo id, colocando os dados na variavel pedido e usando logo abaixo
                                pedido = db_pedido.Select(PedidoCodigo, 'Pedido')
                                if pedido != None:
                                    Opcao = True
                                    while Opcao:
                                        try:
                                            print('\n   [1] - Fechar pedido')
                                            print('   [2] - Escolher outro pedido')
                                            print('   [0] - Cancelar')
                                            opcao = int(input("Digite a opção desejada: "))
                                            if not 0 <= opcao <= 2:
                                                raise ValueError("\n           ***** Valor Inválido *****")
                                        except ValueError as e:
                                            print("\n           ***** Valor Inválido *****")

                                        else:
                                            if opcao in range(0, 3):
                                                if opcao == 1:
                                                    Codigo = False
                                                    Atualizar = False
                                                    Opcao = False
                                                    #Chamada da funcao Update do arquivo db_pedido, para alterar o status do pedido para deixar como "entregue"
                                                    db_pedido.Update("Status", 0, PedidoCodigo)
                                                    print('\n            ***** Pedido Fechado *****')
                                                elif opcao == 2:
                                                    Opcao = False
                                                elif opcao == 0:
                                                    Codigo = False
                                                    Atualizar = False
                                                    Opcao = False
                                else:
                                    Opcao = True
                                    while Opcao:
                                        try:
                                            print(']n   [1] - Escolher outro pedido')
                                            print('   [0] - Cancelar')
                                            opcao = int(input("Digite a opção desejada: "))
                                            if not 0 <= opcao <= 1:
                                                raise ValueError("\n           ***** Valor Inválido *****")
                                        except ValueError as e:
                                            print("\n           ***** Valor Inválido *****")

                                        else:
                                            if opcao in range(0, 2):
                                                if opcao == 1:
                                                    Opcao = False
                                                elif opcao == 0:
                                                    Codigo = False
                                                    Atualizar = False
                                                    Opcao = False
                    elif (opcaoatualizar == 0):
                        Atualizar = False

    elif Type == 'Excluir':
        Delete = True
        while Delete:
            try:
                print('\n   [1] - Excluir')
                print('   [0] - Cancelar')
                opcaodelete = int(input("Digite a opção desejada: "))
                if not 0 <= opcaodelete <= 1:
                    raise ValueError("\n           ***** Valor Inválido *****")
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")

            else:
                if opcaodelete in range(0, 2):
                    if (opcaodelete == 1):
                        Codigo = True
                        while Codigo:
                            try:
                                PedidoCodigo = int(input('\n    Digite o Codigo do Pedido...........: '))
                            except:
                                print("\n           ***** Valor Inválido *****")
                            else:
                                pedido = db_pedido.Select(PedidoCodigo, 'Delete')
                                Codigo = False
                                Delete = False
                                if pedido != None:
                                    delete = True
                                    while delete:
                                        try:
                                            print('\n   [1] - Excluir')
                                            print('   [0] - Cancelar')
                                            opcaodelete = int(input("Digite a opção desejada: "))
                                            if not 0 <= opcaodelete <= 1:
                                                raise ValueError("\n           ***** Valor Inválido *****")
                                        except ValueError as e:
                                            print("\n           ***** Valor Inválido *****")

                                        else:
                                            if opcaodelete in range(0, 2):
                                                if (opcaodelete == 1):
                                                    # Chamada da funcao Delete do arquivo db_pedido, para excluir pedido pelo id
                                                    db_pedido.Delete(pedido[0][3])
                                                    delete = False
                                                else:
                                                    print('\n              ***** Cancelado *****')
                                                    delete = False
                    else:
                        print('\n              ***** Cancelado *****')
                        Delete = False
##########################################################################################################################################################################################################################################

#Funcao para fazer o pedido, colocando a(s) pizza(s) desejada(s)
def Fazer_Pedido( New, id_pedido):
    if New == True:
        Tel = True
        print('\n           ***** Fazendo Pedido *****')
        while Tel:
            try:
                #Pergunta o telefone do cliente, para verificar se ja esta cadastrado, se nao estiver, cadastra, se ja for cadastrado,
                #mostra as pizzas compradas anteriormente e comeca a fazer o pedido
                tel = input('\n    Digite o Telefone Fixo...........: ')
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                cliente, pizzas = db_pedido.Select(tel, 'Cliente')
                if cliente != None:
                    ID_User = cliente[0]
                    Name_User = cliente[1]
                    if (pizzas != None):
                        if pizzas[0][13] == 2 or pizzas[0][13] == 3:
                            print(f"\nUltimas {pizzas[0][13]} Pizzas Pedidas do(a) {Name_User}:")
                        elif pizzas[0][13] > 3:
                            print(f"\nUltimas 3 Pizzas Pedidas do(a) {Name_User}:")
                        elif pizzas[0][13] == 1:
                            print(f"\nUltima Pizza Pedida do(a) {Name_User}:")
                        elif pizzas[0][13] == 0:
                            print(f"\n     ***** Sem  Historico do(a) {Name_User} *****")

                        for pizza in pizzas:
                            if pizza[0] != None:
                                if pizza[0] == 'Inteira':
                                    print('\n')
                                    print('     Pizza.........: ', pizza[0])
                                    print('     ID............: ', pizza[1])
                                    print('     Nome..........: ', pizza[2])
                                    print('     Tipo..........: ', pizza[3])
                                    print('     Valor Custo...: R$', pizza[4])
                                elif pizza[0] == 'Meia':
                                    if (float(pizza[8].replace(',', '.')) > float(pizza[12].replace(',', '.'))):
                                        print('\n')
                                        print('     Pizza.........: ', pizza[0])
                                        print('     ID 1/2........: ', pizza[5])
                                        print('     ID 2/2........: ', pizza[9])
                                        print('     Metade 1/2....: ', pizza[6])
                                        print('     Metade 2/2....: ', pizza[10])
                                        print('     Tipo 1/2......: ', pizza[7])
                                        print('     Tipo 2/2......: ', pizza[11])
                                        print('     Valor Custo...: R$', pizza[8])
                                    else:
                                        print('\n')
                                        print('     Pizza.........: ', pizza[0])
                                        print('     ID 1/2........: ', pizza[5])
                                        print('     ID 2/2........: ', pizza[9])
                                        print('     Metade 1/2....: ', pizza[6])
                                        print('     Metade 2/2....: ', pizza[10])
                                        print('     Tipo 1/2......: ', pizza[7])
                                        print('     Tipo 2/2......: ', pizza[11])
                                        print('     Valor Custo...: R$', pizza[12])
                        User = True
                        while User:
                            try:
                                print('\n   [1] - Pesquisar novamente')
                                print('   [0] - Cadastrar Pedido')
                                opcao = int(input("Escolha uma opcao: "))
                                if not 0 <= opcao <= 1:
                                    raise ValueError("\n           ***** Valor Inválido *****")
                            except ValueError as e:
                                print("\n           ***** Valor Inválido *****")
                            else:
                                if opcao in range(0, 2):
                                    User = False
                                    if opcao == 0:
                                        Tel = False
                    else:
                        print(f"\n     ***** Sem  Historico do(a) {Name_User} *****")
                        User = True
                        while User:
                            try:
                                print('\n   [1] - Pesquisar novamente')
                                print('   [0] - Cadastrar Pedido')
                                opcao = int(input("Escolha uma opcao: "))
                                if not 0 <= opcao <= 1:
                                    raise ValueError("\n           ***** Valor Inválido *****")
                            except ValueError as e:
                                print("\n           ***** Valor Inválido *****")
                            else:
                                if opcao in range(0, 2):
                                    User = False
                                    if opcao == 0:
                                        Tel = False
                else:
                    print('\n     ***** Nenhum Cadastro Encontrado *****')
                    User = True
                    while User:
                        try:
                            print('\n   [1] - Pesquisar novamente')
                            print('   [0] - Cadastrar Cliente')
                            opcao = int(input("Escolha uma opcao: "))
                            if not 0 <= opcao <= 1:
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")
                        else:
                            if opcao in range(0, 2):
                                User = False
                                if opcao == 0:
                                    Tel = False
                                    ID_User = user.Insert()

        pedido = [ID_User]
        pedido.append(library.Datetime_fmt('YYYY-MM-DD'))
        pedido.append(library.Datetime_fmt('HH:MM:SS'))
        #Insercao do pedido, e pegando o ID, para depois referenciar as pizzas selecionadas nele
        ID_Pedido = db_pedido.Insert('Pedido', pedido)
    print("\n         ***** Selecionar  Pizzas *****")
    Tamanho = True
    Quantidade = True
    CodigoPizzaInteira = True
    CodigoPizzaMeiaUm = True
    CodigoPizzaMeiaDois = True
    PizzaInteiraMeia = True
    Pedido = True
    options = ["Media", "Grande", "Gigante"]
    optionspizza = ["Inteira", "Meia"]

    while PizzaInteiraMeia:
        try:
            print('\nEscolha uma opcao: ')
            print('\n   [1] - ' + optionspizza[0])
            print('   [2] - ' + optionspizza[1])
            opcaopizza = int(input("Pizza Inteira ou Meia: "))
            if not 1 <= opcaopizza <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcaopizza in range(1, 3):
                pizzainteirameia = optionspizza[opcaopizza - 1]
                PizzaInteiraMeia = False
                pizza = [(pizzainteirameia)]
                print('    Pizza...: ' + pizzainteirameia)

    if pizzainteirameia == 'Inteira':
        while CodigoPizzaInteira:
            try:
                cod_pizza = int(input("\nCodigo da Pizza Inteira: "))
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                selectpizza = db_pedido.Select(cod_pizza, 'Pizza')
                if selectpizza != 0:
                    CodigoPizzaInteira = False
                    pizza.append(cod_pizza)
                    print('    Pizza...: ' + selectpizza[2])
    elif pizzainteirameia == 'Meia':
        while CodigoPizzaMeiaUm:
            try:
                cod_pizza = int(input("\nCodigo da Pizza 1/2: "))
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                selectpizzaMeiaUm = db_pedido.Select(cod_pizza, 'Pizza')
                if selectpizzaMeiaUm != 0:
                    CodigoPizzaMeiaUm = False
                    CodigoMeiaUm = cod_pizza
                    pizza.append(cod_pizza)
                    print('    Pizza 1/2...: ' + selectpizzaMeiaUm[2])
        while CodigoPizzaMeiaDois:
            try:
                cod_pizza = int(input("\nCodigo da Pizza 2/2: "))
            except ValueError as e:
                print("\n           ***** Valor Inválido *****")
            else:
                if cod_pizza != CodigoMeiaUm:
                    selectpizzaMeiaDois = db_pedido.Select(cod_pizza, 'Pizza')
                    if selectpizzaMeiaDois != 0:
                        CodigoPizzaMeiaDois = False
                        pizza.append(cod_pizza)
                        print('    Pizza 2/2...: ' + selectpizzaMeiaDois[2])
                else:
                    print("\n      ***** Valor Inválido/Indêntico *****")

    while Tamanho:
        try:
            print('\nEscolha uma opcao: ')
            print('\n   [1] - ' + options[0])
            print('   [2] - ' + options[1])
            print('   [3] - ' + options[2])
            opcaotamanho = int(input("Tamanho da pizza: "))
            if not 1 <= opcaotamanho <= 3:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcaotamanho in range(1, 4):
                tamanhopizza = options[opcaotamanho - 1]
                pizza.append(tamanhopizza)
                Tamanho = False
                print('    Tamanho....: ' + tamanhopizza)
    while Quantidade:
        try:
            if pizzainteirameia == 'Inteira':
                quantidadepizza = int(input(f"Quantidade da Pizza {selectpizza[2]}: "))
            elif pizzainteirameia == 'Meia':
                quantidadepizza = int(input(f"Quantidade da Pizza Meia {selectpizzaMeiaUm[2]}, Meia {selectpizzaMeiaDois[2]}: "))
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if quantidadepizza > 0:
                pizza.append(quantidadepizza)
                Quantidade = False
                print('    Quantidade.: ' + str(quantidadepizza))
            else:
                print("\n           ***** Valor Inválido *****")

    #Chamada da funcao Calcular_Valor do arquivo library, para calcular valor da pizza pelo tamanho e quantidade, calculando o valor unitario e total-parcial do pedido
    if pizzainteirameia == 'Inteira':
        if type(selectpizza[4]) == str:
            Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizza[4].replace(',', '.')), quantidadepizza)
        elif float(selectpizza[4]).is_integer():
            Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizza[4]), quantidadepizza)

    elif pizzainteirameia == 'Meia':
        if type(selectpizzaMeiaDois[4]) == str:
            if (float(selectpizzaMeiaUm[4].replace(',', '.')) > float(selectpizzaMeiaDois[4].replace(',', '.'))):
                Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizzaMeiaUm[4].replace(',', '.')), quantidadepizza)
            else:
                Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizzaMeiaDois[4].replace(',', '.')), quantidadepizza)

        elif float(selectpizza[4]).is_integer():
            if (float(selectpizzaMeiaUm[4]) > float(selectpizzaMeiaDois[4])):
                Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizzaMeiaUm[4]), quantidadepizza)
            else:
                Valor_Parcial, Valor_Unit = library.Calcular_Valor(tamanhopizza, float(selectpizzaMeiaDois[4]), quantidadepizza)

    pizza.append(Valor_Unit)
    pizza.append(Valor_Parcial)
    print('\n    Valor Unitario...: ' + str(Valor_Unit))
    print('    Valor Sub Total..: ' + str(Valor_Parcial))
    while Pedido:
        try:
            print('\n   [1] - Incluir mais Pizzas')
            print('   [0] - Concluir Pedido')
            opcao = int(input("Escolha uma opcao: "))
            if not 0 <= opcao <= 1:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao in range(0, 2):
                if New == False:
                    db_pedido.Update('Hora', library.Datetime_fmt('HH:MM:SS'), id_pedido)
                    ID_Pedido = id_pedido
                if opcao == 1:
                    pizza.append(ID_Pedido)
                    Pedido = False
                    if pizzainteirameia == 'Inteira':
                        db_pedido.Insert('Inteira', pizza)
                    elif pizzainteirameia == 'Meia':
                        db_pedido.Insert('Meia', pizza)
                    Total_Parcial = library.Valores_Pedido('Total', ID_Pedido, None)
                    print('Valor Total-Parcial do Pedido: R$', Total_Parcial)
                    Fazer_Pedido(False, ID_Pedido)
                else:
                    pizza.append(ID_Pedido)
                    if pizzainteirameia == 'Inteira':
                        db_pedido.Insert('Inteira', pizza)
                    elif pizzainteirameia == 'Meia':
                        db_pedido.Insert('Meia', pizza)
                    Pedido = False
                    Total_Pedido = library.Valores_Pedido('Total', ID_Pedido, None)
                    Troco = True
                    while Troco:
                        try:
                            print('\nValor Total do Pedido: R$', Total_Pedido)
                            print('\n   [1] - Precisa de Troco')
                            print('   [0] - Nao precisa de Troco')
                            opcaotroco = int(input("Escolha uma opcao: "))
                            if not 0 <= opcao <= 1:
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")
                        else:
                            if opcaotroco in range(0, 2):
                                Troco = False
                                if opcaotroco == 1:
                                    Precisa = True
                                    while Precisa:
                                        try:
                                            print('\nValor Total do Pedido: R$', Total_Pedido)

                                            valortroco = input("Troco para quantos R$: ")
                                            if not(valortroco.replace(',','',1).isdigit()):
                                                raise ValueError("\n           ***** Valor Inválido *****")

                                        except ValueError as e:
                                            print("\n           ***** Valor Inválido *****")

                                        else:
                                            if valortroco.replace(',','',1).isdigit():
                                                if (float(valortroco.replace(',', '.')) >= float(Total_Pedido.replace(',', '.'))):
                                                    Precisa = False
                                                    db_pedido.Update('Total', Total_Pedido, ID_Pedido)
                                                    valortroco = library.Valores_Pedido('Troco', ID_Pedido, valortroco)
                                                    db_pedido.Update('Troco', valortroco, ID_Pedido)
                                                    print('\nValor Total do Pedido: R$', Total_Pedido)
                                                    print('\nValor do troco a ser levado: R$', valortroco)

                                                    PrevisaoEntrega = db_pedido.Select(ID_Pedido, 'Hora')
                                                    print('\nPrevisao para Entrega: ', PrevisaoEntrega[0][0])

                                                    print('\n          ***** Pedido Realizado *****')
                                                else:
                                                    print('\nValor menor que o total!\n')
                                else:
                                    db_pedido.Update('Total', Total_Pedido, ID_Pedido)
                                    db_pedido.Update('Troco', 0, ID_Pedido)
                                    PrevisaoEntrega = db_pedido.Select(ID_Pedido, 'Hora')
                                    print('\nValor Total do Pedido: R$', Total_Pedido)
                                    print('\nPrevisao para Entrega: ', PrevisaoEntrega[0][0])

                                    print('\n          ***** Pedido Realizado *****')

##########################################################################################################################################################################################################################################