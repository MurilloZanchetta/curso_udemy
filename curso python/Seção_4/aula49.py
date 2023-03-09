# Decoradores com parâmetros

# usamos None no nosso decorador, para utilizarmos depoiscom vaalores nomeados
def fabrica_de_decoradores(a=None, b=None, c=None): 
    def fabrica_de_funcoes(func): # esse def q irá fazer a função
        print('Decoradora 1')

        def aninhada(*args, **kwargs): # essa função pegara os valores nomeados
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs) # e irá fazer o resultado
            return res # aqui retorna na tela o resultado
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3) # Aqui é o nosso decorador
def soma(x, y): # e essa função esta fazendo a função de somar x + y
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)
# aqui utlizimos a lambda para criar a função de multiplicar

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)