import sys # tem que importar o sys para usar o sys.getsizeof

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# sys.getsizeof serve para ver quantos bytes está sendo usado para o comando

print(generator)

for n in generator:
     print(n)

     # for usado para contar o generator expression