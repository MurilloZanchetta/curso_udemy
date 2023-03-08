lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
        
print(lista)
print()

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)
print()

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)

'''
Eu criei um vídeo gratuito falando muito mais sobre list comprehension
 tirando como base as dúvidas desse curso. 
Veja em https://youtu.be/1YbTDczvqco
'''