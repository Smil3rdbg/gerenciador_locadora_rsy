bom dia rodrygo <3 
tkinter

from tarefas import cadastro_filme, cadastro_livro, cadastro_hq, ver_infos_filme, ver_infos_livro, ver_infos_hq, lista_filme, lista_livro, lista_hq, apagar_cadastrofilme

# tem q colocar ate a variavel da lista pra importar 


cadastro_filme() 



ver_infos_filme(lista_filme)


#APAGAR CADASTRO DE FILME
print('\n---------EXLUSÃO DE CADASTRO DE FILME---------')
print('1 - Sim\n2 - Não')
opcao_apagar = int(input('\nDeseja apagar o cadastro?: '))

if opcao_apagar == 1:
    apagar_cadastrofilme(lista_filme)
elif opcao_apagar == 2:
    print('Cadastro mantido!')
    ver_infos_filme(lista_filme)
else:
    print('Opção invalida!')






