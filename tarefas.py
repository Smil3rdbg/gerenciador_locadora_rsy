#casdastro de filme e livros , cadastro usuario, validacao de senha e email, Apagar divida, sistema de compra/aluguel (fita, comida,merch,videocassete) e devolucao, ifood de fita, sistema de estoque feito em pilha

#funcoes

def cadastro_filme():
    filme = {}  #criou um dicionário vazio para armazenar as informações do filme
    filme['titulo'] = input('Digite o título do filme: ')
    filme['diretor'] = input('Digite o nome do diretor: ')  # filme = dicionario [titulo] = cria uma etiqueta, topico com esse nome
    filme['ano'] = input('Digite o ano de lançamento: ')
    print(f'\n--------------------------------------------------\nTítulo: {filme["titulo"]}\nDiretor: {filme["diretor"]}\nAno de lançamento: {filme["ano"]}\n\n-----------Filme cadastrado com sucesso!----------')  
    return filme   #retorna o dicionário preenchido com as informações do filme e finaliza a execucao codigo acima assim mostrando o "resultado"


def cadastro_livro():
    livro = {} 
    livro['titulo'] = input('Digite o título do livro: ')
    livro['autor'] = input('Digite o nome do autor: ')  
    livro['ano'] = input('Digite o ano de lançamento: ')
    print(f'\n--------------------------------------------------\nTítulo: {livro["titulo"]}\nAutor: {livro["autor"]}\nAno de lançamento: {livro["ano"]}\n\n-----------Livro cadastrado com sucesso!----------')  
    return livro  


def cadastro_hq():
    hq = {} 
    hq['titulo'] = input('Digite o título da HQ: ')
    hq['autor'] = input('Digite o nome do autor: ')  
    hq['ano'] = input('Digite o ano de lançamento: ')
    print(f'\n--------------------------------------------------\nTítulo: {hq["titulo"]}\nAutor: {hq["autor"]}\nAno de lançamento: {hq["ano"]}\n\n-----------HQ cadastrada com sucesso!----------')  
    return hq  
