def soma(x,y):
    return x + y


def multiplica(x,y):
    return x * y



def executa(funcao, x):
    def interna (y):
        return funcao(x,y)
    return interna


soma_com_cinco = executa(soma, 5)
soma_com_sete = executa(soma, 7)
soma_com_cinquenta = executa(soma, 50)
multiplica_por_dez = executa(multiplica, 10)
multiplica_por_doze = executa(multiplica, 12)
multiplica_por_quarenta_tres = executa(multiplica, 43)

print(soma_com_cinco(55))
print()
print(soma_com_sete(65))
print()
print(soma_com_cinquenta(296))
print()
print(multiplica_por_dez(5))
print()
print(multiplica_por_doze(33))
print()
print(multiplica_por_quarenta_tres(14))
