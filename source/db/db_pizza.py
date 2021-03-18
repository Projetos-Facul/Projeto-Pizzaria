"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Realizar inserção no banco de dados com passagem de parametos, minimizando codigo.
Arquivo.....: db_pizza.py - Inserção padrão em tabelas no banco de dados
Autor.......: Mateus Pompermayer
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

#Funcao para inserir pizza
def Insert(pizza):
    cursor, connection = tables.chamada_db('nao')
    cursor.execute("INSERT INTO pizza(nome, tipo, data_criacao, ingredientes, valor_custo) \
                        values (:nome, :tipo, :datacriacao, :ingredientes, :valorcusto)", pizza)
    connection.commit()
    connection.close()
    return print('          ***** Pizza  Adicionada *****')

####################################################################################################################################################################################################################################################

#Funcao para alterar pizza
def Update(pizzaupdate, inativacao):
    cursor, connection = tables.chamada_db('nao')

    if inativacao == True:
        cursor.execute("UPDATE pizza \
                       set nome = ?, tipo = ?, ingredientes = ?, valor_custo = ?, data_inativacao = ? \
                       where id_pizza = ?",
                       (pizzaupdate[0], pizzaupdate[1], pizzaupdate[2], pizzaupdate[3], None, pizzaupdate[4]))
    else:
        cursor.execute("UPDATE pizza \
                       set nome = ?, tipo = ?, ingredientes = ?, valor_custo = ? \
                       where id_pizza = ?", (pizzaupdate[0], pizzaupdate[1], pizzaupdate[2], pizzaupdate[3], pizzaupdate[4]))

    connection.commit()
    connection.close()

    print('\n          ***** Pizza Alterada *****')

####################################################################################################################################################################################################################################################

#Funcao para mostrar dados da pizza
def Select(PizzaCodigo, bool, select):
    cursor, connection = tables.chamada_db('nao')
    if select == True:
        cursor.execute("SELECT id_pizza, tipo, nome, ingredientes, valor_custo, data_inativacao from pizza where id_pizza = ?", (PizzaCodigo,) )
        pizza = cursor.fetchone()  # retrieve the first row
        connection.close()
        if pizza == None:
            return print('\n      ***** Nenhuma pizza encontrada *****')
        else:
            return pizza
    else:
        if bool == 'Uma':
            cursor.execute("SELECT id_pizza, tipo, nome, ingredientes, valor_custo, data_criacao from pizza where id_pizza = ? and data_inativacao is null", (PizzaCodigo,) )
            pizza = cursor.fetchone()  # retrieve the first row
            if pizza == None:
                connection.close()
                return print('\n      ***** Nenhuma pizza encontrada *****')
            else:
                print('\n      Pizza Selecionada..:', pizza[2])
                connection.close()
                return print('\n      Id............:', pizza[0], '\n' , '     Tipo..........:', pizza[1], '\n', '     Nome..........:', pizza[2], '\n', '     Ingredientes..:', pizza[3],
                          '\n', '     Valor Custo...: R$', pizza[4], '\n', '     Data Criação..:', pizza[5])  # Imprime o primeiro campo
        elif bool == 'Todas':
            cursor.execute("SELECT id_pizza, tipo, nome, ingredientes, valor_custo, data_criacao from pizza where data_inativacao is null")
            pizzas = cursor.fetchall()  # retrieve the first row

            print('\n             ***** Todas Pizzas *****\n')
            if pizzas == None:
                connection.close()
                return print('\n      ***** Nenhuma pizza encontrada *****')
            else:
                for pizza in pizzas:
                 pizzas = [print('      Id............:', pizza[0], '\n' , '     Tipo..........:', pizza[1], '\n', '     Nome..........:', pizza[2], '\n', '     Ingredientes..:', pizza[3],
                          '\n', '     Valor Custo...: R$', pizza[4], '\n', '     Data Criação..:', pizza[5])]
                 print('\n')
                connection.close()
                return pizzas

        elif bool == 'Desativadas':
            cursor.execute("SELECT id_pizza, tipo, nome, ingredientes, valor_custo, data_criacao from pizza where data_inativacao is not null")
            pizzas = cursor.fetchall()  # retrieve the first row

            if pizzas == []:
                connection.close()
                return print('\n      ***** Nenhuma pizza encontrada *****')
            else:
                print('\n        ***** Pizzas  Desativadas *****\n')
                for pizza in pizzas:
                 pizzas = [print('      Id............:', pizza[0], '\n', '     Tipo..........:', pizza[1], '\n', '     Nome..........:', pizza[2], '\n', '     Ingredientes...:', pizza[3],
                          '\n', '     Valor Custo...: R$', pizza[4], '\n', '     Data Criação..:', pizza[5])]
                 print('\n')
                connection.close()
                return pizzas

