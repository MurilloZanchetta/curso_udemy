# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0 # Essa variável  serve para enumerar seus acertos
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    # Esse for esta sendo utilizado para aparecer a pergunta para a pessoa

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

# foi criada a variavel opcoes para aparecer na tela as opções que contém
# de respostas, o for foi criado com o [i] e opcao + o enumerate para
# aparecer as opçoes enumeradas.

    escolha = input('Escolha uma opção: ')

    # isso permite que a pessoa escolha uma opção

    acertou = False # aqui a resposta começa como errada
    escolha_int = None # aqui começa como none
    qtd_opcoes = len(opcoes) # variavel len criada para a pessoa não escolher 
                             # um número maior que as opções

    if escolha.isdigit(): # esse if escolha.isdigit é para conter apenas numeros
        escolha_int = int(escolha) # Aqui transforma sua escolha em numeros int.

    if escolha_int is not None: # Aqui funcionará se o escolha_int for verdadeiro
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            # esse if serve para vc digitar algo maior q zero e menor q as opçoes 
            # permitidas
            if opcoes[escolha_int] == pergunta['Resposta']:
                # Se caso a pessoa marcar a resposta correta, esse if
                # entrará em ação para dizer que acertou a resposta
                acertou = True # aqui torna a resposta valida

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

        # Esse if serve ´para contar quantas perguntas vc acertou

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')