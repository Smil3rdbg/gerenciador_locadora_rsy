#casdastro de filme e livros , cadastro usuario, validacao de senha e email, Apagar divida, sistema de compra/aluguel (fita, comida,merch,videocassete) e devolucao, ifood de fita, sistema de estoque feito em pilha

from utils import *



   

#FUNÇÕES

def cadastro_filme(lista_filme):
    filme = {} #criou um dicionário vazio para armazenar as informações do filme
    filme['id'] = chama_id()  #atribui o ID gerado ao filme
    filme['titulo'] = input('\nDigite o TÍTULO do filme: ')
    filme['genero'] = input('\nDigite o GÊNERO do filme: ')
    while True : # (loop) enquanto for verdade que o input não é int ele vai ficar em looping
        estoque = input('\nDigite a QUANTIDADE de exemplares em ESTOQUE: ') #tive que criar a variavel estoque fora do dic pra atribuir o dado numero caso estivesse sido colocado
        if estoque.isdigit(): #o valor dado é int?
            estoque = int(estoque)
            filme['estoque'] = list(range(1, estoque +1, 1))
            break # quebra o loop caso o usuario digite um número válido para o estoque
        else :  
            print('\nValor inválido para estoque. Por favor, digite um número.')

    filme['estudio'] = input('\nDigite o nome do ESTÚDIO: ') # o problema era aq q o estudio tava dentro do loop do estoque, ai eu separei em 3 etapar assim colocando ua folha no meio de tijolos
    
    while True :
        ano = input('\nDigite o ANO de LANÇAMENTO: ')
        if ano.isdigit():
            filme['ano'] = int(ano)
            lista_filme.append(filme)  #adiciona o dicionário do filme à lista de filmes cadastrados
            ver_infos_filme(lista_filme) #retorna o dicionário preenchido com as informações do filme e finaliza a execucao codigo acima assim mostrando o "resultado"
            break
        else :  
            print('\nValor inválido para ano de lançamento. Por favor, digite um número.')
# chaves juntas n usam virgula pra separar os inputs, chaves q inglobam os msms precisam ser separados por virgula.


def cadastro_livro():
    livro = {} 
    livro['id'] = chama_id()  
    livro['titulo'] = input('\nDigite o TÍTULO do livro: ')
    livro['genero'] = input('\nDigite o GÊNERO do livro: ')
    while True : 
        estoque = input('\nDigite a QUANTIDADE de exemplares em ESTOQUE: ') 
        if estoque.isdigit(): 
            estoque = int(estoque)
            livro['estoque'] = list(range(1, estoque +1, 1))
            break 
        else :  
            print('\nValor inválido para estoque. Por favor, digite um número.')
    livro['estudio'] = input('\nDigite o nome do ESTÚDIO: ') 
    while True :
        ano = input('\nDigite o ANO de LANÇAMENTO: ')
        if ano.isdigit():
            livro['ano'] = int(ano)
            lista_livro.append(livro)  
            ver_infos_livro(lista_livro)
            break
        else :  
            print('\nValor inválido para ano de lançamento. Por favor, digite um número.')


def cadastro_hq():
    hq = {} 
    hq['id'] = chama_id()  
    hq['titulo'] = input('\nDigite o TÍTULO da HQ: ')
    hq['genero'] = input('\nDigite o GÊNERO da HQ: ')
    while True : 
        estoque = input('\nDigite a QUANTIDADE de exemplares em ESTOQUE: ') 
        if estoque.isdigit(): 
            estoque = int(estoque)
            hq['estoque'] = list(range(1, estoque +1, 1))
            break 
        else :  
            print('\nValor inválido para estoque. Por favor, digite um número.')
    hq['estudio'] = input('\nDigite o nome do ESTÚDIO: ') 
    while True :
        ano = input('\nDigite o ANO de LANÇAMENTO: ')
        if ano.isdigit():
            hq['ano'] = int(ano)
            lista_hq.append(hq)  
            ver_infos_hq(lista_hq)
            break
        else :  
            print('\nValor inválido para ano de lançamento. Por favor, digite um número.')
            



#APAGAR ITENS CADASTRADOS

def apagar_cadastrofilme(lista_filme):
        while True:
            id_para_apagar = input('\n\nDigite o ID do filme que deseja apagar: ')
            
            filme_achado = False
            for filme in lista_filme: #PARA variavel (dicionario) NA lista de filmes FAÇA:
                if id_para_apagar.isdigit() and int(id_para_apagar) == filme['id']: #SE o id digitado for igual ao id do filme na lista ENTÃO: 
                    lista_filme.remove(filme)
                    print('\n\nCadastro apagado com sucesso!\n\n')
                    filme_achado = True
                    return

                if not filme_achado :  
                    print('\n\nID não encontrado! Tente novamente.\n') 
                
# pede o input, cria uma variavel e coloca ela como false, puxa o dicionario filme da lista, se id NÂO(ta false) for str(letra) e ao se tornar int se numero for igual o id de algum filme, ele remove tudo do filme, mostra q removeu, transforma a variavel em true e para todos os loopings
# se o id (ta false originalmente) NÃO (muda pra true) (ai teria que ser: for str ou for um numero q n é um id) vai encotrar id e vai voltar pro começo do loop.


