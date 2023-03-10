# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    # Aqui passamos uma lista= None, para criar listas próprias
    if lista is None:
        lista = []
        # Criamos essa lista vazia paraa toda atualização no código
        # criar uma lisra nova automaticamente
    lista.append(nome)
    # Aqui adiciona o nome na lista
    return lista  # aqui retorna a lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)