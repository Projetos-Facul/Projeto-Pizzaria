"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para tratativas em pedidos
Arquivo.....: user.py - Funcionalidades para controle dos usuarios
Autor.......: Vinicius Guedes
Observações.: 2020-05-11 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-11 - [R01] Criação da função Menu_Cadastro - Versao 1.00
              2020-05-11 - [R02] Alteração na função Menu_Cadastro - Versao 1.00
              2020-05-11 - [R03] Criação e alteração na função Insert - Versao 1.00
              2020-05-11 - [R03] Criação e alteração na função Update - Versao 1.00
              2020-05-11 - [R03] Criação na função Select - Versao 1.00
              2020-05-11 - [R03] Criação da função Delete - Versao 1.00
              ...
"""
from source.db import db_user
from source.lib import library

#Menu de chamada das Funçoes Principais
def Menu_Cadastro():
    opcao = 1
    while opcao != 0:
        try:
            print('\n******************* CLIENTES *******************')
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

############################################################################################################################################################################

#Funcao de inserção de usuario
def Insert ():
    print('\n          ***** Inserindo Cliente *****')
    print("    ID.............: ", db_user.Achar_Id())
    usuario = [(input('    Nome...........: '),
                input('    Telefone Fixo..: '),
                input('    Telefone Cel...: '),
                input('    CEP............: '),
                input('    Endereço.......: '),
                input('    Numero.........: '),
                input('    Complemento....: '),
                input('    Bairro.........: '),
                input('    Cidade.........: '),
                input('    UF.............: '),
                library.Datetime_fmt('YYYY-MM-DD'))]
    #Chamada do banco
    ID = db_user.insert(usuario)
    print('\n         ***** Usuario adicionado *****')

    return ID

############################################################################################################################################################################

#Funcao de Atualização de usuario
def Update ():
    opcao = 1
    while opcao != 0:
        try:
            print('\n        ***** Atualizando  Cliente *****')
            print('\n     [1] - Cod do Cliente')
            print('     [2] - Telefone Fixo')
            print('     [3] - Telefone Celular')
            print('     [0] - Voltar')
            opcao = eval(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 3:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            user = db_user.select(4, 'tudo')
            if user == []:
                print("\n     ***** Nenhum Cadastro Encontrado *****")
            else:
                if opcao != 0:
                    if opcao == 1:
                        ref = eval(input('\n     ID Cliente..: '))
                        user = db_user.select(1, ref)
                        # Chamada do banco
                    elif opcao == 2:
                        ref = eval(input('\n     Telefone Fixo..: '))
                        user = db_user.select(2, ref)
                        # Chamada do banco
                    elif opcao == 3:
                        ref = eval(input('\n     Telefone Celular..: '))
                        user = db_user.select(3, ref)
                        # Chamada do banco
                    if user == None or user == []:
                        print("\n     ***** Nenhum Cadastro Encontrado *****")
                    else:
                        print("\n            ***** Dados  Atuais *****\n")
                        Exibir_Select(user, 1)
                        # Chamada do banco
                        opcao = 1
                        while opcao != 2:
                            try:
                                print('   [1] - Sim')
                                print('   [2] - Nao')
                                opcao = int(input("Deseja alterar esse usuario?: "))
                                if not 0 <= opcao <= 3:
                                    raise ValueError("\n           ***** Valor Inválido *****")
                            except ValueError as e:
                                print("\n           ***** Valor Inválido *****")
                            else:
                                if opcao == 1:
                                    print('    ID.............:', user[0])
                                    usuario = [(input('    Nome...........: '),
                                                input('    Telefone Fixo..: '),
                                                input('    Telefone Cel...: '),
                                                input('    CEP............: '),
                                                input('    Endereço.......: '),
                                                input('    Numero.........: '),
                                                input('    Complemento....: '),
                                                input('    Bairro.........: '),
                                                input('    Cidade.........: '),
                                                input('    UF.............: '),
                                                user[0])]
                                    # Chamada do banco
                                    db_user.update(usuario)
                                    print('\n          ***** Usuario Alterado *****')
                                    opcao = 2
                                elif opcao == 2:
                                    pass
                        opcao=0

############################################################################################################################################################################

#Funcao de busca de usuario
def Select ():
    opcao =1
    while opcao != 0:
        try:
            print('\n          ***** Buscando Cliente *****')
            print(' Buscar por:')
            print('   [1] - ID')
            print('   [2] - Telefone Fixo ')
            print('   [3] - Telefone Celular')
            print('   [4] - Listar Todos')
            print('   [0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 4:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            # Chamada do banco
            user = db_user.select(4, 'tudo')
            if user == []:
                print("\n     ***** Nenhum Cadastro Encontrado *****")
            else:
                if opcao == 1:
                    ref = input('     ID..: ')
                    # Chamada do banco
                    user = db_user.select(1, ref)
                    Exibir_Select(user,1)
                elif opcao == 2:
                    ref = input('     Telefone Fixo..: ')
                    # Chamada do banco
                    user = db_user.select(2, ref)
                    Exibir_Select(user,1)
                elif opcao == 3:
                    ref = input('     Telefone Celular..: ')
                    # Chamada do banco
                    user = db_user.select(3, ref)
                    Exibir_Select(user,1)
                elif opcao == 4:
                    for row in user:
                        Exibir_Select(row,1)
                opcao=0

#Funcao de exibicao de usuario
def Exibir_Select(user,tipo):
    if tipo == 1:
        if not user == None:
            print('\n     Id............: ', user[0])
            print('     Nome..........: ', user[1])
            print('     Telefone Fixo.: ', user[2])
            print('     Telefone Cel..: ', user[3])
            print('     CEP...........: ', user[4])
            print('     Endereço......: ', user[5])
            print('     Numero........: ', user[6])
            print('     Complemento...: ', user[7])
            print('     Bairro........: ', user[8])
            print('     Cidade........: ', user[9])
            print('     UF............: ', user[10])
            print('     Criado em.....: ', user[11])
            print('\n')
        else:
            print("     ***** Nenhum Cadastro Encontrado *****")
    elif tipo == 2:
        print('Tipo 2')


############################################################################################################################################################################

#Funcao de remocao de usuario
def Delete ():
    opcao = 1
    while opcao != 0:
        try:
            print('\n        ***** Deletando  Cliente *****')
            print('\n     [1] - Cod do Cliente')
            print('     [2] - Telefone Fixo')
            print('     [3] - Telefone Celular')
            print('     [0] - Voltar')
            opcao = eval(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 3:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            user = db_user.select(4, 'tudo')
            if user == []:
                print("\n     ***** Nenhum Cadastro Encontrado *****")
            else:
                if opcao != 0:
                    if opcao == 1:
                        ref = eval(input('\n     ID Cliente..: '))
                        # Chamada do banco
                        user = db_user.select(1, ref)

                    elif opcao == 2:
                        ref = eval(input('\n     Telefone Fixo..: '))
                        # Chamada do banco
                        user = db_user.select(2, ref)

                    elif opcao == 3:
                        ref = eval(input('\n     Telefone Celular..: '))
                        # Chamada do banco
                        user = db_user.select(3, ref)

                    if user == None or user == []:
                        print("\n     ***** Nenhum Cadastro Encontrado *****")
                    else:
                        print("\n            ***** Dados  Atuais *****\n")
                        Exibir_Select(user, 1)

                        opcao = 1
                        while opcao != 2:
                            try:
                                print('   [1] - Sim')
                                print('   [2] - Nao')
                                opcao = int(input("Deseja excluir esse usuario?: "))
                                if not 0 <= opcao <= 3:
                                    raise ValueError("\n           ***** Valor Inválido *****")
                            except ValueError as e:
                                print("\n           ***** Valor Inválido *****")
                            else:
                                if opcao == 1:
                                    # Chamada do banco
                                    db_user.delete(user[0])
                                    opcao = 2
                                elif opcao == 2:
                                    pass
                        opcao = 0