# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está ligando para o número', self.phone)
        return 'Murillo Recusou'


call1 = CallMe('19 99391-3048')
retorno = call1('Ramon dino')
print(retorno)