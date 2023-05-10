# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os
# Criamos uma variavel juntando nossas str com o os.path.join
caminho = os.path.join('/Users', 'julio', 'Desktop', 'curso python')

# criamos um for para listar o  nosso caminho
for pasta in os.listdir(caminho):
    # criamos uma variavel caminho_completo usando o join para justar
    # o caminho e a pasta 
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)


    # Criamos esse if, para se caso não for diretorio, continuar
    if not os.path.isdir(caminho_completo_pasta):
        continue

        # Criamos outro for tirando o item de dentro da variavel 
        # caminho_completo_pasta com o os.listdir()
    for item in os.listdir(caminho_completo_pasta):
        print('  ', item)