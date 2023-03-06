"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número:  ')

try:
    num_par_impar_int = float(numero) 
    num_par_impar = num_par_impar_int % 2 == 0
    num_par_impar_text = 'Impar'
    

    if num_par_impar:
        num_par_impar_text = 'Par'

    print(f'O número {num_par_impar_int}, é {num_par_impar_text}')

except:
    print('Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Digite um número inteiro:  ')

try:
    
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    
    elif hora >= 18 and hora <= 23:
        print('Boa noite')

    else:
        print('Não conheço esse Número inteiro ')

        
except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')