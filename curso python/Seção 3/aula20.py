primeiro_valor = input('Digite um valor:  ')
segundo_valor = input('Digite outro valor:  ')


if primeiro_valor > segundo_valor:
    print('O valor', primeiro_valor, 'é maior que o valor', segundo_valor)

elif primeiro_valor == segundo_valor:
    print('O valor', primeiro_valor, 'é igual ao valor', segundo_valor)

elif primeiro_valor < segundo_valor:
    print('O valor', primeiro_valor, 'é menor que o valor', segundo_valor)



                                        #CORREÇÃO DO EXERCÍCIO

'''primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
'''