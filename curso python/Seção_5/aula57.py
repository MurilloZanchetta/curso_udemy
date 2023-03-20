# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import asdict, astuple, dataclass

# Importamos o asdict, astuple para trasformar a dataclass em dicionario
# e tuplas

@dataclass(repr=True)
@dataclass
class Pessoa:
    nome: str
    sobrenome: str

p1 = Pessoa('Murillo', 'Henrique')

# usamos o asdict() para trasformar a dataclass em dicionario
print(asdict(p1).keys())
print(asdict(p1).values())
print(asdict(p1).items())

# usamos o astuple() para trasformar a dataclass em tuplas
print(astuple(p1)[0])