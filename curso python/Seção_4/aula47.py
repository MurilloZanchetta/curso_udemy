# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func): 
    def interna(*args, **kwargs): # **kwargs serve para argumentos nomeados
        print('Vou te decorar')
        for arg in args: # esse for verifica se é str e retorna o resultado
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def inverte_string(string): # essa função serve para inverter a str
    return string[::-1] #Serve para a str começar de tras para frente


def e_string(param): # essa função serve para dizer que só aceita str
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
# esse if foi criado para retornar o erro quando o valor não for str

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)