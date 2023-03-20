import enum
# Temos que importar o enum para usar.


# Criamos a classe  Direcoes herdando de enum.Enum
class Direcoes(enum.Enum):

    # Usamos o enum.auto() para contar os valores progressivamente
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


# Criamos essa função mover retornando o valor direcao = Direcoes
def mover(direcao: Direcoes):

    # Criamos esse if, para se não for a instancia (direcao, Direcoes)
    # Ele retorna o raise ValueError
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)