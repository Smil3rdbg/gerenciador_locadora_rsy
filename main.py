bom dia rodrygo <3 
tkinter

from tarefas import cadastro_filme, cadastro_livro, cadastro_hq, ver_infos_filme, ver_infos_livro, ver_infos_hq, apagar_cadastrofilme, apagar_cadastrolivro, apagar_cadastrohq, modificar_cadastrofilme, modificar_cadastrolivro, modificar_cadastrohq
from utils import lista_filme, lista_livro, lista_hq

# tem q colocar ate a variavel da lista pra importar 



#APAGAR CADASTRO DE FILME

def apagar_filme():
    print('\n---------EXLUSÃO DE CADASTRO DE FILME---------')
    print('\n1 - Sim\n2 - Não')
    opcao_apagar = int(input('\nDeseja apagar o filme cadastrado?: '))

    if opcao_apagar == 1:
        ver_infos_filme(lista_filme)
        apagar_cadastrofilme(lista_filme) 
    elif opcao_apagar == 2:
        print('\nCadastro mantido!\n')    
    
def apagar_livro():
    print('\n---------EXLUSÃO DE CADASTRO DE LIVRO---------')
    print('\n1 - Sim\n2 - Não')
    opcao_apagar = int(input('\nDeseja apagar o cadastro?: '))

    if opcao_apagar == 1:
        ver_infos_livro(lista_livro)
        apagar_cadastrolivro(lista_livro) 
    elif opcao_apagar == 2:
        print('\nCadastro mantido!\n') 

    
def apagar_hq():
    print('\n---------EXLUSÃO DE CADASTRO DE HQ---------')
    print('\n1 - Sim\n2 - Não')
    opcao_apagar = int(input('\nDeseja apagar o cadastro?: '))

    if opcao_apagar == 1:
        ver_infos_hq(lista_hq)
        apagar_cadastrohq(lista_hq) 
    elif opcao_apagar == 2:
        print('\nCadastro mantido!\n')




# MUDAR DADOS DE CADASTRO DE FILME

def modificar_cadastrofilme(lista_filme):
    
    print('\n---------MODIFICAÇÃO DE CADASTRO DE FILME---------')
  

    while True:
        
    #se for 1 ou 2 aceita, se for diferente ou for  str recusa e volta em loop ate acertar
           
        try:   
            print('\n1 - Sim\n2 - Não')
            opcao_modificar = int(input('\nDeseja modificar um filme cadastrado?: '))
             
            if opcao_modificar != 1 and opcao_modificar != 2:   
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue # faz com q o codigo volte pro começo do loop e mostre a pergunta de novo
            
        except ValueError:    
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue




        if opcao_modificar == 2:
            print('\n\nNenhuma ação executada!\n')
            break
        elif opcao_modificar == 1:
            ver_infos_filme(lista_filme)


        while True:    
            
            try:
                modificar_filme = int(input('\nDigite o ID do filme que deseja modificar: '))

            except ValueError:
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue

            filme_encontrado = False


            for filme in lista_filme:

            
                if modificar_filme == filme['id']:
                    
                    filme_encontrado = True
                    
                    print('\n' + '=' * 50)
                    filme['titulo'] = input('\n\nDigite o novo título do filme: ')
                    filme['genero'] = input('\n\nDigite o novo gênero do filme: ')
                    filme['estoque'] = int(input('\n\nDigite a nova quantidade de exemplares em estoque: '))
                    filme['estudio'] = input('\n\nDigite o novo nome do estúdio: ') 
                    filme['ano'] = int(input('\n\nDigite o novo ano de lançamento: '))
                    print('\n~~~~~~~~DADOS DO FILME MODIFICADOS COM SUCESSO!~~~~~~~~\n')
                    ver_infos_filme(lista_filme)
                    return  #return precisa estar alinhado com as infos dentro do if para fechar o looping
            if filme_encontrado:
                break
            else:
                print('\n\nID não encontrado! Tente novamente.\n\n')
                

    
# tive um pouco de dificuldade nesse final da def acima pq o print tava mostrando o numero de vezes de acordo com o conteudo que tinha na lista (2x para 2 conjuntos de itens)

