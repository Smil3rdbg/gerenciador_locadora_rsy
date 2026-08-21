from tarefas import *
from utils import *


def menu():
    while True:
        print("""
====================================
          SISTEMA LOCADORA
====================================

🎬 FILMES
1  - Cadastrar filme
2  - Ver filmes
3  - Apagar filme
4  - Alterar dados do filme
5  - Alugar filme
6  - Devolver filme
7  - Estoque de filmes

📚 LIVROS
8  - Cadastrar livro
9  - Ver livros
10 - Apagar livro
11 - Alterar dados do livro
12 - Alugar livro
13 - Devolver livro
14 - Estoque de livros

📖 HQ'S
15 - Cadastrar HQ
16 - Ver HQs
17 - Apagar HQ
18 - Alterar dados da HQ
19 - Alugar HQ
20 - Devolver HQ
21 - Estoque de HQs

👤 CLIENTES
22 - Cadastrar cliente
23 - Ver clientes
24 - Login
25 - Reservar item
26 - Devolver item

0  - Sair
""")

        try:
            opcao = int(input("Selecione uma opção: "))
        except ValueError:
            print("\nOpção inválida! Digite apenas números.\n")
            continue

        if opcao == 0:
            print("\nPrograma encerrado!")
            break

        elif opcao == 1:
            cadastro_filme(lista_filme)

        elif opcao == 2:
            ver_infos_filme(lista_filme)

        elif opcao == 3:
            apagar_cadastrofilme(lista_filme)

        elif opcao == 4:
            modificar_cadastrofilme(lista_filme)

        elif opcao == 5:
            alugar_filme(lista_filme)

        elif opcao == 6:
            devolucao_filme(lista_filme)

        elif opcao == 7:
            controle_estoque_filme(lista_filme)

        elif opcao == 8:
            cadastro_livro(lista_livro)

        elif opcao == 9:
            ver_infos_livro(lista_livro)

        elif opcao == 10:
            apagar_cadastrolivro(lista_livro)

        elif opcao == 11:
            modificar_cadastrolivro(lista_livro)

        elif opcao == 12:
            alugar_livro(lista_livro)

        elif opcao == 13:
            devolucao_livro(lista_livro)

        elif opcao == 14:
            controle_estoque_livro(lista_livro)

        elif opcao == 15:
            cadastro_hq(lista_hq)

        elif opcao == 16:
            ver_infos_hq(lista_hq)

        elif opcao == 17:
            apagar_cadastrohq(lista_hq)

        elif opcao == 18:
            modificar_cadastrohq(lista_hq)

        elif opcao == 19:
            alugar_hq(lista_hq)

        elif opcao == 20:
            devolucao_hq(lista_hq)

        elif opcao == 21:
            controle_estoque_hq(lista_hq)

        elif opcao == 22:
            cadastro_cliente(lista_cliente)

        elif opcao == 23:
            ver_infos_cliente(lista_cliente)

        elif opcao == 24:
            login(lista_cliente)

        elif opcao == 25:
            reservados_alugados(
                lista_filme,
                lista_livro,
                lista_hq,
                lista_cliente
            )

        elif opcao == 26:
            devolucao_alugados(
                lista_filme,
                lista_livro,
                lista_hq,
                lista_cliente
            )

        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    menu()
