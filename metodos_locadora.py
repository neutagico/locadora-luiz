from operacoesbd import *

def listarfilmes(conexao):
    lista = listarBancoDados(conexao, "select * from filmes")

    if len(lista) > 0:
            print("lista de filmes")
            for item in lista:
                print(item[0], '-', item[1], '-', item[2], '-', item[3])
    else:
            print("nao existem filmes a serem exibidos!")


def adicionarfilmes(conexao):
    nome = input("digite o nome do filme a ser adicionado: ")
    sinopse = input("digite a sinopse do filme: ")
    ano = input("digite o ano do filme: ")

    consutainserir = "insert into filmes(nome,sinopse,ano)values(%s,%s,%s)"

    values = [nome, sinopse, ano]
    insertNoBancoDados(conexao, consutainserir, values)

    print("filme adicionado com sucesso")

def pesquisarcodigo(conexao):
    codigopesquisa = input("digite o codigo: ")

    consultapesquisar = "select * from filmes where codigo = %s"
    dados = [codigopesquisa]

    filmes = listarBancoDados(conexao, consultapesquisar, dados)
    if len(filmes) > 0:
        print(filmes[0][1], "-", filmes[0][2], "-", filmes[0][3])

    else:
        print("nao existe!")

def removerfilmes(conexao):
    consultacodigo = int(input("digite o codigo pra deletar: "))

    consutadeletar = " delete from filmes where codigo = %s "
    valores = [consultacodigo]

    linhasafetadas = excluirBancoDados(conexao, consutadeletar, valores)

    if linhasafetadas > 0:
        print("filme removido com sucesso!")
    else:
        print("nao existe o codigo!")


def quantidadefilmes(conexao):

        consultaquantidade = "select count(*) from filmes"

        listagem = listarBancoDados(conexao, consultaquantidade)
        quantidade = listagem[0][0]
        print("atualmente temos", quantidade, "filme(s)")


