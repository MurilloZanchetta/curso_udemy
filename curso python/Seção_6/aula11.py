# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count
# Importamos o count para contar os arquivos


# os.path.join para juntar 
caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')

# Criamos a variavel counter para retornar o interavel count()
counter = count()

# Criamos esse for com as variaveis root, dirs e files e  usamos  o
# os.walk para navegar de caminhos de forma recursiva
for root, dirs, files in os.walk(caminho):
    
    # Usamos o next(counter) para ir contando de 1 em 1 a cada arquivo
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)


    # Criamos a variavel dir_ que esta em dirs, e no print demos um espaço
    # dentro de ' ', depois usamos a variavel the_counter que usa o next(counter)
    # e depois usamos uma str para indicar que será o diretorio e colocamos a 
    # variavel dir_
    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)


    # Criamos a variavel file_ que esta em files
    for file_ in files:

        # Criamos a variavel caminho_completo_arquivo que foi usado
        # o os.path.join juntanto o root com o file_
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)

        
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)