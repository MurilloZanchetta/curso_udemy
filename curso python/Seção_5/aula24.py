# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)
class A:
    ...

    def quem_sou(self):
        print('A')


# B herda de A
class B(A):
    ...

    # def quem_sou(self):
    #     print('B')

# C herda de A
class C(A):
    ...

    def quem_sou(self):
        print('C')

# herança multipla é quando tem 2 ou mais classes dentro do ()
class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
# print(D.__mro__)

# .mro serve para vc ver a ordem que o python estábuscando as classes
print(D.mro())