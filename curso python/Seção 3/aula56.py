'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.'''


lista = []   # Variável lista com um [] vazio, para mostrar que está na função list

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # criamos uma variavel "opção" com as palavras inserir, apagar e listar. Com o [i], [a], [l]
    # sendo a letra para usar, com isso criamos if e elif para salvar essas letras

    if opcao == 'i':   # Criamos a função [i] para inserir novos valores
        
        valor = input('Valor: ')
        lista.append(valor)

    # Criamos a função [a] para apagar algum valor de sua lista
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

            
            #Criamos esse try para transformar a 1° resposta em número inteiro e na 2° é deletado o seu valor
            #na função lista...
            #logo depois, foi criado o except pra previnir erros de digitação e nao quebrar o código,
            #então quando acontece o erro do except, ele dará um print na tela e voltará para a opção
            #de escolher entre Inserir, Apagar e Listar 
            


    elif opcao == 'l':       # Criamos a função [l] para listar os seus novos valores
        

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')

        # For criado para pegar o valor inserido, e usando a função 'enumerate', adiciona o número
        # do indice em cada produto da lista.

        # Else criado apenas para um backup se caso dê erro.
