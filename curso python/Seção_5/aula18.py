# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

# Criamos essa função para inserir endereços
    def inserir_endereco(self, rua, numero):
        # usamos o self.enderecos.append(Endereco()) sendo que a  classe Endereço
        # deve estar dentro do append
        # append adiciona 1 valor por vez
        self.enderecos.append(Endereco(rua, numero))


# função criada para adicionar o  self.ederecos em endreco 
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    # Função criada para listar os endereços com a rua e com o numero,
    # Usamos o for para listar o endereço do self.enderecos
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


    # função criada para apagar o self.nome no final do codigo
    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

 # Criamos a class Endereco e colocamos essa função para apagar o self.rua e self.numero,
 # logo após do self.nome ser apagado
    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1


print(endereco_externo.rua, endereco_externo.numero)
print('######################## AQUI TERMINA MEU CÓDIGO')

