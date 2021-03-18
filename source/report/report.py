"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Arquivo main para relatorios.
Arquivo.....: report.py - Arquivo padrão para relatorios
Autor.......: Vinicius Guedes / Mateus Pompermayer
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-10 - [R01] Criação da função Menu_Relatorio - Versao 1.00
              ...
"""

from source.db import db_report
from source.db import db_pizza
from source.lib import library
from source import user
from source.db import db_user


def Menu_Relatorio ():
    opcao = 1
    while opcao != 0:
        try:
            print('\n****************** RELATORIOS ******************')
            print('   [1] - Cliente')
            print('   [2] - Cliente Parametrizado')
            print('   [3] - Pedidos')
            print('   [4] - Pizza')
            print('   [5] - Pizza - Maior receita')
            print('   [6] - Pizza - Menor receita')
            print('   [0] - Voltar')
            opcao = int(input('Digite a opção desejada: '))
            if not 0 <= opcao <= 6:
                raise ValueError("\n           ***** Valor Inválido *****")
        except ValueError as e:
            print("\n           ***** Valor Inválido *****")
        else:
            if opcao == 1:
                report_user('padrao')
            elif opcao == 2:
                report_user('parametro')
            elif opcao == 3:
                report_pedido()
            elif opcao == 4:
                report_pizza()
            elif opcao == 5:
                ReceitaPizza('Maior')
            elif opcao == 6:
                ReceitaPizza('Menor')


def ReceitaPizza(Tamanho):
    pizzas = db_report.Select('Pizza', None, None)

    if Tamanho == 'Maior':
        print('\n            ***** Maior  Receita ***** ')

        if pizzas != None:
            num = len(pizzas)

            for i in range(num):
                ref = float(pizzas[i][4].replace(',', '.'))
                if i == 0:
                    maior = ref
                elif ref > maior:
                    maior = ref

            for i in range(num):
                ref = float(pizzas[i][4].replace(',', '.'))
                if ref == maior:
                    print("\n     ID.......:", pizzas[i][0])
                    print("     Nome.....:", pizzas[i][1])
                    print("     Tipo.....:", pizzas[i][2])
                    print("     Valor....:", ref)

        else:
            print('Nenhuma Receita Encontrada!')

    elif Tamanho == 'Menor':
        print('\n            ***** Menor  Receita ***** ')

        if pizzas != None:
            num = len(pizzas)

            for i in range(num):
                ref = float(pizzas[i][4].replace(',', '.'))
                if i == 0:
                    menor = ref
                elif ref < menor:
                    menor = ref

            for i in range(num):
                ref = float(pizzas[i][4].replace(',', '.'))
                if ref == menor:
                    print("\n     ID.......:", pizzas[i][0])
                    print("     Nome.....:", pizzas[i][1])
                    print("     Tipo.....:", pizzas[i][2])
                    print("     Valor....:", ref)

        else:
            print('Nenhuma Receita Encontrada!')

def report_user(ref):
    usuario = db_user.select(4, 'tudo')
    if usuario == []:
        print("\n     ***** Nenhum Cadastro Encontrado *****")
    else:
        if ref == "padrao":
            for row in usuario:
                user.Exibir_Select(row, 1)
        elif ref == "parametro":
            print("\n           ***** Buscando Cliente *****")
            print("\nFormato de pesquisa YYYY-MM-DD")
            inicio = input("     Data Inicio....: ")
            fim = input("     Data Fim.......: ")

            usuario = db_report.user_data(inicio, fim)

            if usuario == None or usuario == []:
                print("\n     ***** Nenhum Cadastro Encontrado *****")
            else:
                for i in usuario:
                    user.Exibir_Select(i, 1)

#Funcao para relatorio das pizzas, mostrando todas pizzas com valores media, grande e gigante
def report_pizza():
    pizzas = db_report.Select('Pizza', None, None)
    if pizzas != None:
        for pizza in pizzas:
            if type(pizza[4]) == str:
                ValorMedia = library.Calcular_Valor("Media", float(pizza[4].replace(',', '.')), 1)
                ValorGrande = library.Calcular_Valor("Grande", float(pizza[4].replace(',', '.')), 1)
                ValorGigante = library.Calcular_Valor("Gigante", float(pizza[4].replace(',', '.')), 1)
            elif float(pizza[4]).is_integer():
                ValorMedia = library.Calcular_Valor("Media", float(pizza[4]), 1)
                ValorGrande = library.Calcular_Valor("Grande", float(pizza[4]), 1)
                ValorGigante = library.Calcular_Valor("Gigante", float(pizza[4]), 1)
            print('\n      Id............:', pizza[0], '\n', '     Tipo..........:', pizza[1], '\n',
                  '     Nome..........:', pizza[2], '\n', '     Ingredientes..:', pizza[3],
                  '\n', '     Valor Custo...: R$', pizza[4], '\n', '     Valor Media...: R$',
                  ValorMedia[0],  '\n', '     Valor Grande..: R$', ValorGrande[0], '\n',
                  '     Valor Gigante.: R$', ValorGigante[0], '\n', '     Data Criação..:', pizza[5])

#Funcao para relatorio dos pedidos, mostrando todos pedidos parametrizados pela data, e mostrando o total desses pedidos
def report_pedido():
    print("\n           ***** Buscando Pedidos *****")
    print("\nFormato de pesquisa YYYY-MM-DD")
    inicio = input("     Data Inicio....: ")
    fim = input("     Data Fim.......: ")
    pedidos = db_report.Select('Pedido', inicio, fim)
    total = db_report.Select('Total', inicio, fim)
    Total = report_total(total)
    print(f'       *** TOTAL GERAL ENTRE AS DATAS *** \n  *** {inicio} e {fim}.: R$ {Total} ***')

#Funcao para relatorio das pizzas, calculando o total dos pedidos da data escolhida na funcao report_pedido
def report_total(Valores):
    Total = 0
    for Valor in Valores:
        ValorFloat = float(Valor[0].replace(',', '.'))
        Total = float("{:.2f}".format(Total + ValorFloat))

    Total = str(Total)
    Total = str(Total.replace('.', ','))

    return Total