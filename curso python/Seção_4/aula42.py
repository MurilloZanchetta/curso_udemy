import importlib #importlib serve para recarregar o módulo importado

import aula42_m

print(aula42_m.variavel)

for i in range(10):
    importlib.reload(aula42_m) #importlib.reload recarrega o modulo
    print(i)

print('Fim')