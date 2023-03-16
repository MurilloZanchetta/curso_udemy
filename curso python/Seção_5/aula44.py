# Classes decoradoras (Decorator classes)



# Criamos essa classe para ser decoradora
class Multiplicar:

    # fizemos essa função retornando o valor multiplicador
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

# Tivemos que fazer a função __call__ retornando o valor  func
# e fizemos uma função interna retornando *args, **kwargs
    def __call__(self, func):
        def interna(*args, **kwargs):

            # Criamos a variavel resultado para retornar o
            # valor de resultado * self._multiplicador
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

# Decoradores de class deve começar com a letra maiuscula
@Multiplicar(2)

# Fizemos a função soma retornando x + y e usamos o decorador para retornar 
# a multiplicação ro resultado de x + y
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)