def modificar_cadastrolivro(lista_livro):
    print('\n---------MODIFICAÇÃO DE CADASTRO DE LIVRO---------')
  

    while True:
        
    #se for 1 ou 2 aceita, se for diferente ou for  str recusa e volta em loop ate acertar
           
        try:   
            print('\n1 - Sim\n2 - Não')
            opcao_modificar = int(input('\nDeseja modificar um livro cadastrado?: '))
             
            if opcao_modificar != 1 and opcao_modificar != 2:   
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue # faz com q o codigo volte pro começo do loop e mostre a pergunta de novo
            
        except ValueError:    
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue




        if opcao_modificar == 2:
            print('\n\nNenhuma ação executada!\n')
            break
        elif opcao_modificar == 1:
            ver_infos_livro(lista_livro)


        while True:    
            
            try:
                modificar_livro = int(input('\nDigite o ID do filme que deseja modificar: '))

            except ValueError:
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue

            livro_encontrado = False


            for livro in lista_livro:

            
                if modificar_livro == livro['id']:
                    
                    livro_encontrado = True
                    
                    print('\n' + '=' * 50)
                    livro['titulo'] = input('\n\nDigite o novo título do livro: ')
                    livro['genero'] = input('\n\nDigite o novo gênero do livro: ')
                    livro['estoque'] = int(input('\n\nDigite a nova quantidade de exemplares em estoque: '))
                    livro['estudio'] = input('\n\nDigite o novo nome do estúdio: ') 
                    livro['ano'] = int(input('\n\nDigite o novo ano de lançamento: '))
                    print('\n~~~~~~~~DADOS DO LIVRO MODIFICADOS COM SUCESSO!~~~~~~~~\n')
                    ver_infos_livro(lista_livro)
                    return  #return precisa estar alinhado com as infos dentro do if para fechar o looping
            if livro_encontrado:
                break
            else:
                print('\n\nID não encontrado! Tente novamente.\n\n')

def modificar_cadastrohq(lista_hq):
    print('\n---------MODIFICAÇÃO DE CADASTRO DE HQ---------')
  

    while True:
        
    #se for 1 ou 2 aceita, se for diferente ou for  str recusa e volta em loop ate acertar
           
        try:   
            print('\n1 - Sim\n2 - Não')
            opcao_modificar = int(input('\nDeseja modificar um HQ cadastrado?: '))
             
            if opcao_modificar != 1 and opcao_modificar != 2:   
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue # faz com q o codigo volte pro começo do loop e mostre a pergunta de novo
            
        except ValueError:    
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue




        if opcao_modificar == 2:
            print('\n\nNenhuma ação executada!\n')
            break
        elif opcao_modificar == 1:
            ver_infos_hq(lista_hq)


        while True:    
            
            try:
                modificar_hq = int(input('\nDigite o ID da HQ que deseja modificar: '))

            except ValueError:
                print('\n\nOpção inválida! Tente novamente\n\n')
                continue

            hq_encontrado = False


            for hq in lista_hq:

            
                if modificar_hq == hq['id']:
                    
                    hq_encontrado = True
                    
                    print('\n' + '=' * 50)
                    hq['titulo'] = input('\n\nDigite o novo título da HQ: ')
                    hq['genero'] = input('\n\nDigite o novo gênero da HQ: ')
                    hq['estoque'] = int(input('\n\nDigite a nova quantidade de exemplares em estoque: '))
                    hq['estudio'] = input('\n\nDigite o novo nome do estúdio: ') 
                    hq['ano'] = int(input('\n\nDigite o novo ano de lançamento: '))
                    print('\n~~~~~~~~DADOS DA HQ MODIFICADOS COM SUCESSO!~~~~~~~~\n')
                    ver_infos_hq(lista_hq)
                    return  #return precisa estar alinhado com as infos dentro do if para fechar o looping
            if hq_encontrado:
                break
            else:
                print('\n\nID não encontrado! Tente novamente.\n\n')

def menu():
    print("""

====🎬FILMES🎬===

1 - Cadastrar filme
2 - apagar filme
3 - Alterar dados do filme
4 - Alugar/comprar
5 - Estoque

====📚LIVROS📚====

6 - Registrar Livro
7 - Apagar livro 
8 - Alterar informações sobre o livro
9 - Alugar/comprar
10 - Estoque de livros

====📖HQ'S📖====

11 - Registrar HQ 
12 - Apagar HQ 
13 - Alterar informações da HQ
14 - Alugar/comprar
15 - Estoque de livros

""")

    opcao = input("Selecione uma das opções abaixo: ")

    if opcao == "1":
        input("Digite o nome do filme")
        input("Digite o genero")
        input("Digite estudio")
        input("Digite o ano de lançamento")


vc n deveria chamar a funcao ja q eu ja criei ela?

cadastro_filme(lista_fime)


