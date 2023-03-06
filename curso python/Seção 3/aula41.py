""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break #usado para interromper o loop while

    # função do if é parar assim que o loop achar o espaço na frase digitada

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')


#toda vez que ocorrer um break antes do "else", o comando else não será executado....

#caso não tenha break o comando else será executado logo apos o seu while encerrar