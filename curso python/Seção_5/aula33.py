#  exception_.add_note serve para vc adicionar notas no erro
# exception_.__notes__ = error.__notes__.copy() serve para 
# copiar a nota do erro anterior

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('você errou isso')
    raise exception_

def levantar():
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error