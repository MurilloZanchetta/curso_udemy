"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
#Murillo

nome = input('Digite seu Nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print('Seu nome é  ' f'{nome},')
    print('Seu nome invertido é  ' f'{nome[::-1]}')

    if nome ==' ': #Correção: if ' ' in nome:
        print('Seu nome contém espaços')

    else:
        print('Seu nome não contém espaços')

    print('Seu nome tem  ' f'{len(nome[0:])} LETRAS') #Correção: print(f'Seu nome tem {len(nome)} letras')
    print('A primeira letra do seu nome é  ' f'{len(nome[0])}') #Correção:  print(f'A primeira letra do seu nome é {nome[0]}')
    print('A última letra do seu nome é  ' f'{nome[-1]}') #Correção: print(f'A última letra do seu nome é {nome[-1]}')

# Faltou o comando else para caso não digitar Nome e Idade...

'''
else:
    print("Desculpe, você deixou campos vazios.")
'''


    
