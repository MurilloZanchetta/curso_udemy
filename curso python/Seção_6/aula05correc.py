# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

#------------------------------------------------------------------------------#



from datetime import datetime
from dateutil.relativedelta import relativedelta

# Importamos o datetime e relativedelta para configurarmos as datas


# O Py permite usar _ para ter uma leitura facilitada em numeros int grande
# criamos a variavel valor_total = o valor total que ela emprestou
# criamos a variavel data_emprestimo, formatando com o datetime (2020, 12, 20)
#criamos a variavel data_anos, formatando com o relativedelta (years= 5)...
# mostrando o total de anos que ela levou para pagar tudo
# criamos a variavel data_final somando a data_emprestimo + data_anos
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

# criamos a variavel data_parcelas com o valor de uma lista [] vazia
# e criamos a variavel data_parcela = data_emprestimo
data_parcelas = []
data_parcela = data_emprestimo

# ai criamos um while com a variavel data_parcela sendo < que a data_final
# ou seja, o while ira encerrar assim que chegar na data final.
while data_parcela < data_final:

    # usamos a variavel data_parcelas que é = [], para adicionar os valores
    # da variavel data_parcela dentro da sua lista []
    data_parcelas.append(data_parcela)

    # Usamos a variavel data_parcela para somar 1 mes a cada passagem,
    # Ou seja, data_parcela += relativedelta(months=+1), adicionando assim
    # 1 mes a cada nova parcela
    data_parcela += relativedelta(months=+1)

# Criamos a variavel numero_parcelas sendo igual ao len(data_parcelas)
# para o numero_parcelas n exceder o numero das datas
numero_parcelas = len(data_parcelas)

# E criamos  a variavel valor_parcela para 
# dividirmos o valor_total / numero_parcelas
valor_parcela = valor_total / numero_parcelas

# Criamos esse for para separar a data de cada mes dentro da
# lista data_parcelas
for data in data_parcelas:

    # Usamos o strftime para transformar a data em str e podermos alterar o
    # formato dela, como no exemplo a seguir : 21/03/2023... E usamos
    # o fstring para trazer o valor da parcela de cada mes sendo formatado
    # pelo {valor parcela:,.2f}, usamos a virgula para separar o valor dos 0
    # e usamos o 2f para ter apenas 2 casas decimmais após o .
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()


# Fizemos esse print para falar quantos R$ ela pegou emprestado, quantos anos
# ela levou para pagar, em quantos meses deram esses 5 anos, o numero de suas
# parcelas e o valor de cada parcela
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)