# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

# Usamos o os.path.join para juntar a nossa string, ja adicionando a / 
# automaticamente
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
print()
print()
print()

# O os.path.split() é usado para separar a nossa path em tuplas
print(os.path.split(caminho))
print()
print()
print()


diretorio, arquivo = os.path.split(caminho)

# O os.path.splitext() separa o arquivo e a extensão do seu diretorio
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
print()
print()
print()

# O os.path.exists() verifica se ja existe o arquivo
print(os.path.exists(''))
print()
print()
print()

# O os.path.abspath('.') com um . dentro dos (), mostra o nome do arquivo 
# que você está aberto
print(os.path.abspath('.'))
print()
print()
print()
print(caminho)
print()
print()
print()
print('basename')

# O os.path.basename() retorna o seu nome. como por exemplo:
# os.path.basename(caminho) retorna arquivo.txt
print(os.path.basename(caminho))
print()
print()
print()

# O os.path.basename() retorna o seu nome. como por exemplo:
# os.path.basename(diretorio) retorna curso
print(os.path.basename(diretorio))
print()
print()
print()

# O os.path.dirname() retorna o nome do diretorio
print(os.path.dirname(caminho))