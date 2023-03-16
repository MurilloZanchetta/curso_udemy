# Python Dunder Methods __repr__ e __str__
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

# __str__ retorna uma string
    def __str__(self):
        return f'({self.x}, {self.y})'


# __repr__ retorna uma string mais formal, mas usada entre devs
    def __repr__(self):

        # Esses dois modos abaixo chamam iguais
        # class_name = self.__class__.__name__

        # type(self).__name__ chama o nome da classe utilizada 'Ponto'
        class_name = type(self).__name__

        # Usamos o f'abaixo e a cada self.x usamos um !r para retornar
        # em repr
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'


p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p2))
print(f'{p2!r}')