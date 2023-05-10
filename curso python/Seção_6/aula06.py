# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

#------------------------------------------------------------------------------#
import calendar

print(calendar.calendar(2023))
print()
print()
print(calendar.month(2023, 7))
print()
print()
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023, 7)
print(list(enumerate(calendar.day_name)))
print()
print()
print(calendar.day_name[numero_primeiro_dia])
print()
print()

# - Qual o nome e número do dia de determinada data weekday
print(calendar.day_name[calendar.weekday(2023, 7, ultimo_dia)])
print()
print()

# Criamos essa variavel week que esta em calendar.mothcalendar

# - Criar um calendário em si (ex.: monthcalendar)
for week in calendar.monthcalendar(2023, 7):

    # Criamos esse for interno para tirar os dias da variavel week
    for day in week:
        # fizemos esse if para a variavel day começar no 0
        if day == 0:
            continue
        print(day)