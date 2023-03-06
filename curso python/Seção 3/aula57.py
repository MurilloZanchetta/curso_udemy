"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal    # Para funcionar o código "decimal.Decimal" devemos importar o "decimal"

numero_1 = decimal.Decimal('0.1')  #Essa função decimal.Decimal vc deverá colocar o float em string para dar
                                                        # o resultado da operação de uma forma precisa
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)   #Usando essa função, vemos que deu o resultado exato em 0.8
print(f'{numero_3:.2f}')  # Temos esse jeito de formatar
print(round(numero_3, 2))  # Temos esse jeito de formatar


#  O Round é usado para arrendondar numeros em float, deixando-os em números INT.
