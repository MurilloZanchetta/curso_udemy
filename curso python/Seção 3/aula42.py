'''
a função count funciona apenas em strings. Essa função é usada 
para contar as letras introduzidas na váriavel "frase"

'''




frase = 'O dia está muito iluminado hoje, pois estamos no verão. \
    e isso causa o aumento de temperatura e da absorção de luz solar'

i = 0  # Variável i usado para representar a condição da qtd de letras presente na variável "frase"
qtd_apareceu_mais_vezes = 0 # variavel usada para contar quantas x determinada letra apareceu
letra_apareceu_mais_vezes = '' #variavel para representar no terminal a letra mais usada na frase

while i < len(frase): 
# Condição (i) tem que ser introduzida com o sinal de < para o len(frase), que representa 
# o numero de cada letra

    letra_atual = frase[i] # função criada para realizar o if logo a seguir... 

    if letra_atual == ' ':
         # if usado para o código não contar os espaços que contem em "frase", 
         #r usando a expressão (i+= 1) antes do continue para o codigo não bugar e continuar contando as letras
         # seguintes, pulando apenas os espaços
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    #Variavel usada para saber a letra que apareceu mais vezes 

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

        #if usado para o codigo interpretar dentro da frase inteira, qual str apareceu mais vezes,
        #por isso usado o sinal de < para a variavel "mais_vezes" e a "mais vezes atual"
        #usando assim o sinal de = para a mesma expressão após os : e o sinal de = para "letra_mais_vezes e
        # letra atual"


    i += 1 #usado novamente para contar as letras, já sem os espaços aparecer

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)