"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Realizar inserção no banco de dados com passagem de parametos, minimizando codigo.
Arquivo.....: db_report.py - Inserção padrão em tabelas no banco de dados
Autor.......: Mateus Pompermayer / Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Insert - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Update - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Select - Versao 1.00
              2020-05-13 - [R00] Criação da funcao Delete - Versao 1.00
              ...
"""
import os
from source.db.database import tables
from source.lib import library

def Select(Tabela, inicio, fim):
    cursor, connection = tables.chamada_db('nao')

    if Tabela == 'Pizza':
        cursor.execute("SELECT id_pizza, tipo, nome, ingredientes, valor_custo, data_criacao from pizza where data_inativacao is null")
        pizzas = cursor.fetchall()
        if pizzas == None:
            connection.close()
            return print('\n      ***** Nenhuma pizza encontrada *****')
        else:
            connection.close()
            return pizzas

    elif Tabela == 'Pedido':
        cursor.execute("SELECT inf_pedido.pizza, inf_pedido.tamanho, inf_pedido.qtd, pedido.id_pedido, pedido.data_inicio, pedido.hora, pedido.total_pedido, pedido.troco_pedido, \
                                            user.nome, user.tel_fix, Inteira.nome, MeiaUm.nome, MeiaDois.nome  FROM pedido \
                                            LEFT JOIN inf_pedido ON pedido.id_pedido = inf_pedido.id_pedido \
                                            LEFT JOIN user ON pedido.id_user = user.id_user \
                                            LEFT JOIN pizza AS Inteira ON inf_pedido.id_pizza_inteira = Inteira.id_pizza \
                                            LEFT JOIN pizza AS MeiaUm ON inf_pedido.id_pizza_meia_um = MeiaUm.id_pizza \
                                            LEFT JOIN pizza AS MeiaDois ON inf_pedido.id_pizza_meia_dois = MeiaDois.id_pizza \
                                            WHERE pedido.data_inicio BETWEEN :inicio AND :fim \
                                            ORDER BY pedido.data_inicio ASC", (inicio, fim))
        pedidos = cursor.fetchall()  # retrieve the first row

        if pedidos == []:
            connection.close()
            return print("\n       **** Nenhum pedido encontrado ****")
        else:
            print("\n")
            for pedido in pedidos:
                if pedido[0] == 'Meia':
                    print('      Id Pedido....:', pedido[3], '\n', '     Data.........:', pedido[4], '\n',
                          '     Hora Entrega.:', pedido[5], '\n', '     Total........: R$', pedido[6],
                          '\n', '     Troco........: R$', pedido[7], '\n', '     Cliente......:', pedido[8],
                          '\n',
                          '     Telefone.....:', pedido[9], '\n', '     Pizza........:', pedido[0],
                          '\n', '     Tamanho......:', pedido[1], '\n', '     Quantidade...:', pedido[2], '\n',
                          '     Meia 1/2.....:', pedido[11], '\n', '     Meia 2/2.....:', pedido[12])

                elif pedido[0] == 'Inteira':
                    print('      Id Pedido....:', pedido[3], '\n', '     Data.........:', pedido[4], '\n',
                          '     Hora Entrega.:', pedido[5], '\n', '     Total........: R$', pedido[6],
                          '\n', '     Troco........: R$', pedido[7], '\n', '     Cliente......:', pedido[8],
                          '\n',
                          '     Telefone.....:', pedido[9], '\n', '     Pizza........:', pedido[0],
                          '\n', '     Tamanho......:', pedido[1], '\n', '     Quantidade...:', pedido[2], '\n',
                          '     Inteira......:', pedido[10], '\n')

                print('\n')
            connection.close()
            return pedidos

    elif Tabela == 'Total':
        cursor.execute("SELECT total_pedido, id_pedido FROM pedido \
                         WHERE pedido.data_inicio BETWEEN :inicio AND :fim \
                        ORDER BY pedido.data_inicio ASC", (inicio, fim))
        total = cursor.fetchall()  # retrieve the first row

        if total == []:
            connection.close()
            return print("\n       **** Nenhum pedido encontrado ****")
        else:
            connection.close()
            return total

def user_data(inicio, fim):
    cursor, connection = tables.chamada_db('nao')

    cursor.execute("SELECT * from user where data_criacao >= ? and data_criacao <= ?", (inicio, fim))
    user = cursor.fetchall()

    return user


