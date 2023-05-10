# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime

from dateutil.relativedelta import relativedelta
# Devemos importar o relativedelta para usa-lo

# Criamos a variavel fmt para formatar a nossa data
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('21/03/2023 14:08:00', fmt)
# delta = timedelta(days=10, hours=2)

# Criamos a variavel delta = relativedelta para formatar o data_fim e o 
# data_inicio
delta = relativedelta(data_fim, data_inicio)

# usamos o delta.days, para mostrar quantos dias de diferença entre o dia 20 e 
# dia 21....
# utilizamos o delta.years para mostrar quantos anos de diferença entre o ano
# de 1987 e 2023
print(delta.days, delta.years)






# print(data_fim - delta)
# print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))

# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)