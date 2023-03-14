class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:

    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    
    def __init__(self, nome):
        self.nome = nome

carro = Carro('Onix')
chevrolet = Fabricante('Chevrolet')
motor_1_0 = Motor('1.0')
carro.fabricante = chevrolet
carro.motor = motor_1_0
print(carro.nome, carro.fabricante.nome, carro.motor.nome)
print()

carro_2 = Carro('Jeep Compass')
jeep = Fabricante('Jeep')
motor_turbo = Motor('TD350 TURBO DIESEL')
carro_2.fabricante = jeep
carro_2.motor = motor_turbo
print(carro_2.nome, carro_2.fabricante.nome, carro_2.motor.nome)
print()

saveiro = Carro('Saveiro')
volkswagen = Fabricante('Volkswagen')
motor_1_6 = Motor('1.6')
saveiro.fabricante = volkswagen
saveiro.motor = motor_1_6
print(saveiro.nome, saveiro.fabricante.nome,saveiro.motor.nome)
