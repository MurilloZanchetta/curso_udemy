# Funções decoradoras e decoradores com métodos

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

# CRIAMOS ESSA FUNÇÃO PARA SER UM DECORADOR
def meu_planeta(metodo):

    #CRIAMOS ESSA FUNÇÃO INTERNA RETORNANDO A VARIAVEL
    # METODO(SELF, *ARGS, **KWARGS)
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

# CRIAMOS ESSE IF PARA RETORNAR A FRASE 'Você está em casa'
# QUANDO O IF SER IGUAL A TERRA
        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


# USAMOS O DECORADOR MEU PLANETA AQUI
    @meu_planeta

    # CRIAMOS ESSA FUNÇÃO PARA RETORNAR A FRASE f'O planeta é {self.nome}'
    def falar_nome(self):
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())