##################################################################################################################################################################################################################################################

#Funcao para deletar(desativar) pizza
def Delete(data, PizzaCodigo):
    cursor, connection = tables.chamada_db('nao')
    cursor.execute("UPDATE pizza \
                    set data_inativacao = ? \
                    where id_pizza = ?", (data, PizzaCodigo,))
    connection.commit()
    connection.close()
    return print('\n          ***** Pizza Desativada *****')

##################################################################################################################################################################################################################################################

#Funcao para excluir todas as pizzas, e depois incluir as padroes
def create_db_pizza():
    cursor, connection = tables.chamada_db('nao')

    cursor.execute("DELETE FROM pizza")
    connection.commit()

    cursor.execute("DELETE FROM SQLITE_SEQUENCE where name = 'pizza'")
    connection.commit()

    data = library.Datetime_fmt('YYYY-MM-DD HH:MM:SS.MS')

    lista_pizza = [('Salgada', 'ALHO E ÓLEO', 'Alho frito picado, parmesão ralado e azeitonas', '22,90', data),
                    ('Salgada', 'ALLICI', 'Alicci importado, rodelas de tomate, parmesão e azeitonas', '28,90', data),
                    ('Salgada', 'ATUM', 'Atum, cebola e azeitona', '22,90', data),
                    ('Salgada', 'BACON', 'Bacon coberto com muzzarela e azeitonas', '26,90', data),
                    ('Salgada', 'BERINJELA', 'Berinjela, cobertura com muzzarela, manjericão e parmesão', '23,90', data),
                    ('Salgada', 'CAIPIRA', 'Frango desfiado, coberto com catupiry e milho verde e azeitonas','26,90', data),
                    ('Salgada', 'CALABRESA', 'Linguiça calabresa, cebola e azeitonas', '19,90', data),
                    ('Salgada', 'CINCO QUEIJOS', 'Muzzarela, parmesão, catupiry, gorgonzola e provolone', '29,90', data),
                    ('Salgada', 'ESCAROLA', 'Escarola refogada, muzzarela e azeitonas', '24,90', data),
                    ('Salgada', 'EXECUTIVA', 'Milho Verde, catupiry e azeitonas', '22,90', data),
                    ('Salgada', 'PERUANA', 'Atum, cebola, muzzarela e azeitonas', '26,90', data),
                    ('Salgada', 'PALMITO', 'Palmito com muzzarela e azeitonas', '26,90', data),
                    ('Doce', 'BANANA', 'Banana fatiada com, cobertura com leite condensado e canela em pó', '21,90', data),
                    ('Doce', 'BRIGADEIRO', 'Chocolate, leite condensado e chocolate granulado', '23,90', data),
                    ('Doce', 'PRESTIGIO', 'Chocolate coberta com côco', '23,90', data)]

    cursor.executemany("INSERT INTO pizza(tipo, nome, ingredientes, valor_custo, data_criacao) \
                                values (:tipo, :nome, :ingredientes, :valorcusto, :data);", lista_pizza)
    connection.commit()
    connection.close()

