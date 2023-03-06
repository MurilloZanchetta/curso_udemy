"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

"""

qtd_linha = 30
qtd_coluna = 30

linha = 1

while linha <= qtd_linha:
    coluna = 1

    while coluna <= qtd_coluna:


        print(f'{linha= }, {coluna= }')

        coluna += 1
    linha += 1

print('ACABOU')