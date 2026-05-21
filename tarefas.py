from utils import *
from dados import status_estoque


# =========================
# FUNÇÕES AUXILIARES
# =========================

def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("\nValor inválido! Digite apenas números.\n")


def criar_estoque(quantidade):
    return list(range(1, quantidade + 1))


def buscar_por_id(lista, id_procurado):
    for item in lista:
        if item["id"] == id_procurado:
            return item

    return None


# =========================
# CADASTROS
# =========================

def cadastro_filme(lista_filme):
    print("\n========= CADASTRO DE FILME =========")

    filme = {
        "id": chama_id(),
        "titulo": input("\nDigite o TÍTULO do filme: "),
        "genero": input("Digite o GÊNERO do filme: "),
        "estoque": criar_estoque(ler_numero("Digite a QUANTIDADE em ESTOQUE: ")),
        "estudio": input("Digite o nome do ESTÚDIO: "),
        "ano": ler_numero("Digite o ANO de LANÇAMENTO: ")
    }

    lista_filme.append(filme)

    print("\nFilme cadastrado com sucesso!\n")
    ver_infos_filme(lista_filme)


def cadastro_livro(lista_livro):
    print("\n========= CADASTRO DE LIVRO =========")

    livro = {
        "id": chama_id(),
        "titulo": input("\nDigite o TÍTULO do livro: "),
        "genero": input("Digite o GÊNERO do livro: "),
        "estoque": criar_estoque(ler_numero("Digite a QUANTIDADE em ESTOQUE: ")),
        "estudio": input("Digite o nome da EDITORA: "),
        "ano": ler_numero("Digite o ANO de LANÇAMENTO: ")
    }

    lista_livro.append(livro)

    print("\nLivro cadastrado com sucesso!\n")
    ver_infos_livro(lista_livro)


def cadastro_hq(lista_hq):
    print("\n========= CADASTRO DE HQ =========")

    hq = {
        "id": chama_id(),
        "titulo": input("\nDigite o TÍTULO da HQ: "),
        "genero": input("Digite o GÊNERO da HQ: "),
        "estoque": criar_estoque(ler_numero("Digite a QUANTIDADE em ESTOQUE: ")),
        "estudio": input("Digite o nome da EDITORA: "),
        "ano": ler_numero("Digite o ANO de LANÇAMENTO: ")
    }

    lista_hq.append(hq)

    print("\nHQ cadastrada com sucesso!\n")
    ver_infos_hq(lista_hq)


# =========================
# VER INFORMAÇÕES
# =========================

def mostrar_item(item):
    if len(item["estoque"]) > 0:
        status = status_estoque[1]
    else:
        status = status_estoque[0]

    print(f"""
📍 ID: {item["id"]}
📎 Título: {item["titulo"]}
🎞️ Gênero: {item["genero"]}
📦 Estoque: {len(item["estoque"])} exemplar(es)
📌 Status: {status}
🎬 Estúdio/Editora: {item["estudio"]}
🎆 Ano de lançamento: {item["ano"]}
""")

    print("=" * 50)


def ver_infos_filme(lista_filme):
    print("\n--------- FILMES CADASTRADOS --------\n")

    if len(lista_filme) == 0:
        print("Nenhum filme cadastrado.")
        return

    for filme in lista_filme:
        mostrar_item(filme)


def ver_infos_livro(lista_livro):
    print("\n--------- LIVROS CADASTRADOS --------\n")

    if len(lista_livro) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in lista_livro:
        mostrar_item(livro)


def ver_infos_hq(lista_hq):
    print("\n--------- HQS CADASTRADAS --------\n")

    if len(lista_hq) == 0:
        print("Nenhuma HQ cadastrada.")
        return

    for hq in lista_hq:
        mostrar_item(hq)


# =========================
# APAGAR CADASTROS
# =========================

def apagar_item(lista, nome_item):
    id_para_apagar = ler_numero(f"\nDigite o ID do {nome_item} que deseja apagar: ")

    item = buscar_por_id(lista, id_para_apagar)

    if item is None:
        print("\nID não encontrado!\n")
    else:
        lista.remove(item)
        print(f"\nCadastro de {nome_item} apagado com sucesso!\n")


