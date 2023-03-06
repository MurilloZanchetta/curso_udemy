"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'João',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

''' 
Podemos usar como no exemplo, uma variavel lista no quadrante [-3 ou 2] e mudar o seu valor original.
como por exemplo... na lista o str é João, e em baixo colocamos uma variavel especifica para essa str em nome Maria.
Após dar o print, automaticamente ele alterará na lista o nome de João para o nome Maria


o código list pode ser representado de duas formas: "list()" ou "[]"

'''

# Lembrando... a função "type()" diz qual é a classe da função.

# a função "upper()" deixa o str 100% maiuscula.