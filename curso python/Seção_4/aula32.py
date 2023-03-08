# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)

    '''
    dir serve para descobrir todos os atributos que pode ser utilizado
    pela str

    hasattr serve para ver se tem algum atributo

    getattr serve para executar esse atributo
    '''
