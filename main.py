bom dia rodrygo <3 
tkinter

from tarefas import cadastro_filme, cadastro_livro, cadastro_hq, ver_infos_filme, ver_infos_livro, ver_infos_hq, apagar_cadastrofilme, apagar_cadastrolivro, apagar_cadastrohq, modificar_cadastrofilme, modificar_cadastrolivro, modificar_cadastrohq
from utils import lista_filme, lista_livro, lista_hq

# tem q colocar ate a variavel da lista pra importar 



#APAGAR CADASTRO DE FILME

def apagar_filme():
    print('\n---------EXLUSÃO DE CADASTRO DE FILME---------')
    print('\n1 - Sim\n2 - Não')
    opcao_apagar = int(input('\nDeseja apagar o cadastro?: '))

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

    modificar_filme = int(input('\nDigite o ID do filme que deseja modificar: '))

    for filme in lista_filme:
        if modificar_filme == filme['id']:
            filme['titulo'] = input('Digite o novo título do filme: ')
            filme['diretor'] = input('Digite o nome do novo diretor: ')
            filme['ano'] = input('Digite o novo ano de lançamento: ')
            print('\n~~~~~~~~DADOS DO FILME MODIFICADOS COM SUCESSO!~~~~~~~~\n')
            ver_infos_filme(lista_filme)
            return  #return precisa estar alinhado com as infos dentro do if para fechar o looping
    print('\n\nID não encontrado!Tente novamente.') # pro print funcionar ele precisa estar alinhado com o for (loop) pra ficar fora do loop e mostrar o print

# tive um pouco de dificuldade nesse final da def acima pq o print tava mostrando o numero de vezes de acordo com o conteudo que tinha na lista (2x para 2 conjuntos de itens)

def modificar_cadastrolivro(lista_livro):
    print('\n---------MODIFICAÇÃO DE CADASTRO DE LIVRO---------')

    modificar_livro = int(input('\nDigite o ID do livro que deseja modificar: '))

    for livro in lista_livro:
        if modificar_livro == livro['id']:
            livro['titulo'] = input('Digite o novo título do livro: ')
            livro['autor'] = input('Digite o nome do novo autor: ')
            livro['ano'] = input('Digite o novo ano de lançamento: ')
            print('\n~~~~~~~~DADOS DO LIVRO MODIFICADOS COM SUCESSO!~~~~~~~~\n')
            ver_infos_livro(lista_livro)
            return  
    print('\n\nID não encontrado!Tente novamente.')

def modificar_cadastrohq(lista_hq):
    print('\n---------MODIFICAÇÃO DE CADASTRO DE HQ---------')

    modificar_hq = int(input('\nDigite o ID da HQ que deseja modificar: '))

    for hq in lista_hq:
        if modificar_hq == hq['id']:
            hq['titulo'] = input('Digite o novo título da HQ: ')
            hq['autor'] = input('Digite o nome do novo autor: ')
            hq['ano'] = input('Digite o novo ano de lançamento: ')
            print('\n~~~~~~~~DADOS DA HQ MODIFICADOS COM SUCESSO!~~~~~~~~\n')
            ver_infos_hq(lista_hq)
            return  
    print('\n\nID não encontrado!Tente novamente.')




