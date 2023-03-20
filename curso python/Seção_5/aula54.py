# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass
@dataclass
class Pessoa:
    nome: str
    #idade: int
    sobrenome: str


# Podemos usar o property junto com a dataclass
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

# Fizemos o setter para a função nome_completo retornando o valor
    @nome_completo.setter

    # O nome, sobrenome retorna o valor. usamos o * antes do sobrenome
    # para tudo o que for digitado depois do nome, ser incluso no sobrenome.
    def nome_completo(self, valor):

        # Usamos o valor.split para separar o sobrenome do nome
        nome, *sobrenome = valor.split()
        self.nome = nome
        # Usamos o self.sobrenome = ' '. join para seprar o resto do sobrenome
        # com espaço.
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Murillo', 18)
    p2 = Pessoa('Murillo', 18)
    print(p1 == p2)
    p1 = Pessoa('Murillo', 'Henrique')
    p1.nome_completo = 'Murillo Henrique Zanchetta Quirino'
    print(p1)
    print()
    print('Agora utilizaremos o *sobrenome,  o split e o join')
    print()
    print(p1.nome_completo)