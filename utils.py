#sistema multa, deixar bonitinho/organizado, configuro aparencia data, sistema de apagar e salvar(tuplas), configurar dinheiro pra float.  

#LISTAS .

#entre '' é str sem é int


import random


def chama_id():
    id_ezin = random.randint(1000, 999999999)  # Gera um número aleatório entre 1 e 1000 para o ID
    return id_ezin



lista_filme = [
    {
        'id': chama_id(),
        'titulo': 'Vingadores: Ultimato',
        'genero': 'Ação',
        'estoque': 5,
        'estudio': 'Marvel Studios',
        'ano': 2019
    }
]  

lista_livro = []  #cria uma lista vazia para armazenar os livros cadastrados

lista_hq = [] 
