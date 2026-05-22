# LOCADORA RSY

O tema escolhido para o projeto foi uma Locadora de Filmes. O sistema foi desenvolvido pelos estudantes Rodrygo Schadeck Gomes, Sara dos Santos de Oliveira e Yasmin Santos de Lima, alunos do 1° semestre da universidade BRAZ CUBAS, turma 012A do período da manhã.

---

# RESUMO DO PROJETO

O Sistema de Locadora é um projeto desenvolvido em Python com o objetivo de gerenciar o cadastro e o controle de filmes, livros e HQs em uma locadora. O programa foi criado para praticar conceitos básicos e intermediários da linguagem Python, utilizando organização em múltiplos arquivos e estruturas de dados.

---

## EXPLICAÇÃO CONCEITUAL

- FIFO(First in First out): O FIFO é o conceito de o primeiro item colocado na lista ser o primeiro a sair, como um sistema de fila no dia a dia. Adicionando um item em uma lista e retirando o primeiro item dessa mesma lista.  Sendo utilizado os comandos .pop() para remoção e .append() para adição.


**O FIFO aparece nesse código:**

'''
for _ in range(quantidade):
                    item['estoque'].pop()
                cliente['alugados'].append(item['titulo'])
'''

Que esta localizado na def de reservados_alugados().


**E nesse código:**


'cliente['alugados'].pop(0)'


Que esta localizado na def de devolucao_alugados().   

---

- LIFO(Last in First out): Ao contrario do conceito FIFO, o LIFO adiciona no ultimo lugar da lista e é retirado a partir do ultimo item da lista. Sendo utilizado sempre o exemplo de uma pilha de pratos em ensinos acadêmicos. Sendo utilizado os comandos .pop() para remoção e .append() para adição.

***O LIFO aparece nesse código:***

'filme["estoque"].pop()'

Localizado no def de alugar filmes, livros e HQs


***E nesse código:***


'''
    for _ in range(filme_quantidade):
        novo_exemplar = len(filme["estoque"]) + 1
        filme["estoque"].append(novo_exemplar)
'''

Localizado no def para devolução de filmes, livros e HQs.

---
