from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

# __post_init__ é usado logo após o init do dataclass
    def __post_init__(self):
        print('POST INIT')

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    p1.nome_completo = 'Maria Helena'
    print(p1)
    print(p1.nome_completo)