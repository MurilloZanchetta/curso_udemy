# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)


    # metodo criado para retornar o print que o leao está comendo
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    # esse metodo esta criado para retornar o nome do alimento 
    # e retorna o valor de alimento
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
        # retornamos o valor do *kwargs ou *args para o metodo def comendo


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))