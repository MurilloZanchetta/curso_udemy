# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
# Importamos o 'os' para usar a função de limpar o terminal


# Essa função está sendo usada para listar as tarefas
def listar(tarefas):
    print()
    if not tarefas: # Se não for uma tarefa irá retornar esse print
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    
    # Esse for esta sendo usado para se caso for tarefa, ele retornar no terminal o nome da tarefa
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

# Essa função está sendo usada para desfazer uma tarefa
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas: # se n for tarefa irá retornar esse print
        print('Nenhuma tarefa para desfazer')
        return
    
    # Essa variavel usada com o pop é usada para apagar a ulltima str adicionada
    tarefa = tarefas.pop()
    # print para retornar q foi removida
    print(f'{tarefa=} removida da lista de tarefas.')

    # essa função adiciona no fim da lista uma str 
    tarefas_refazer.append(tarefa)
    print()

# Essa função está refazendo o indice apagado
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:  # se n for tarefa irá retornar esse print
        print('Nenhuma tarefa para refazer')
        return


    # Essa variavel esta refazendo o ultimo valor apagado pelo pop. Por isso utlizamos 
    # tarefas_refazer.pop().
    tarefa = tarefas_refazer.pop()


    # esse print retorna o valor adicionado
    print(f'{tarefa=} adicionada na lista de tarefas.')

    # Aqui acrescenta um valor na variavel tarefa
    tarefas.append(tarefa)
    print()

# essa função irá adicionar itens em sua lista
def adicionar(tarefa, tarefas):
    print()

    # Essa variavel esta feita com o 'tarefa.strip()' para retirar todos os espaços em volta
    tarefa = tarefa.strip()
    if not tarefa:  # se n for tarefa irá retornar esse print

        print('Você não digitou uma tarefa.')
        return
     
     # Esse print retorna o valor adicionado
    print(f'{tarefa=} adicionada na lista de tarefas.')


    # Esse acrescenta o item no final da sua lista produzida
    tarefas.append(tarefa)
    print()

# 2 variaveis vazias para adicionar valor que desejar
tarefas = []
tarefas_refazer = []



while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    # if produzido para quando for listar, retornar  tarefas
    if tarefa == 'listar':
        listar(tarefas)
        continue

    # Elif produzido para desfazer, então temos que criar 'desfazer(tarefas, tarefas_refazer)'
    # para excluir o item e depois retornar tarefas para vir a lista nova
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    # Elif produzido para refazer, então temos que criar 'refazer(tarefas, tarefas_refazer)'
    # para refazer o item e depois retornar tarefas para vir a lista atualizada
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    # elif criado para usar o comando que importamos: os.system('clear'), para ele limpar o terminal
    # quando esse elif for executado
    elif tarefa == 'clear':
        os.system('clear')
        continue


    # se nada acontecer ele adiciona um item novo em sua lista e retorna tarefas com a lista atualizada
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue