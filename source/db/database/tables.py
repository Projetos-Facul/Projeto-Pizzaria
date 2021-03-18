"""
Data.Criacao: 2020-05-08
Projeto.....: Projeto_Pizzaria
Descricao...: Arquivo para criar banco de dados
Arquivo.....: tables.py - Criação das Tabelas do banco
Autor.......: Vinicius Guedes
Observações.: 2020-05-12 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-12 - [R01] Criação do database pizzaria - Versao 1.00
              2020-05-12 - [R02] Criação da tabela pizza - Versao 1.00
              ...
"""

import os
import sqlite3
from source.db import db_pizza


def chamada_db(new):
    # definindo um arquivo
    fileDB = 'C:\\Users\\vinip\\Documents\\Facul\\3SEM\\Saito\\Pyton\\Projeto_Pizzaria\\source\\db\\database\\db_pizzaria.sqlite'

    # verificando se arquivo de banco de dados existe
    if not os.path.exists(fileDB) and new != 'new':
        return 0
    else:
        if new == 'new' and os.path.exists(fileDB):
            os.remove(fileDB)

    #Criando a base de dados
    connection = sqlite3.connect(fileDB)

    # Get a cursor object
    return connection.cursor(), connection

#Criacao de tabelas
def create_table():
    cursor, connection = chamada_db('new')

    #Criação da tabela pizza
    cursor.execute('CREATE TABLE IF NOT EXISTS pizza \
                       (id_pizza INTEGER PRIMARY KEY AUTOINCREMENT, \
                        tipo    varchar(40), \
                        nome  varchar(80), \
                        ingredientes varchar(180), \
                        valor_custo decimal(10,2), \
                        data_criacao datetime, \
                        data_inativacao datetime )'
                   )

    # Criação da tabela cliente
    cursor.execute('CREATE TABLE IF NOT EXISTS user \
                           (id_user INTEGER PRIMARY KEY AUTOINCREMENT, \
                            nome varchar(40), \
                            tel_fix varchar(15), \
                            tel_cel varchar(15), \
                            cep varchar(15), \
                            endereco varchar(25), \
                            numero varchar(8), \
                            complemento varchar(15), \
                            bairro varchar(15), \
                            cidade varchar(15), \
                            uf varchar(2), \
                            data_criacao datetime)')

    # Criação da tabela pedido
    cursor.execute('CREATE TABLE IF NOT EXISTS pedido \
                              (id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, \
                               id_user INTERGER, \
                               data_inicio date, \
                               hora datetime, \
                               troco_pedido decimal(10,2), \
                               total_pedido decimal(10,2), \
                               status boolean)')

    cursor.execute('CREATE TABLE IF NOT EXISTS inf_pedido \
                                  (id_item INTEGER PRIMARY KEY AUTOINCREMENT, \
                                   id_pedido INTEGER, \
                                   pizza varchar(7), \
                                   id_pizza_inteira INTERGER, \
                                   id_pizza_meia_um INTERGER, \
                                   id_pizza_meia_dois INTERGER, \
                                   tamanho varchar(15), \
                                   qtd float , \
                                   valor_unit float, \
                                   sub_total float )')

    db_pizza.create_db_pizza()
    connection.close()
