from utils import * # pega tudo que existe no arquivo utils.py.
import random # importa a biblioteca random para gerar números aleatórios, usada para criar IDs únicos para filmes, livros e HQs cadastrados


def gerar_id():
    return random.randint(1000, 9999)  # função que gera um número aleatório entre 1000 e 9999, usado para criar IDs únicos para filmes, livros e HQs cadastrados


# ================= CADASTROS =================

def cadastro_filme():
    filme = {}

    filme["id"] = gerar_id()
    filme["titulo"] = input("Digite o título do filme: ")
    filme["diretor"] = input("Digite o diretor: ")
    filme["ano"] = input("Digite o ano: ")

    lista_filme.append(filme)

    print("\nFilme cadastrado com sucesso!")
    print(filme)


def cadastro_livro():
    livro = {}

    livro["id"] = gerar_id()
    livro["titulo"] = input("Digite o título do livro: ")
    livro["autor"] = input("Digite o autor: ")
    livro["ano"] = input("Digite o ano: ")

    lista_livro.append(livro)

    print("\nLivro cadastrado com sucesso!")
    print(livro)


def cadastro_usuario():
    usuario = {}

    usuario["id"] = gerar_id()
    usuario["nome"] = input("Digite o nome do usuário: ")

    email = input("Digite o email: ")

    if "@" in email and ".com" in email:
        usuario["email"] = email
    else:
        print("Email inválido!")
        return

    senha = input("Digite a senha: ")

    if len(senha) >= 6:
        usuario["senha"] = senha
    else:
        print("Senha inválida! Precisa ter pelo menos 6 caracteres.")
        return

    usuario["divida"] = 0.0

    lista_usuario.append(usuario)

    print("\nUsuário cadastrado com sucesso!")
    print(usuario)


# ================= VER CADASTROS =================

def ver_filmes():
    print("\n--- FILMES CADASTRADOS ---")

    for filme in lista_filme:
        print(filme)


def ver_livros():
    print("\n--- LIVROS CADASTRADOS ---")

    for livro in lista_livro:
        print(livro)


def ver_usuarios():
    print("\n--- USUÁRIOS CADASTRADOS ---")

    for usuario in lista_usuario:
        print(usuario)


# ================= APAGAR DÍVIDA =================

def apagar_divida():
    nome = input("Digite o nome do usuário: ")

    for usuario in lista_usuario:
        if usuario["nome"] == nome:
            usuario["divida"] = 0.0
            print("Dívida apagada com sucesso!")
            return

    print("Usuário não encontrado!")


# ================= ESTOQUE EM PILHA =================

def adicionar_estoque():
    print("""
1 - Fita
2 - Comida
3 - Merch
4 - Videocassete
""")

    opcao = input("Escolha o tipo de item: ")
    item = input("Digite o nome do item: ")

    if opcao == "1":
        estoque_fitas.append(item)
        print("Fita adicionada!")

    elif opcao == "2":
        estoque_comidas.append(item)
        print("Comida adicionada!")

    elif opcao == "3":
        estoque_merch.append(item)
        print("Merch adicionado!")

    elif opcao == "4":
        estoque_videocassete.append(item)
        print("Videocassete adicionado!")

    else:
        print("Opção inválida!")


def remover_estoque():
    print("""
1 - Fita
2 - Comida
3 - Merch
4 - Videocassete
""")

    opcao = input("Escolha o estoque: ")

    if opcao == "1":
        if len(estoque_fitas) > 0:
            item = estoque_fitas.pop()
            print("Item removido:", item)
        else:
            print("Estoque vazio!")

    elif opcao == "2":
        if len(estoque_comidas) > 0:
            item = estoque_comidas.pop()
            print("Item removido:", item)
        else:
            print("Estoque vazio!")

    elif opcao == "3":
        if len(estoque_merch) > 0:
            item = estoque_merch.pop()
            print("Item removido:", item)
        else:
            print("Estoque vazio!")

    elif opcao == "4":
        if len(estoque_videocassete) > 0:
            item = estoque_videocassete.pop()
            print("Item removido:", item)
        else:
            print("Estoque vazio!")

    else:
        print("Opção inválida!")


def ver_estoque():
    print("\n--- ESTOQUE DE FITAS ---")
    print(estoque_fitas)

    print("\n--- ESTOQUE DE COMIDAS ---")
    print(estoque_comidas)

    print("\n--- ESTOQUE DE MERCH ---")
    print(estoque_merch)

    print("\n--- ESTOQUE DE VIDEOCASSETE ---")
    print(estoque_videocassete)


# ================= COMPRA / ALUGUEL =================

def compra_aluguel():
    nome = input("Nome do usuário: ")
    item = input("Nome do item: ")

    print("""
1 - Comprar
2 - Alugar
""")

    opcao = input("Escolha: ")

    registro = {}

    registro["usuario"] = nome
    registro["item"] = item

    if opcao == "1":
        registro["tipo"] = "Compra"
        print("Compra feita com sucesso!")

    elif opcao == "2":
        registro["tipo"] = "Aluguel"
        registro["status"] = "Alugado"
        print("Aluguel feito com sucesso!")

    else:
        print("Opção inválida!")
        return

    compras_alugueis.append(registro)


# ================= DEVOLUÇÃO =================

def devolucao():
    nome_item = input("Digite o nome do item para devolver: ")

    for registro in compras_alugueis:
        if registro["item"] == nome_item and registro["tipo"] == "Aluguel":
            registro["status"] = "Devolvido"
            print("Item devolvido com sucesso!")
            return

    print("Aluguel não encontrado!")


# ================= IFOOD DE FITA =================

def ifood_fita():
    filme = input("Qual fita você quer receber em casa? ")
    endereco = input("Digite seu endereço: ")

    pedido = {}

    pedido["filme"] = filme
    pedido["endereco"] = endereco
    pedido["status"] = "Saiu para entrega"

    print("\nPedido feito com sucesso!")
    print(pedido)
