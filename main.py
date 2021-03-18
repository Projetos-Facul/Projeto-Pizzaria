"""
Data.Criacao: 2020-05-10
Projeto.....: Projeto Pizzaria
Descricao...: Arquivo padrão.
Arquivo.....: main.py - Arquivo padrão do projeto
Autor.......: Vinicius Guedes
Observações.: 2020-05-10 - [R00] Criação do Arquivo - Versao 1.00
              2020-05-10 - [R01] Criação do Main - Versao 1.00
              2020-05-18 - [R02] Mudança no Main, abertura e confirmação do arquivo do banco- Versao 1.00
              ...
"""

from source.lib import library
from source.db.database import tables

def main():
    #Confirmação do arquivo do banco
    connection = tables.chamada_db('nao')
    if connection == 0:
        tables.create_table()

    #Chamada no Library para os menus de projeto
    library.Menu_Inicial()

if __name__ == '__main__':  # chamada da funcao principal
    main()
