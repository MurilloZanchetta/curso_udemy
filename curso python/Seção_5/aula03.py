# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:


    # O 1º parametro sempre deverá ser o self
    def __init__(self, nome):
        self.nome = nome

    # criamos outro metodo para acelerar
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome.upper())
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
print(celta.nome.upper()) # upper deixa tudo em maiusculo
celta.acelerar()
Carro.acelerar(celta)