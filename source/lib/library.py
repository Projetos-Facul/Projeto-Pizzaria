"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto03
Descricao...: Arquivo de biblioteca padrão
Arquivo.....: library.py - Função Principal contendo menu para chamada das demais funções
Autor.......: Vinicius Guedes / Mateus Pompermayer
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-10 - [R01] Criação da função Datetime_fmt - Versao 1.00
              2020-05-10 - [R02] Criação da função Limpar_Tela - Versao 1.00
              2020-05-10 - [R03] Criação da função Cabeçalho_Geral - Versao 1.00
              2020-05-10 - [R04] Criação da função Pause - Versao 1.00
              2020-05-10 - [R05] Criação da função Menu_Inicial - Versao 1.00
              2020-05-10 - [R06] Criação da função Menu_Movimentacao - Versao 1.00
              2020-05-11 - [R07] Tentativa de criação da função Abrir_Banco - Versao 1.00
              2020-05-11 - [R08] Tentativa de criação da função data_entry - Versao 1.00
              ...
"""

import datetime
from source.mov import pedido
from source import user
from source import pizza
from source.report import report
from source.db.database import tables
from source.db import db_pizza
from source.db import db_pedido


# Retorna somente a data e hora atual, novo (retorna so hora ou so data)
def Datetime_fmt(formatstring):
    # no formato YYYY-MM-DD HH: MM:SS
    if formatstring == 'YYYY-MM-DD HH:MM:SS.MS':
        return format(datetime.datetime.now())
    if formatstring == 'YYYY-MM-DD':
        return format(datetime.date.today())
    if formatstring == 'HH:MM:SS':
        minutesLater = datetime.datetime.today() + datetime.timedelta(minutes = 50)
        minutesLater = minutesLater.strftime("%H:%M:%S")
        return format(minutesLater)

def Limpar_Tela():
    print('\n' * 40)

def Cabecalho_Geral():
    Limpar_Tela()
    print('\n************************************************')
    print('* BOB´s PIZZARIA - SISTEMA CONTROLE DE PEDIDOS *')
    print('* Desenvolvido por Guedeneti Systems           *')
    print('* Centro Universiário "Padre Anchieta"         *')
    print('************************************************')

def Pause():
    programPause = input("\nPressione <ENTER> para continuar...")

def Menu_Inicial():
    Cabecalho_Geral()
    opcao = 1
    while opcao != 0:
        try:
            print('\n**************** MENU PRINCIPAL ****************')
            print('   [1] - Abrir Pedido')
            print('   [2] - Pedidos Abertos')
            print('   [3] - Movimentações Cadastrais')
            print('   [4] - Relatórios')
            print('   [0] - Sair')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 4:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                pedido.Abrir(0)
            elif opcao == 2:
                pedido.Abrir(1)
            elif opcao == 3:
                Menu_Movimentacao()
            elif opcao == 4:
                report.Menu_Relatorio()

def Menu_Movimentacao():
    opcao = 1;
    while opcao != 0:
        try:
            print('\n************** MENU MOVIMENTAÇÕES **************')
            print('   [1] - Usuarios')
            print('   [2] - Pizzas')
            print('   [9] - Reset de banco')
            print('   [0] - Voltar ao Menu Principal')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 2 and opcao != 9:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                user.Menu_Cadastro()
            elif opcao == 2:
                pizza.Menu_Cadastro()
            elif opcao == 9:
                ref = "BOB"
                while ref != 'BOB-PIZZARIA':
                    print('\n    Você está preste a apagar todos os dados do banco de dados!')
                    print('    Para confirmar digite BOB-PIZZARIA\n'
                          '    Para voltar digite SAIR')
                    ref = input('    Frase: ')
                    if ref == 'BOB-PIZZARIA':
                        tables.create_table()
                        print('\n         ***** BANCO  REINICIADO *****')
                    elif ref == 'SAIR':
                        ref= 'BOB-PIZZARIA'

#Funcao para calcular valores da pizza, fazendo o calculo a partir do tamanho e quantidade de pizzas
def Calcular_Valor(Tamanho, Valor, Qtde):
    if Tamanho == 'Media':
        Valor_Parcial = (Valor * 1.15) * Qtde
        Valor_Unit = Valor * 1.15

        Valor_Parcial = float("{:.2f}".format(Valor_Parcial))
        Valor_Unit = float("{:.2f}".format(Valor_Unit))

        Valor_Unit = str(Valor_Unit)
        Valor_Parcial = str(Valor_Parcial)
        Valor_Unit = str(Valor_Unit.replace('.', ','))
        Valor_Parcial = str(Valor_Parcial.replace('.', ','))

        return Valor_Parcial, Valor_Unit
    elif Tamanho == 'Grande':
        Valor_Parcial = (Valor * 1.25) * Qtde
        Valor_Unit = Valor * 1.25

        Valor_Parcial = float("{:.2f}".format(Valor_Parcial))
        Valor_Unit = float("{:.2f}".format(Valor_Unit))

        Valor_Unit = str(Valor_Unit)
        Valor_Parcial = str(Valor_Parcial)
        Valor_Unit = str(Valor_Unit.replace('.', ','))
        Valor_Parcial = str(Valor_Parcial.replace('.', ','))

        return Valor_Parcial, Valor_Unit
    elif Tamanho == 'Gigante':
        Valor_Parcial = (Valor * 1.35) * Qtde
        Valor_Unit = Valor * 1.35

        Valor_Parcial = float("{:.2f}".format(Valor_Parcial))
        Valor_Unit = float("{:.2f}".format(Valor_Unit))

        Valor_Unit = str(Valor_Unit)
        Valor_Parcial = str(Valor_Parcial)
        Valor_Unit = str(Valor_Unit.replace('.', ','))
        Valor_Parcial = str(Valor_Parcial.replace('.', ','))

        return Valor_Parcial, Valor_Unit

#Funcao para calcular valores do pedido, fazendo o calculo a partir do pedido, para calcular o total ou o troco do pedido
def Valores_Pedido(Pedido, id_pedido, Troco):
    if Pedido == 'Total':
        Valores = db_pedido.Select(id_pedido, 'Valor')
        Total = 0

        for Valor in Valores:
            ValorFloat = float(Valor[0].replace(',', '.'))
            Total = float("{:.2f}".format(Total + ValorFloat))

        Total = str(Total)
        Total = str(Total.replace('.', ','))

        return Total

    if Pedido == 'Troco':
        Valores = db_pedido.Select(id_pedido, 'Valor')
        Total = 0
        for Valor in Valores:
            ValorFloat = float(Valor[0].replace(',', '.'))
            Total = float("{:.2f}".format(Total + ValorFloat))

        TrocoFloat = float(Troco.replace(',', '.'))
        Troco = float("{:.2f}".format(TrocoFloat - Total))

        Troco = str(Troco)
        Troco = str(Troco.replace('.', ','))

        return Troco


