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

soma = 2 + 2
multiplicação = 5 * 5
divisão = 10 / 2

for soma in perguntas:
    escolha =  print(input('Opções 1, 3, 4, 5: ' ))

    if escolha == 4:
        print('Você acertou')

    else:
        print('Você errou')

        


                