"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
#del  lista[2]        #"del" é usado para deletar item da sua lista, como no exemplo: "del lista[2]"
# print(lista)
#print(lista[2])
lista.append(50)       #Append é usado para adicionar itens ao final da sua lista
lista.pop()            #Pop é usado para remover o último indice da sua lista ou outro que escolher
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)   # Nesse caso o "pop(3)" está removendo o indice que está localizado na posição 3
print(lista, 'Removido,', ultimo_valor)