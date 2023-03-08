# Métodos úteis:
# add, update, clear, discard

# add - adiciona 1 item
# update - adiciona vários intens
# clear - limpa o seu set
# discard - limpa um valor específico

s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
