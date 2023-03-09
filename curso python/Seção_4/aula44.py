# copy, sorted, produtos.sort
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos= [
     {**aumento, 'preco': round (aumento['preco'] * 1.1, 2)}
       for aumento in copy.deepcopy(produtos)             
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_decrescente = sorted(
    copy.deepcopy(produtos),
    key=lambda aumento: aumento['nome'],

    reverse= True
)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda aumento: aumento['preco']
    
    #key= lambda usado para strings
)






print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_decrescente, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
