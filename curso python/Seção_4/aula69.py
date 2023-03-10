import json 
# temos que importar jsonpara usar

# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula69.json', 'w', encoding='utf8') as arquivo:
    json.dump(   # json.dump = Gera um arquivo json
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)  # json.load: carrega o arquivo json no py.
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])