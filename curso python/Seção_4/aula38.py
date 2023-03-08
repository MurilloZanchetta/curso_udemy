# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError): # silencia o erro
    print('NameError, ImportError')
else: # Será executado se o try não der erro
    print('Não deu erro')
finally: # Sempre será executado, independente do erro
    print('FECHAR ARQUIVO')


'''
try nunca pode ficar sozinho.

jeitos que podem usar o try:

try e except
try e else
try e finally
try, except e else
try, except e finally
try, except, else e finally
try e mais de um except
'''
