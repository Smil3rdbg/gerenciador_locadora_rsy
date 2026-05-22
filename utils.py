#sistema multa, deixar bonitinho/organizado, configuro aparencia data, sistema de apagar e salvar(tuplas), configurar dinheiro pra float.  

#LISTAS .

#entre '' é str sem é int


import random


def chama_id():
    id_ezin = random.randint(1000, 999999999)  # Gera um número aleatório entre 1 e 1000 para o ID
    return id_ezin



lista_filme = [
    {
        'id': 44444,
        'titulo': 'Vingadores: Ultimato',
        'genero': 'Ação',
        'estoque': [1, 2, 3, 4, 5],
        'estudio': 'Marvel Studios',
        'ano': 2019
    }
]  

lista_livro = []  #cria uma lista vazia para armazenar os livros cadastrados

lista_hq = [] 

lista_cliente = [
    {
        'nome' : 'sara dos santos',
        'cpf' : '123456789-00',
        'senha' : '123456',
        'alugados' : ['Vingadores: Ultimato'],  
    }
]

