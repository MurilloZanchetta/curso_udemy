from datetime import datetime
from pytz import timezone

# Usamos o timezone para ver exatamente a hora do país que escolhermos
data = datetime.now(timezone('Hongkong'))
print(data)
print()
print()

# Usamos o tzinfo = timezone() para escolhermos o pais, a data e as horas 
data_2 = datetime(2022, 4, 20, 7, 49, 23, tzinfo = timezone('Hongkong'))
print(data_2)
print()
print()

data_3 = datetime(2023, 3, 21,  11, 59, 00)
# Usamos  o timestamp() para mostrar quantos segundos tem de 1970 até os dias
# atuais
print(data_3.timestamp())  # Isso está na base de dados
print()
print()

# Usamos o fromtimestamp() para converter os segundos em data novamente
print(datetime.fromtimestamp(1679410740.0))
print()
print()



data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'



#data = datetime.strptime(data_str_data, data_str_fmt)

# data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)