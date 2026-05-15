# mostrar data d qnd foi alugado e devolvido (Em desenvolvimento)

# =========================================
# SISTEMA DE LOCADORA DE FILMES
# =========================================

import json

# Lista onde os filmes serão armazenados 
filmes = []


# =========================
# FUNÇÃO PARA CADASTRAR
# =========================
def cadastrar_filme():
    print("\n--- CADASTRAR FILME ---")

    nome = input("Digite o nome do filme: ")
    genero = input("Digite o gênero: ")
    autor = input("Digite o autor(a): ")
    data = input("Digite a data de lançamento: ")

    filme = [
        {
        "Nome": nome,
        "Gênero": genero,
        "Autor(a)": autor,
        "Data de lançamento": data
        }
    ]

    filmes.append(filme)

    print("\nFilme cadastrado com sucesso!")


# =========================
# FUNÇÃO PARA LISTAR
# =========================
def listar_filmes():
    print("\n--- LISTA DE FILMES ---")

    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
    else:
        for i, filme in enumerate(filmes): # O enumerate vai mostrar o número do filme, começando do 1, e o filme em si.
           print(f"""
Nome: {filme[0].get("Nome", "Não informado")}
Gênero: {filme[0].get("Gênero", "Não informado")}
Autor(a): {filme[0].get("Autor(a)", "Não informado")}
Data de lançamento: {filme[0].get("Data de lançamento", "Não informado")}
""")

 # O get vai evitar caso tenha algum erro de chave, ele vai mostrar que não tem a informação, evitando mostrar a mensagem de erro.


# =========================
# Função para procurar os filminhos
# =========================
def buscar_filme():
    print("\n--- BUSCAR FILME ---")

    nome_busca = input("Digite o nome do filme: ")

    encontrado = False

    for filme in filmes:
        if filme["Nome"].lower() == nome_busca.lower():
            print("\nFilme encontrado!")
            print(f"""
Nome: {filme["Nome"]}
Gênero: {filme["Gênero"]}
Autor(a): {filme["Autor(a)"]}
Data de lançamento: {filme["Data de lançamento"]}
""")
            encontrado = True

    if encontrado == False:
        print("Filme não encontrado.")


# =========================
# Função para apagar algum filme
# =========================
def remover_filme():
    print("\n--- REMOVER FILME ---")

    nome_remover = input("Digite o nome do filme: ")

    for filme in filmes:
        if filme["Nome"].LOWER() == nome_remover.lower():
            filmes.remove(filme)
            print("Filme removido com sucesso!")
            return

    print("Filme não encontrado.")


# =========================
# Salvar em Json
# =========================
def salvar_json():
    with open("filmes.json", "w", encoding="utf-8") as arquivo:
        json.dump(filmes, arquivo, indent=4, ensure_ascii=False)

    print("Dados salvos no arquivo JSON!")


# =========================
# Carregar Json
# =========================
def carregar_json():
    global filmes

    try:
        with open("filmes.json", "r", encoding="utf-8") as arquivo:
            filmes = json.load(arquivo)

        print("Dados carregados com sucesso!")

    except FileNotFoundError:
        print("Arquivo JSON não encontrado. Um novo será criado.")


# =========================
# MENU PRINCIPAL
# =========================
def menu():
    carregar_json()

    while True:
        print("""
======== LOCADORA ========

1 - Cadastrar filme
2 - Listar filmes
3 - Buscar filme
4 - Remover filme
5 - Salvar dados
0 - Sair

==========================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_filme()

        elif opcao == "2":
            listar_filmes()

        elif opcao == "3":
            buscar_filme()

        elif opcao == "4":
            remover_filme()

        elif opcao == "5":
            salvar_json()

        elif opcao == "0":
            salvar_json()
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


# =========================
# INICIAR SISTEMA
# =========================
menu()
