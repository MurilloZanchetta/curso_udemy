from dataclasses import dataclass, field

# fields retorna as configurações dos campos

#field configura os seus campos na dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    nome: str = field(
        default='MISSING', repr=True
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)



p1 = Pessoa()
# print(fields(p1))
print(p1)