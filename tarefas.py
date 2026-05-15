#casdastro de filme e livros , cadastro usuario, validacao de senha e email, Apagar divida, sistema de compra/aluguel (fita, comida,merch,videocassete) e devolucao, ifood de fita, sistema de estoque feito em pilha

import random

id = random.randint(1000, 9999999)  #gera um número aleatório entre 1000 e 9999999 para ser usado como ID do filme, livro ou HQ cadastrado

#LISTAS 

lista_filme = [
    {
        "id": 9864344,
        "titulo": "Sara",
        "diretor": "linda",
        "ano": "maravilhosa"
    },
    {
        "id": 7609292,
        "titulo": "fcsag",
        "diretor": "gaagaga",
        "ano": "gagfag"
    }
]  #lista com infos pra testar

lista_livro = []  #cria uma lista vazia para armazenar os livros cadastrados

lista_hq = [] 

#FUNÇÕES

def cadastro_filme():
    filme = {} #criou um dicionário vazio para armazenar as informações do filme
    filme['id'] = id  #atribui o ID gerado ao filme
    filme['titulo'] = input('Digite o título do filme: ')
    filme['diretor'] = input('Digite o nome do diretor: ')  # filme = dicionario [titulo] = cria uma etiqueta, topico com esse nome
    filme['ano'] = input('Digite o ano de lançamento: ')

# chaves juntas n usam virgula pra separar os inputs, chaves q inglobam os msms precisam ser separados por virgula.

    lista_filme.append(filme)  #adiciona o dicionário do filme à lista de filmes cadastrados
    print(f'\n--------------------------------------------------\nID: {filme["id"]}\nTítulo: {filme["titulo"]}\nDiretor: {filme["diretor"]}\nAno de lançamento: {filme["ano"]}\n\n-----------Filme cadastrado com sucesso!----------')  
    return filme   #retorna o dicionário preenchido com as informações do filme e finaliza a execucao codigo acima assim mostrando o "resultado"


def cadastro_livro():
    livro = {} 
    livro['id'] = id
    livro['titulo'] = input('Digite o título do livro: ')
    livro['autor'] = input('Digite o nome do autor: ')  
    livro['ano'] = input('Digite o ano de lançamento: ')
    lista_livro.append(livro)
    print(f'\n--------------------------------------------------\nID: {livro["id"]}\nTítulo: {livro["titulo"]}\nAutor: {livro["autor"]}\nAno de lançamento: {livro["ano"]}\n\n-----------Livro cadastrado com sucesso!----------')  
    return livro  


def cadastro_hq():
    hq = {} 
    hq['id'] = id
    hq['titulo'] = input('Digite o título da HQ: ')
    hq['autor'] = input('Digite o nome do autor: ')  
    hq['ano'] = input('Digite o ano de lançamento: ')
    lista_hq.append(hq)
    print(f'\n--------------------------------------------------\nID: {hq["id"]}\nTítulo: {hq["titulo"]}\nAutor: {hq["autor"]}\nAno de lançamento: {hq["ano"]}\n\n-----------HQ cadastrada com sucesso!----------')  
    return hq  



#APAGAR ITENS CADASTRADOS

def apagar_cadastrofilme(lista_filme):
    
        id_para_apagar = int(input('Digite o ID do filme que deseja apagar: '))  #PERGUNTA PRIMEIRO (Fora do loop, para perguntar uma vez só)
        
        for filme in lista_filme: #PARA variavel (dicionario) NA lista de filmes FAÇA:
            if id_para_apagar == filme['id']: #SE o id digitado for igual ao id do filme na lista ENTÃO:
                lista_filme.remove(filme) #remove o filme da lista de filmes
                print('Cadastro apagado com sucesso!') 
        print(lista_filme) #para parar o loop
        return 
        

    


#VER ITENS CADASTRADOS

def ver_infos_filme(lista_filme):
    print("\n---------FILMES CADASTRADOS:--------\n")
    for filme in lista_filme:  #LOOP PARA PERCORRER A LISTA DE FILMES CADASTRADOS E IMPRIMIR AS INFORMAÇÕES DE CADA UM
        print(filme)

def ver_infos_livro(lista_livro):
    print("\n---------LIVROS CADASTRADOS:--------\n")
    for livro in lista_livro:
        print(livro)

def ver_infos_hq(lista_hq):
    print("\n---------HQS CADASTRADAS:--------\n")
    for hq in lista_hq:
        print(hq)

