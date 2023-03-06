# for é usado geralmente para recursos que vc geralmente conhece o inicio ou o fim


# O (i) está sendo usado para contar as linhas
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')  # Esse if esta sendo usado para quando o codigo chegar no 2 ele pular direto \
                                    # para o 3
        continue

    if i == 8:
        print('i é 8, seu else não executará')   # if usado para qnd o (i) chegar no 8, o loop finalizar.
        break

    # O (J) esta sendo usado para contar colunas

    for j in range(1, 4):
        print(i, j)
else:
    print('For completo com sucesso!')

    # caso o codigo não chegue em 8, onde acontece o break.... o Else poderá aparecer na tela.
