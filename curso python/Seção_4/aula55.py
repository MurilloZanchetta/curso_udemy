# groupby - agrupando valores (itertools)
from itertools import groupby
# groupby só pode ser usado com o  import

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# Essa função foi usada para organizar os alunos pela nota
def ordena(aluno):
    return aluno['nota']

# Usamos o key= ordena para separar os alunos por notas
alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)
# groupby criado para criar grupos por notas
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo: # for  criado para cada nome ficar abaixo dos outros
        print(aluno) # esse for foi criado para separar cada aluno