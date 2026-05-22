# LOCADORA RSY

O tema escolhido para o projeto foi uma Locadora de Filmes. O sistema foi desenvolvido pelos estudantes Rodrygo Schadeck Gomes, Sara dos Santos de Oliveira e Yasmin Santos de Lima, alunos do 1° semestre da universidade BRAZ CUBAS, turma 012A do período da manhã.

---

## RESUMO DO PROJETO

O Sistema de Locadora é um projeto desenvolvido em Python com o objetivo de gerenciar o cadastro e o controle de filmes, livros e HQs em uma locadora. O programa foi criado para praticar conceitos básicos e intermediários da linguagem Python, utilizando organização em múltiplos arquivos e estruturas de dados.

---

### EXPLICAÇÃO CONCEITUAL

- FIFO(First in First out): O FIFO é o conceito de o primeiro item colocado na lista ser o primeiro a sair, como um sistema de fila no dia a dia. Adicionando um item em uma lista e retirando o primeiro item dessa mesma lista.  Sendo utilizado os comandos .pop() para remoção e .append() para adição.

<br>
<br>

**O FIFO aparece nesse código:**

'''
for _ in range(quantidade):
                    item['estoque'].pop()
                cliente['alugados'].append(item['titulo'])
'''

<br>

Que esta localizado na ***def de reservados_alugados().***

<br>
<br>

**E nesse código:**


'cliente['alugados'].pop(0)'

<br>

Que esta localizado na ***def de devolucao_alugados().***   

---

<br>

- LIFO(Last in First out): Ao contrario do conceito FIFO, o LIFO adiciona no ultimo lugar da lista e é retirado a partir do ultimo item da lista. Sendo utilizado sempre o exemplo de uma pilha de pratos em ensinos acadêmicos. Sendo utilizado os comandos .pop() para remoção e .append() para adição.

<br>
<br>

***O LIFO aparece nesse código:***

'filme["estoque"].pop()'

<br>

Localizado no def de ***alugar*** filmes, livros e HQs

<br>
<br>

***E nesse código:***


'''
    for _ in range(filme_quantidade):
        novo_exemplar = len(filme["estoque"]) + 1
        filme["estoque"].append(novo_exemplar)
'''

<br>

Localizado no def para ***devolução*** de filmes, livros e HQs.

---

### EXPLICAÇÃO DO DICIONARIO APLICADO NO PROJETO

<br>

No projeto foi utilizado o modo de implementação de um dicionário vazio a principio para que o usuário digitasse as informações pedidas nos campos de cadastro, e esses dados vão direto a etiquetas criadas dentro do dicionário afim de organização de dados, após essas etapas os dados vão para listas de seus respectivos tópicos, sendo eles: lista de filmes, livros, HQs e usuários.

<br>
<br>

'''
filme = {
        "id": chama_id(),
        "titulo": input("\nDigite o TÍTULO do filme: "),
        "genero": input("Digite o GÊNERO do filme: "),
        "estoque": criar_estoque(ler_numero("Digite a QUANTIDADE em ESTOQUE: ")),
        "estudio": input("Digite o nome do ESTÚDIO: "),
        "ano": ler_numero("Digite o ANO de LANÇAMENTO: ")
    }
'''

---

### EXPLICAÇÃO SOBRE LISTAS E TUPLAS UTILIZADAS NO PROJETO

<br>

A Lista foi utilizada para o armazenamento dos dados adicionados via usuário nos cadastros, sendo usada por ter a flexibilidade de mudanças, sendo indicado para auxiliar na logística da locadora.

<br>
<br>

A Tupla foi selecionada para informar somente quando os itens da locadora estiverem disponíveis para aluguel, sendo assim para dados imutáveis, contendo apenas os status Disponível e Não disponível para melhor controle de logística. 

---


### DIVISÃO DE ARQUIVOS

<br>

O projeto foi dividido em quatro arquivos principais:

<br>
<br>

**-main.py:** responsável pelo menu principal e pela interação com o usuário. 

**-tarefas.py:** contém as funções principais do sistema, como cadastro, aluguel, devolução, alteração e exclusão. 

**-utils.py:** guarda listas, funções auxiliares e geração de IDs aleatórios.

**-dados.py:** armazena dados fixos do sistema, como tuplas de status de estoque.

<br>

---


### MODO DE EXECUÇÃO

**O projeto deve ser rodado em python 3.10 ou superior. (É preferivel utilizar a versão mais atual do Python)**

<br>
<br>

Para executar o programa, basta abrir o terminal na pasta do projeto e utilizar o comando:

**python main.py**

<br>

Após iniciar o sistema, o usuário poderá navegar pelo menu e escolher as funcionalidades desejadas.

<br>
<br>

***Não são necessárias bibliotecas externas***

<br>
<br>

---


### FUNCIONALIDADES 

<br>

O sistema possui funcionalidades como cadastro de filmes, livros e HQs, visualização dos itens cadastrados, alteração de informações, exclusão de cadastros, controle de estoque, aluguel de filmes e devolução de exemplares. Além disso, o programa informa se determinado item possui estoque disponível ou se está esgotado, e foi implementado um código para a criação aleatória de "ID" para auxiliar nos sistemas para ações especificas e delicadas como: excluir, modificar, retirar e adicionar itens. 

<br>

---


### DIFICULDADES E APRENDIZADOS

<br>

A maior dificuldade ao longo do projeto foi ao implementar códigos novos, sendo eles recém-aprendidos ou não. Percebemos o impacto que um pequeno conjunto de códigos novos tem na lógica inteira de um código, tendo que reestruturar toda a lógica e o esqueleto do código diversas vezes, conforme o que queríamos entregar. Apesar das dificuldades, este projeto nos mudou como estudantes. A nossa visão de programação se tornou mais concreta, e observar como “simples” palavras e comandos, quando unidos, podem dar vida a projetos magníficos nos proporcionou sentimentos de entusiasmo e motivação.  

<br>

---



### OBSERVAÇÕES

<br>

Este projeto foi desenvolvido para fins acadêmicos, com foco no aprendizado de lógica de programação, manipulação de estruturas de dados e organização de projetos em Python.

<br>

---



