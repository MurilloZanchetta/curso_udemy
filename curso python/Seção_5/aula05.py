# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    # esse método está sendo usado para filmar
    def filmar(self):
        if self.filmando: # se for verdadeiro irá retornar esse print
            print(f'{self.nome} JÁ está filmando...')
            return
        # ou irá retornar este outro print
        print(f'{self.nome} está filmando...')
        self.filmando = True

    # Esse método irá parar de filmar
    def parar_filmar(self):
        if not self.filmando: # se não for verdadeiro, irá retornar esse print
            print(f'{self.nome} NÃO está filmando...')
            return

        # Se for verdadeiro retornará esse print
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    # Esse método irá fotografar
    def fotografar(self):
        if self.filmando: # Se for verdade retornará esse print
            print(f'{self.nome} não pode fotografar filmando')
            return

        # Se for verdadeiro retornará esse print
        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()