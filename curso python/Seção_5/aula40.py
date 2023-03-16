# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager
# tivemos que importar o contextmanager



@contextmanager

# Usamos essa função para retornar o caminho_arquivo e o modo
def my_open(caminho_arquivo, modo):

    # Criamos o try para prevenir o erro
    try:
        print('Abrindo arquivo')
        #aqui usamos a variavel para abrir o arquivo
        arquivo = open(caminho_arquivo, modo, encoding='utf8')

        # Usamos o yield para pausar o arquivo e jogar no with
        yield arquivo
        # Usamos o except para colocar o erro na tela
    except Exception as e:
        print('Ocorreu erro', e)
        #  E usamos o finally para fechar o arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)