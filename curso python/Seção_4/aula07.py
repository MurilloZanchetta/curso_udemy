def multiplicar (*args):
    total = 1

    for numero in args:
        total *= numero
    return total
    
multiplicacao = multiplicar (1, 2, 3, 4, 5, 6, 7)

print(multiplicacao)


def par_impar (numero):

    if numero % 2 == 0:
        print(f'O numero {numero} e Par' )
    
    else:
        print(f'O numero {numero} e Impar')
    
print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(5))
print(par_impar(6))
print(par_impar(7))
print(par_impar(8))
print(par_impar(9))

