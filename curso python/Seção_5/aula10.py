# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Usamos  @classmethod faz com o que eu possa chamar minha  classe
    # sem passar o self
    @classmethod

    # usamos o  cls no lugar de self 
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    # Isso permite que criamos valores fixos para a nossa operação
    # Como no exemplo: cls(nome,50), ou seja todos terão 50 anos
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod

    # Isso permite que criamos valores fixos para a nossa operação
    # Como no exemplo: cls('Anônima',idade), ou seja todos serão anonimos
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()