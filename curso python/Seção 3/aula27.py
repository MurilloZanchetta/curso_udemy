"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])

print(variavel[0:9:2])

print(variavel[0:10:4])

print(variavel[0:len(variavel):])

print(len(variavel))

print(len(variavel[5]))

print(len(variavel[0:5]))
