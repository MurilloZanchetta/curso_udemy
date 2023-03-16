class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

# Essa função __add__ soma o p1 com p2
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

# Essa função __gt__ mostra se p1 > p2
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


# essse if esta  retornando o nome == o main
if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)