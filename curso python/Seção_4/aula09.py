# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def numero_2(*args):
    total = 2

    for numero1 in args:
        total *= numero1
    return total

def numero_3(*args):
    total = 3

    for numero3 in args:
        total *= numero3
    return total

def numero_4(*args):
    total = 4

    for numero4 in args:
        total *= numero4
    return total

print(numero_2(6))
print(numero_3(6))
print(numero_4(6))