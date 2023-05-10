# locale -a para listar idiomas de outros países
# locale -a | grep 'pt', irá buscar todos os paises que utlizam a linguagem pt 
# Esses dois comandos acima é usado no terminal

#------------------------------------------------------------------------------#


# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale
# Importamos o locale

# usamos o locale.setlocale() e dentro do () usamos o locale.LC_ALL, para mudar 
# Tudo para o seu idioma local
locale.setlocale(locale.LC_ALL, 'fr_ML.utf8')

print(calendar.calendar(2023))

print()


# Usamos o locale.getlocale() para colocar o local no seu terminal
print(locale.getlocale())