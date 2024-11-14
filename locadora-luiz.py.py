from metodos_locadora import *
from operacoesbd import *

opcao = 3

conexao = criarConexao('127.0.0.1','root','luiz310303','locadora_luiz')

while opcao != 6:
    print("1)listar\n2)adicionar\n3)pesquisar\n4)remover\n5)quantidade\n6)sair")
    opcao = int(input("digite sua opcao: "))
    if opcao == 1:
        listarfilmes(conexao)
    elif opcao == 2:
        adicionarfilmes(conexao)
    elif opcao == 3:
        pesquisarcodigo(conexao)
    elif opcao == 4:
     removerfilmes(conexao)
    elif opcao == 5:
     quantidadefilmes(conexao)
    elif opcao != 6:
        print("codigo invalido")

encerrarConexao(conexao)

print("obrigado por usar a locadora_luiz")