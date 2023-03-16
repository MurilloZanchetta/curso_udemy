# Funções decoradoras e decoradores com classes

# Criamos essa função para retornar o nome da classe e um dict
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

# Criamos essa função para adicionar os reps nas classes
def adiciona_repr(cls):
    # usamos cls.__repr__ = meu_repr para retornar o cls.__repr__ na
    # função de cima.
    cls.__repr__ = meu_repr

    # Aqui retornamos o cls
    return cls

# Aqui temos o decorador de nossas classes
@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)