def apagar_cadastrofilme(lista_filme):
    apagar_item(lista_filme, "filme")


def apagar_cadastrolivro(lista_livro):
    apagar_item(lista_livro, "livro")


def apagar_cadastrohq(lista_hq):
    apagar_item(lista_hq, "HQ")


# =========================
# ALUGAR FILME
# =========================

def alugar_filme(lista_filme):
    print("\n========= ALUGAR FILME =========")

    if len(lista_filme) == 0:
        print("\nNenhum filme cadastrado.\n")
        return

    ver_infos_filme(lista_filme)

    id_reserva_filme = ler_numero("\nDigite o ID do filme que deseja reservar: ")

    filme = buscar_por_id(lista_filme, id_reserva_filme)

    if filme is None:
        print("\nID não encontrado! Tente novamente.\n")
        return

    filme_quantidade = ler_numero("\nDigite quantos exemplares você quer reservar: ")

    if filme_quantidade <= 0:
        print("\nQuantidade inválida!\n")
        return

    if len(filme["estoque"]) < filme_quantidade:
        print("\nEstoque insuficiente!")
        print(f"Só existem {len(filme['estoque'])} exemplar(es) do filme {filme['titulo']}.")
        return

    for _ in range(filme_quantidade):
        filme["estoque"].pop()

    print(f"""
Ação realizada com sucesso!

Você retirou {filme_quantidade} exemplar(es)
do filme {filme["titulo"]}.

Agora restam {len(filme["estoque"])} exemplar(es) em estoque.
""")


# =========================
# DEVOLUÇÃO DE FILME
# =========================

def devolucao_filme(lista_filme):
    print("\n========= DEVOLUÇÃO DE FILME =========")

    if len(lista_filme) == 0:
        print("\nNenhum filme cadastrado.\n")
        return

    ver_infos_filme(lista_filme)

    id_devolucao_filme = ler_numero("\nDigite o ID do filme que deseja devolver: ")

    filme = buscar_por_id(lista_filme, id_devolucao_filme)

    if filme is None:
        print("\nID não encontrado! Tente novamente.\n")
        return

    filme_quantidade = ler_numero("\nDigite quantos exemplares você quer devolver: ")

    if filme_quantidade <= 0:
        print("\nQuantidade inválida!\n")
        return

    for _ in range(filme_quantidade):
        novo_exemplar = len(filme["estoque"]) + 1
        filme["estoque"].append(novo_exemplar)

    print(f"""
Ação realizada com sucesso!

Você devolveu {filme_quantidade} exemplar(es)
do filme {filme["titulo"]}.

Agora existem {len(filme["estoque"])} exemplar(es) em estoque.
""")


# =========================
# CONTROLE DE ESTOQUE
# =========================

def controle_estoque_filme(lista_filme):
    print("\n========= CONTROLE DE ESTOQUE =========")

    if len(lista_filme) == 0:
        print("\nNenhum filme cadastrado.\n")
        return

    ver_infos_filme(lista_filme)

    id_estoque_filme = ler_numero("\nDigite o ID do filme que deseja ver o estoque: ")

    filme = buscar_por_id(lista_filme, id_estoque_filme)

    if filme is None:
        print("\nID não encontrado!\n")
        return

    if len(filme["estoque"]) > 0:
        status = status_estoque[1]
    else:
        status = status_estoque[0]

    print(f"""
Filme: {filme["titulo"]}
Quantidade em estoque: {len(filme["estoque"])}
Status: {status}
""")

    while True:
        print("""
--------- OPÇÕES DO ESTOQUE ---------

1 - Adicionar exemplares novos
2 - Reservar filme
3 - Devolver filme
0 - Sair
""")

        resposta = ler_numero("Digite uma opção: ")

        if resposta == 1:
            quantidade = ler_numero("\nDigite a quantidade de exemplares que deseja adicionar: ")

            if quantidade <= 0:
                print("\nQuantidade inválida!\n")
                continue

            for _ in range(quantidade):
                novo_exemplar = len(filme["estoque"]) + 1
                filme["estoque"].append(novo_exemplar)

            print(f"\nForam adicionados {quantidade} exemplar(es).")
            print(f"Estoque atual: {len(filme['estoque'])}\n")

        elif resposta == 2:
            alugar_filme(lista_filme)

        elif resposta == 3:
            devolucao_filme(lista_filme)

        elif resposta == 0:
            print("\nVocê saiu do controle de estoque.\n")
            break

        else:
            print("\nOpção inválida!\n")


