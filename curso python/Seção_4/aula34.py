# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        # yield serve para pausar a execução onde vc designar
        n += 1
    
        if n >= maximum:
            return 'ACABOU'


gen = generator(maximum=100)
for n in gen:
    
    print(n)