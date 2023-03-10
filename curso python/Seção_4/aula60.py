# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
#def recursiva(inicio=0, fim=4):
# import sys

    #print(inicio, fim)
# sys.setrecursionlimit(1004)

    # Caso base
    #if inicio >= fim:
        #return fim

    # Caso recursivo
    # contar até chegar ao final
    #inicio += 1
    #return recursiva(inicio, fim)
# def recursiva(inicio=0, fim=4):

#     print(inicio, fim)

#print(recursiva())
#     # Caso base
#     if inicio >= fim:
#         return fim

#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 1001))

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))


'''
estamos fazendo uma função fatorial de um número,como no exemplo =
5! = 5.4.3.2.1 = 120.

Temos que tomar cuidado com o limite re recursão to python, então se a gente quiser 
fatorar um número grande, como por exemplo o número 1000, devemos usar o seguinte
código:

import sys

sys.setrecursionlimit(1004) ai no entre () vc define o valor limite que
vc quer para o python
'''