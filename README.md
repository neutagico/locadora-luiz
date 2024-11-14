Locadora_Luiz - Sistema de Locadora de Filmes
Este é um sistema simples de gestão de filmes para uma locadora. Ele permite realizar operações como listar, adicionar, pesquisar, remover e consultar a quantidade de filmes disponíveis no banco de dados.

Requisitos
Python 3.x
Biblioteca mysql-connector (ou outra biblioteca de sua escolha para se conectar ao MySQL)
Banco de dados MySQL configurado (nome do banco de dados: locadora_luiz)
Arquitetura
O código está dividido em dois módulos principais:

metodos_locadora.py: Contém os métodos responsáveis pelas operações relacionadas aos filmes, como listar, adicionar, pesquisar, remover e consultar a quantidade.
operacoesbd.py: Contém os métodos de interação com o banco de dados, como criar a conexão e encerrar a conexão com o banco.
Estrutura do Projeto
plaintext
Copiar código
locadora_luiz/
│
├── metodos_locadora.py        # Métodos de gerenciamento de filmes
├── operacoesbd.py             # Métodos para interação com o banco de dados
└── main.py                    # Arquivo principal que executa o sistema
└── README.md                  # Este arquivo
Como Usar
1. Configuração do Banco de Dados
Antes de rodar o sistema, é necessário configurar o banco de dados MySQL.

Crie o banco de dados locadora_luiz.
Crie as tabelas necessárias para armazenar informações sobre filmes (certifique-se de que existam tabelas com campos como id, titulo, ano, quantidade, etc.).
2. Configuração da Conexão
No arquivo main.py, a linha de conexão com o banco de dados é:

python
Copiar código
conexao = criarConexao('127.0.0.1', 'root', 'luiz310303', 'locadora_luiz')
Certifique-se de alterar os parâmetros de conexão ('127.0.0.1', 'root', 'luiz310303', 'locadora_luiz') de acordo com sua configuração de banco de dados.

3. Execução do Sistema
Execute o arquivo main.py para iniciar o sistema de gerenciamento de filmes. O programa apresentará um menu com as seguintes opções:

Listar Filmes: Exibe todos os filmes cadastrados no banco de dados.
Adicionar Filme: Permite adicionar um novo filme ao banco de dados.
Pesquisar Filme: Permite pesquisar um filme pelo código (ID) no banco de dados.
Remover Filme: Remove um filme do banco de dados.
Quantidade de Filmes: Exibe a quantidade total de filmes cadastrados no banco de dados.
Sair: Encerra o programa.
4. Funções
Listar Filmes
A função listarfilmes exibe todos os filmes cadastrados no banco de dados.

python
Copiar código
def listarfilmes(conexao):
    lista = listarBancoDados(conexao, "select * from filmes")

    if len(lista) > 0:
        print("Lista de Filmes")
        for item in lista:
            print(item[0], '-', item[1], '-', item[2], '-', item[3])
    else:
        print("Não existem filmes a serem exibidos!")
Adicionar Filme
A função adicionarfilmes permite adicionar um novo filme ao banco de dados, fornecendo o nome, sinopse e ano do filme.

python
Copiar código
def adicionarfilmes(conexao):
    nome = input("Digite o nome do filme a ser adicionado: ")
    sinopse = input("Digite a sinopse do filme: ")
    ano = input("Digite o ano do filme: ")

    consutainserir = "insert into filmes(nome, sinopse, ano) values(%s, %s, %s)"
    values = [nome, sinopse, ano]

    insertNoBancoDados(conexao, consutainserir, values)

    print("Filme adicionado com sucesso")
Pesquisar Filme pelo Código
A função pesquisarcodigo permite pesquisar um filme no banco de dados pelo código (ID).

python
Copiar código
def pesquisarcodigo(conexao):
    codigopesquisa = input("Digite o código: ")

    consultapesquisar = "select * from filmes where codigo = %s"
    dados = [codigopesquisa]

    filmes = listarBancoDados(conexao, consultapesquisar, dados)
    if len(filmes) > 0:
        print(filmes[0][1], "-", filmes[0][2], "-", filmes[0][3])
    else:
        print("Não existe!")
Remover Filme
A função removerfilmes permite remover um filme do banco de dados com base no código.

python
Copiar código
def removerfilmes(conexao):
    consultacodigo = int(input("Digite o código para deletar: "))

    consutadeletar = "delete from filmes where codigo = %s"
    valores = [consultacodigo]

    linhasafetadas = excluirBancoDados(conexao, consutadeletar, valores)

    if linhasafetadas > 0:
        print("Filme removido com sucesso!")
    else:
        print("Não existe o código!")
Consultar Quantidade de Filmes
A função quantidadefilmes consulta e exibe a quantidade total de filmes cadastrados no banco de dados.

python
Copiar código
def quantidadefilmes(conexao):
    consultaquantidade = "select count(*) from filmes"

    listagem = listarBancoDados(conexao, consultaquantidade)
    quantidade = listagem[0][0]
    print("Atualmente temos", quantidade, "filme(s)")
Código de Integração com MySQL
Aqui estão as funções que fazem a integração com o MySQL, permitindo realizar operações como conexão, inserção, listagem, atualização e exclusão de dados no banco de dados.

Criar Conexão
A função criarConexao estabelece a conexão com o banco de dados MySQL usando as credenciais fornecidas.

python
Copiar código
import mysql.connector

# Inicializa a conexão com o banco de dados
def criarConexao(endereco, usuario, senha, bancodedados):
    try:
        return mysql.connector.connect(
            host=endereco,
            user=usuario,
            password=senha,
            database=bancodedados
        )
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
Encerrar Conexão
A função encerrarConexao encerra a conexão com o banco de dados.

python
Copiar código
# Encerra a conexão com o banco de dados
def encerrarConexao(connection):
    if connection:
        connection.close()
Inserir Dados no Banco
A função insertNoBancoDados insere dados no banco de dados utilizando prepared statements e tratamento de exceções.

python
Copiar código
# Insere dados no banco de dados com prepared statements e tratamento de exceções
def insertNoBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        id = cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Erro ao inserir no banco de dados: {err}")
        connection.rollback()  # Reverte a transação em caso de erro
        return None
    finally:
        cursor.close()
    return id
Listar Dados do Banco
A função listarBancoDados recupera dados do banco de dados, tratando exceções durante a execução.

python
Copiar código
# Lista dados do banco de dados com tratamento de exceções
def listarBancoDados(connection, sql, params=None):
    try:
        cursor = connection.cursor(prepared=True)
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro ao listar do banco de dados: {err}")
        return []
    finally:
        cursor.close()
    return results
Atualizar Dados no Banco
A função atualizarBancoDados atualiza registros no banco de dados.

python
Copiar código
# Atualiza dados no banco de dados com tratamento de exceções
def atualizarBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        linhasAfetadas = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar o banco de dados: {err}")
        connection.rollback()  # Reverte a transação em caso de erro
        return 0
    finally:
        cursor.close()
    return linhasAfetadas
Excluir Dados no Banco
A função excluirBancoDados exclui dados do banco de dados com base em uma consulta.

python
Copiar código
# Exclui dados no banco de dados com tratamento de exceções
def excluirBancoDados(connection, sql, dados):
    try:
        cursor =
