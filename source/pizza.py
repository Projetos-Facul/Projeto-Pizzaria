"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: pizza.py - Funcionalidades para controle das Pizzas
Autor.......: Mateus Pompermayer
Observações.: 2020-05-11 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Menu_Cadastro - Versao 1.00
              2020-05-12 - [R02] Criação da função Insert - Versao 1.00
              2020-05-13 - [R03] Criação da função Update - Versao 1.00
              2020-05-13 - [R04] Criação da função Select - Versao 1.00
              ...
"""

from source.lib import library
from source.db import db_pizza

#Funcao menu da pizza
def Menu_Cadastro():
    opcao = 1
    while opcao != 0:
        try:
            print('\n******************** PIZZAS ********************')
            print('   [1] - Inserir')
            print('   [2] - Alterar')
            print('   [3] - Consultar')
            print('   [4] - Excluir')
            print('   [0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 4:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                Insert()
            elif opcao == 2:
                Update()
            elif opcao == 3:
                Select()
            elif opcao == 4:
                Delete()

###########################################################################################################################################################################################

#Funcao para inserir pizza
def Insert():

    print('\n         ***** Inserindo Pizza *****')
    pizza = [input('\n    Nome da Pizza...........: ')]
    options = ["Salgada", "Doce"]
    type = True
    value = True
    while type:
        try:
            print('\n   [1] - ' + options[0])
            print('   [2] - ' + options[1])
            opcao = int(input("Numero do tipo da pizza: "))
            if not 1 <= opcao <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcao in range(1, 3):
                tipo = options[opcao - 1]
                pizza.append(tipo)
                type = False
                print('    Tipo...: ' + tipo)

    pizza.append(library.Datetime_fmt('YYYY-MM-DD HH:MM:SS.MS'))
    pizza.append(input('    Ingredientes...: '))

    while value:
        try:
            valor = input('    Valor Custo Padrao............: ')
            if not(valor.replace(',','',1).isdigit()):
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if valor.replace(',','',1).isdigit():
                pizza.append(valor)
                value = False


    db_pizza.Insert(pizza)

###########################################################################################################################################################################################

#Funcao para fazer alteracao na pizza
def Update():
    update = True
    updatebool = True
    typeupdate = True
    valueupdate = True
    inativacao = False
    updateinativacao = False

    print('\n          ***** Atualizando Pizza *****')
    while update:
        try:
            PizzaCodigo = int(input('\n    Digite o Codigo da Pizza...........: '))
        except:
            print("\n           ***** Valor Inválido *****")
        else:
            pizza = db_pizza.Select(PizzaCodigo, False, True)
            if pizza != None:
                print('\nPizza Selecionada: ', pizza[2])
                print('     Id............: ', pizza[0])
                print('     Tipo..........: ', pizza[1])
                print('     Nome..........: ', pizza[2])
                print('     Igredientes...: ', pizza[3])
                print('     Valor Custo...: R$', pizza[4])
                pizzainativa = pizza[5]
                update = False

    if pizzainativa != None:
        inativacao = True

    while updatebool:
        try:
            print('\n   [1] - Sim')
            print('   [2] - Nao')
            opcaoupdate = int(input("Deseja alterar essa pizza?: "))
            if not 1 <= opcaoupdate <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcaoupdate in range(1, 3):
                if(opcaoupdate == 1):
                    pizzaupdate = [input('\n    Nome da Pizza...........: ')]
                    optionsupdate = ["Salgada", "Doce"]
                    updatebool = False

                    while typeupdate:
                        try:
                            print('\n   [1] - ' + optionsupdate[0])
                            print('   [2] - ' + optionsupdate[1])
                            opcaoupdate = int(input("Numero do tipo da pizza: "))
                            if not 1 <= opcaoupdate <= 2:
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")

                        else:
                            if opcaoupdate in range(1, 3):
                                tipoupdate = optionsupdate[opcaoupdate - 1]
                                pizzaupdate.append(tipoupdate)
                                typeupdate = False
                                print('    Tipo...: ' + tipoupdate)

                    pizzaupdate.append(input('    Ingredientes...: '))

                    while valueupdate:
                        try:
                            valorupdate = input('    Valor Custo Padrao............: ')
                            if not (valorupdate.replace(',', '', 1).isdigit()):
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")

                        else:
                            if valorupdate.replace(',', '', 1).isdigit():
                                pizzaupdate.append(valorupdate)
                                valueupdate = False

                    while inativacao:
                        try:
                            print('\n   [1] - Sim')
                            print('   [2] - Nao')
                            inativacaoupdate = int(input('\n    Deseja reincluir essa pizza............: '))
                            if not 1 <= inativacaoupdate <= 2:
                                raise ValueError("\n           ***** Valor Inválido *****")
                        except ValueError as e:
                            print("\n           ***** Valor Inválido *****")


                        else:
                            if inativacaoupdate in range(1, 3):
                                if inativacaoupdate == 1:
                                    updateinativacao = True
                                    inativacao = False
                                else:
                                    updateinativacao = False
                                    inativacao = False


                    pizzaupdate.append(PizzaCodigo)

                    if updateinativacao == True:
                        db_pizza.Update(pizzaupdate, updateinativacao)
                    else:
                        db_pizza.Update(pizzaupdate, updateinativacao)

                else:
                    print('           ***** Pizza não alterada *****')
                    updatebool = False

###########################################################################################################################################################################################

#Funcao para mostrar dados da pizza
def Select():
    Select = True
    print('\n            ***** Buscando Pizza *****')
    while Select:
        try:
            print('\n   [1] - Uma Pizza')
            print('   [2] - Todas Pizzas')
            print('   [3] - Pizzas Desativadas')
            print('   [0] - Voltar')
            opcaoselect = int(input("Digite a opção desejada: "))
            if not 0 <= opcaoselect <= 3:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcaoselect in range(0, 4):
                if(opcaoselect == 1):
                    Codigo = True
                    while Codigo:
                        try:
                            PizzaCodigo = int(input('\n    Digite o Codigo da Pizza...........: '))
                        except:
                            print("\n           ***** Valor Inválido *****")
                        else:
                            db_pizza.Select(PizzaCodigo, 'Uma', False)
                            Codigo = False
                            Select = False
                elif (opcaoselect == 2):
                    db_pizza.Select( 0, 'Todas', False)
                    Select = False
                elif (opcaoselect == 3):
                    db_pizza.Select(0, 'Desativadas', False)
                    Select = False
                elif (opcaoselect == 0):
                    Select = False

###########################################################################################################################################################################################

#Funcao para deletar(desativar) pizza
def Delete():
    Delete = True
    delete = True
    print('\n           ***** Deletando *****')
    while delete:
        try:
            PizzaCodigo = int(input('\n    Digite o Codigo da Pizza...........: '))
        except:
            print("\n           ***** Valor Inválido *****")

        else:
            pizza = db_pizza.Select(PizzaCodigo, False, True)
            if pizza != None:
                print('\n  Pizza Selecionada: ', pizza[2])
                print('  ID:', pizza[0], '\n', ' Tipo:', pizza[1], '\n', ' Nome:', pizza[2], '\n', ' Ingredientes:',
                  pizza[3], '\n', ' Valor Custo:', pizza[4])
                delete = False

    while Delete:
        try:
            print('\n   [1] - Desativar')
            print('   [2] - Cancelar')
            opcaodelete = int(input("Digite a opção desejada: "))
            if not 1 <= opcaodelete <= 2:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")

        else:
            if opcaodelete in range(1, 3):
                if(opcaodelete == 1):
                    data_inativacao = library.Datetime_fmt('YYYY-MM-DD HH:MM:SS.MS')
                    db_pizza.Delete(data_inativacao, PizzaCodigo)
                    Delete = False
                else:
                    print('\n              ***** Cancelado *****')
                    Delete = False

###########################################################################################################################################################################################