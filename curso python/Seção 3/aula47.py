"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""




palavra_secreta = 'flamengo'   # Palavra que ganha no jogo
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    # Código para contar as tentativas de acerto

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    # Esse if está usando para impedir da pessoa escrever mais que 1 letra no código
    # Caso escreva mais q uma letra ele passa e volta ao inicio

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    # Esse if serve para salvar cada letra que é adicionada até acertar a palavra secreta

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

            # Esse for está criando a variavel "Letra_secreta"
            # e logo após o for, entramos com um if para em caso de acerto da letra
            # Ela mostrar a palavra no display
            # Caso erre a letra secreta, o else entra em ação colocando um '*' no lugar da letra secreta

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:



        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

    if palavra_formada == palavra_secreta :
        break

    # Esse if está sendo usado para quando a pessoa acertar a palavra secreta
    # o loop infinito sofrer um break. 


        # Essas 2 variaveis foram reproduzidas novamente dentro do while, pois quando
        # a pessoa ganhar, aparecer na tela a quantidade de vezes que ela tentou acertar
        # e aparece também a frase secreta completa