# =========================
# CLIENTES
# =========================

def cadastro_cliente(lista_cliente):
    print("\n========= CADASTRO DE CLIENTES =========")

    cliente = {
        "nome": input("\nDigite o NOME do cliente: "),
        "cpf": input("Digite o CPF do cliente: "),
        "senha": input("Digite a SENHA do cliente: "),
        "alugados": []
    }

    lista_cliente.append(cliente)

    print("\nCadastro efetuado com sucesso!\n")


def ver_infos_cliente(lista_cliente):
    print("\n--------- CLIENTES CADASTRADOS --------\n")

    if len(lista_cliente) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in lista_cliente:
        print(f"""
Nome: {cliente["nome"]}
CPF: {cliente["cpf"]}
Senha: {cliente["senha"]}
Alugados: {cliente["alugados"]}
""")

        print("=" * 50)


def login(lista_cliente):
    print("\n========= LOGIN =========")

    nome = input("\nDigite o nome do cliente: ")
    senha = input("Digite a senha: ")

    for cliente in lista_cliente:
        if nome == cliente["nome"] and senha == cliente["senha"]:
            print("\nUsuário encontrado!")
            print("--- SEJA BEM-VINDO! ---")
            return cliente

    print("\nUsuário não encontrado!\n")
    return None



# =========================
# SISTEMA FILA (FIFO) (TEM Q TERMINAR)
# =========================


def reservados_alugados(lista_filme, lista_livro, lista_hq, lista_cliente):
    while True:
        print('=' * 20, 'SISTEMA DE REGISTRO DE ALUGUEL', '=' * 20 )
        print('\n\nVocê deseja adicionar um item alugado na conta de um cliente?')
        print('\n\n\n---OPÇÕES---\n\n(SIM)\n\n(NÂO)')
        fila_flhq = input('\n\nDigite uma das opções acima: ')
        
        
         # formula para juntar varios itens e listas de parametro de uma vez
    

        if fila_flhq == 'nao' or fila_flhq == 'não':
                print('\nNenhuma ação executada.')
                break
        
        
        elif fila_flhq == 'sim':
                while True:
                    print('=' * 100)
                    print('\n---OPÇÕES---\n1 - filme\n2 - livro\n3 - hq\n\n')
                    escolha = input("Digite em qual local você quer adicionar uma reserva: ")
                    
                    if escolha == '1':
                        alugar_filme(lista_filme)
                        for filme in lista_filme:
                            for cliente in lista_cliente:
                                
                                cliente['alugados'].append(filme['titulo'])
                                print('\n\nAção realizada com sucesso.')
                                print(f'\nO cliente possui {cliente['alugados']} na sua lista de itens alugados')
                                break
                            break
                        
                    elif escolha == '2':
                        alugar_livro(lista_livro)
                        for livro in lista_livro:
                            for cliente in lista_cliente:
                                
                                cliente['alugados'].append(livro['titulo'])
                                print('Ação realizada com sucesso.')
                                print(f'O cliente possui {cliente['alugados']} na sua lista de itens alugados')
                                break
                            break
                        
                    elif escolha == '3':
                        alugar_hq(lista_hq)
                        for hq in lista_hq:
                            for cliente in lista_cliente:
                                
                                cliente['alugados'].append(hq['titulo'])
                                print('Ação realizada com sucesso.')
                                print(f'O cliente possui {cliente['alugados']} na sua lista de itens alugados')
                                break
                            break
                
                
                    else:
                        print('\n\nResposta invalida! tente novamente.\n\n')
                        continue
                        
        
        
        
        
        else:        
            print('\n\nResposta invalida, Digite apenas SIM ou NÃO.\n\n')
            continue
