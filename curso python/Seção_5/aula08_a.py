# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

# Variavel em maiusculas diz ao python para não mexer nela
CAMINHO_ARQUIVO = 'aula08.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]

# Esse metodo esta inserido para transformar o arquivo em json
def fazer_dump():
    # Aqui usamos a função para criar arquivo json
    with open(CAMINHO_ARQUIVO, 'w', encoding= 'utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        #json.dump cria o arquivo

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()