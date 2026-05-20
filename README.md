=========IDEIA DO PROJETO=========

O Sistema de Locadora é um projeto desenvolvido em Python com o objetivo de gerenciar o cadastro e o controle de filmes, livros e HQs em uma locadora. O programa foi criado para praticar conceitos básicos e intermediários da linguagem Python, utilizando organização em múltiplos arquivos e estruturas de dados.

O sistema possui funcionalidades como cadastro de filmes, livros e HQs, visualização dos itens cadastrados, alteração de informações, exclusão de cadastros, controle de estoque, aluguel de filmes e devolução de exemplares. Além disso, o programa informa se determinado item possui estoque disponível ou se está esgotado.

O projeto foi dividido em quatro arquivos principais:

main.py: responsável pelo menu principal e pela interação com o usuário.
tarefas.py: contém as funções principais do sistema, como cadastro, aluguel, devolução, alteração e exclusão.
utils.py: guarda listas, funções auxiliares e geração de IDs aleatórios.
dados.py: armazena dados fixos do sistema, como tuplas de status de estoque.


=========RECOMENDAÇÕES=========
O projeto deve ser rodado em python 3.10 ou superior.


=========O QUE FOI USADO?=========

Durante o desenvolvimento foram utilizados conceitos como:

Funções
Listas
Dicionários
Tuplas
Estruturas condicionais (if, elif, else)
Estruturas de repetição (while)
Tratamento de erros com try e except
Organização modular em vários arquivos Python
Estrutura de pilha utilizando pop() e append()

O sistema também utiliza IDs aleatórios para identificar cada item cadastrado. Os estoques são armazenados em listas, permitindo adicionar e remover exemplares conforme o aluguel ou devolução dos itens.

=========COMO RODAR?=========

Para executar o programa, basta abrir o terminal na pasta do projeto e utilizar o comando:

python main.py

Após iniciar o sistema, o usuário poderá navegar pelo menu e escolher as funcionalidades desejadas.

Este projeto foi desenvolvido para fins acadêmicos, com foco no aprendizado de lógica de programação, manipulação de estruturas de dados e organização de projetos em Python.