def apagar_cadastrolivro(lista_livro):
    
        while True:
            id_para_apagar = input('\n\nDigite o ID do livro que deseja apagar: ')
            
            livro_achado = False
            for livro in lista_livro: 
                if id_para_apagar.isdigit() and int(id_para_apagar) == livro['id']: 
                    lista_livro.remove(livro)
                    print('\n\nCadastro apagado com sucesso!\n\n')
                    livro_achado = True
                    return

                if not livro_achado :  
                    print('\n\nID não encontrado! Tente novamente.\n') 
        
def apagar_cadastrohq(lista_hq):
    
        while True:
            id_para_apagar = input('\n\nDigite o ID da HQ que deseja apagar: ')
            
            hq_achado = False
            for hq in lista_hq: 
                if id_para_apagar.isdigit() and int(id_para_apagar) == hq['id']:  
                    lista_hq.remove(hq)
                    print('\n\nCadastro apagado com sucesso!\n\n')
                    hq_achado = True
                    return

                if not hq_achado :  
                    print('\n\nID não encontrado! Tente novamente.\n') 
                print('\n\nID não encontrado! Tente novamente.\n\n') 
                return 
        
                
    

#VER ITENS CADASTRADOS

def ver_infos_filme(lista_filme):
    print("\n---------FILMES CADASTRADOS:--------\n")
    for filme in lista_filme:  #LOOP PARA PERCORRER A LISTA DE FILMES CADASTRADOS E IMPRIMIR AS INFORMAÇÕES DE CADA Um
        print(f'\n📍 ID: {filme["id"]}\n\n📎 Título: {filme["titulo"]}\n\n🎞️  Gênero: {filme["genero"]}\n\n📦 Em estoque: {filme["estoque"]}\n\n🎬 Estúdio: {filme["estudio"]}\n\n🎆 Ano de lançamento: {filme["ano"]}') #printa as infos pra eu conseguir deixar organizado, c eu printasse apenas (filme) ia puxar tudo da lista e ia ficar feio
        print('=' * 50)  #adiciona 50 = para separar visualmente as informações de cada filme cadastrado

def ver_infos_livro(lista_livro):
    print("\n---------LIVROS CADASTRADOS:--------\n")
    for livro in lista_livro:
        print(f'\n📍 ID: {livro["id"]}\n\n📎 Título: {livro["titulo"]}\n\n🎞️  Gênero: {livro["genero"]}\n\n📦 Em estoque: {livro["estoque"]}\n\n🎬 Estúdio: {livro["estudio"]}\n\n🎆 Ano de lançamento: {livro["ano"]}')
        print('=' * 50)  
        
def ver_infos_hq(lista_hq):
    print("\n---------HQS CADASTRADAS:--------\n")
    for hq in lista_hq:
        print(f'\n📍 ID: {hq["id"]}\n\n📎 Título: {hq["titulo"]}\n\n🎞️  Gênero: {hq["genero"]}\n\n📦 Em estoque: {hq["estoque"]}\n\n🎬 Estúdio: {hq["estudio"]}\n\n🎆 Ano de lançamento: {hq["ano"]}')
        print('=' * 50) 

# preciso fazer um sistema que recolha a quantidade de estoque que tem na lista e qnd recolher ele leia qnts itens(filmes etc ) tem de estoque pra implementar no sistema de aluguel e devolucao, qro q mostre os status: tem ou não

def controle_estoque_filme(lista_filme):

    for filme in lista_filme:
        if filme['estoque'] >= 1:
            print('=' * 100) 
            print(f'\n\nO filme {filme["titulo"]} tem {filme["estoque"]} exemplares em estoque.\n')
            print('=' * 100)  
        elif filme['estoque'] == 0 :
            print(f'O filme {filme["titulo"]} está esgotado.')

   
    

    while True:
        
    #se for 1 ou 2 aceita, se for diferente ou for  str recusa e volta em loop ate acertar
           
        try:   
            print('\n1 - Sim\n2 - Não')
            adic_filme = int(input('\nDeseja adicionar mais exemplares a algum filme?: '))
             
            if adic_filme != 1 and adic_filme != 2:  # se ofr um numero q n seja 1 ou 2 ele bloq 
                print('\n\n\nOpção inválida! Tente novamente\n')
                print('-' * 100)
                continue # faz com q o codigo volte pro começo do loop e mostre a pergunta de novo
            
        except ValueError:    # se for um str 
                print('-' * 100) 
                print('\n\nOpção inválida! Tente novamente\n')
                print('-' * 100)
                continue
        
        while True:

            if adic_filme == 2:
                print('\n\nNenhuma ação executada!\n')
                break
        
        

            if adic_filme == 1:
            
                for filme in lista_filme:
                
                    try:
                        filme_etiq_nome = filme['titulo']
                        filme_etiq_id = filme['id']
                        filme_etiq_estudio = filme['estudio']

                        print(f"\n\nesses são as infos de cada filme:\n\n📎  Título: {filme_etiq_nome}\n📍  ID: {filme_etiq_id}\n🎞️   Gênero: {filme_etiq_estudio}\n📦 Em estoque: {filme["estoque"]}")


                        id_estoque_filme = int(input('\n\nDigite o ID do filme que deseja adicionar exemplares: '))
                
                

                        if id_estoque_filme == filme['id']: #int
                            print('-' * 100) 
                            print('\n' + '=' * 100)
                            print(f'\n\nO filme {filme["titulo"]} tem {filme["estoque"]} exemplares em estoque.\n')
                            print('\n' + '=' * 100)
                            
                    
                            #COLOCAR DEF DA DEVOLUCAO (+1)
                
            
                        elif id_estoque_filme != filme['id']: #int
                            print('\n\nID não encontrado! Tente novamente.\n\n') 
                            print('\n' + '-' * 100)
                            continue
                    
                    except ValueError: #str
                        print('\n\nID não encontrado! Tente novamente.\n\n') 
                        print('\n' + '-' * 100)
                        continue
            
            
