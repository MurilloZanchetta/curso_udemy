# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence

# Para importarmos o  Sequecence, devemos usar o from collections.abc

# Criamos a class MyList herdando de Sequence
class MyList(Sequence):

    # Criamos essa função retornando o self.data = dict{}, o self._index = 0
    # e o self._next_index = 0  
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0


# Criamos a função append para adicionar os valores em nossa lista
# Usamos o * para adquirir todos os valores a direita do 1º valor
    def append(self, *values):

        # Criamos esse for para pegar cada valor de *values para adicionar
        # em nossa lista. Retornamos o self._data [self._index] com o 
        # self.index dentro da lista do self._data.
        # E retornamos o self._index += 1 para adicionar o numero em valores
        # novos
        for value in values:
            self._data[self._index] = value
            self._index += 1


# Criamos essa função __len__ para enumerar e retornar o self._index
    def __len__(self) -> int:
        return self._index

# Criamos a função __getitem__ retornando o valor de index dentro da lista []
#  self._data[index]
    def __getitem__(self, index):
        return self._data[index]


# Criamos  o __setitem__ retornando o index e o value em self._data...

    def __setitem__(self, index, value):
        self._data[index] = value


# Criamos essa função __iter__ (interavel) retornando o proprio self
    def __iter__(self):
        return self

# Criamos a função __next__ e retornamos um if
    def __next__(self):

        # Criamos o if para o self._next_index ser >= self._index
        # self._next_index = 0
        if self._next_index >= self._index:
            self._next_index = 0

            # se for false, retorna esse erro
            raise StopIteration

    # Criamos a variavel value = self._data com o self._next_index estando 
    # dentro de sua lista []
    # colocando o self._next_index += 1, retornando assim o value
        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))

    # Criamos esse for para printar todos os itens dentro da lista.
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')