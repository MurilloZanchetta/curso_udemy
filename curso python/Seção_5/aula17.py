# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []

    # essa função irá calcular o total da soma do preço de cada produto
    def total(self):
        # um return com soma(sum) com a variavel p.preço, para retornar o valor dos produtos
        # e somar os preços
        return sum([p.preco for p in self._produtos])


    # Essa função serve para adicionar novos produtos, usamos o * para quebrar a tupla
    def inserir_produtos(self, *produtos):
# Abaixo temos 3 maneiras diferentes para adicionar os produtos

        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    # essa função serve para listar os seus produtos
    def listar_produtos(self):
        print()
        # Usamos um for para listar o produto dentro do self._produtos
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


# criamos outra classe chamada produto, com 2 valores: nome e preco
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())