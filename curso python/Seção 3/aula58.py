"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

# strip é usado para remover os espaços da frase
# rstrip é usado para remover os espaços da direita
# lstrip é usado pare remover os espaços da esquerda

# no join vc terá que começar com uma str ''.join...
# E o join só funciona com interáveis, como por exemplo: str, listas e tuplas.