def aluguel_filme(lista_filme):
    
    while True:
        
    #se for 1 ou 2 aceita, se for diferente ou for  str recusa e volta em loop ate acertar
           
        try:   
            print('\n1 - Sim\n2 - Não')
            re_filme = int(input('\nDeseja reservar um filme?: '))
             
            if re_filme != 1 and re_filme != 2:  # se ofr um numero q n seja 1 ou 2 ele bloq 
                print('\n\n\nOpção inválida! Tente novamente\n')
                print('-' * 100)
                continue # faz com q o codigo volte pro começo do loop e mostre a pergunta de novo
            
        except ValueError:    # se for um str 
                print('-' * 100) 
                print('\n\nOpção inválida! Tente novamente\n')
                print('-' * 100)
                continue
        
        while True:

            if re_filme == 2:
                print('\n\nNenhuma ação executada!\n')
                break
        
        

            if re_filme == 1:
            
                for filme in lista_filme:
                
                    try:
                        filme_etiq_nome = filme['titulo']
                        filme_etiq_id = filme['id']
                        filme_etiq_estudio = filme['estudio']

                        print(f"\n\nesses são as infos de cada filme:\n\n📎  Título: {filme_etiq_nome}\n📍  ID: {filme_etiq_id}\n🎞️   Gênero: {filme_etiq_estudio}\n📦 Em estoque: {filme["estoque"]}")


                        id_reserva_filme = int(input('\n\nDigite o ID do filme que deseja reservar: '))
    

                        if id_reserva_filme == filme['id']: #int
                            

                            if filme['estoque'] <= 0:
                                print('-' * 100)
                                print(f'O filme {filme["titulo"]} está esgotado.')
                                print('-' * 100)
                            


                            #PAREI NESSE DAQ DE BAIXO   
                            elif filme['estoque'] > 5 :





                                print('-' * 100) 
                                print('\n' + '=' * 100)
                                print(f'\n\nO filme {filme["titulo"]} tem {filme["estoque"]} exemplares em estoque.\n')
                                print('\n' + '=' * 100)
                            
                    
                        remover = filme['estoque'] -1
                            #COLOCAR DEF DA DEVOLUCAO (+1)
                
            
                        if id_reserva_filme != filme['id']: #int
                            print('\n\nID não encontrado! Tente novamente.\n\n') 
                            print('\n' + '-' * 100)
                            continue
                    
                    except ValueError:  #str
                        print('\n\nID não encontrado! Tente novamente.\n\n') 
                        print('\n' + '-' * 100)
                        continue

                

    #filme id tal
    #pilha = 

































ANOTACOES NA SALA




 for filme in lista_filme[-1]['etiqueta']:
                            
                                if filme[-1]['etiqueta'] <= 0:
                                    print('-' * 100)
                                    print(f'O filme {filme["titulo"]} está esgotado.')
                                    print('-' * 100)
                            


                            #PAREI NESSE DAQ DE BAIXO   
                                elif lista_filme['estoque'] == reserva_filme:
                                    retirado = filme['estoque'] - reserva_filme
                                    print('-' * 100)
                                    print(f'Foi retirado {retirado} exemplares do filme {filme['titulo']}!')

                            




                                print('-' * 100) 
                                print('\n' + '=' * 100)
                                print(f'\n\nO filme {filme["titulo"]} tem {filme["estoque"]} exemplares em estoque.\n')
                                print('\n' + '=' * 100)
                            
                    
                        remover = filme['estoque'] -1
                            #COLOCAR DEF DA DEVOLUCAO (+1)
                
            
                        if id_reserva_filme != filme['id']: #int
                            print('\n\nID não encontrado! Tente novamente.\n\n') 
                            print('\n' + '-' * 100)
                            continue
                    
                    except ValueError:  #str
                        print('\n\nID não encontrado! Tente novamente.\n\n') 
                        print('\n' + '-' * 100)
                        continue

                

    #filme id tal
    #pilha = 

    
