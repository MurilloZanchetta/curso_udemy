# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)

# Usamos o strptimme para colocar a formatação junto com a data
data = datetime.strptime('2023-03-21 14:50:00', '%Y-%m-%d %H:%M:%S')

# Usamos o strftime, para transformar em str e adicionar do jeito que pedimos
# Aqui aparecera o dia, mes e ano
print(data.strftime('%d/%m/%Y'))
# Aqui aparecera o dia, mes, ano, horas e minutos
print(data.strftime('%d/%m/%Y %H:%M'))

# Aqui aparecera o dia, mes, ano, horas, minutos e segundos
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# Aqui aparecerá o ano
print(data.strftime('%Y'), data.year)

# Aqui aparecerá o dia
print(data.strftime('%d'), data.day)

# Aqui aparecerá o mes
print(data.strftime('%m'), data.month)

# Aqui aparecerá a hora
print(data.strftime('%H'), data.hour)

# Aqui aparecerá o minuto
print(data.strftime('%M'), data.minute)

# Aqui aparecerá o segundo
print(data.strftime('%S'), data.second)