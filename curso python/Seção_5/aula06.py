# Atributos de classe
class Pessoa:
    # Criamos a variavel ano atual como atributo
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Esse metodo está executando a função de diminuir o ano atual
    # pela idade da pessoa
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Murillo', 19)
p2 = Pessoa('Isa', 18)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())