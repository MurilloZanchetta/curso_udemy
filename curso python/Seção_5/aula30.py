# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

# Criamos uma class Notificação abstrata
class Notificacao(ABC):

    # Fizemos um __init__ com um valor mensagem
    def __init__(self, mensagem):

        # self.mensagem retorna o valor mensagem
        self.mensagem = mensagem

    # fazemos esse @abstractmethod para torna-los abstratos
    @abstractmethod

    #Criamos essa função para enviar as notificações
    # usamos -> bool para indicar aos devs, que estamos retornando
    # True ou False
    def enviar(self) -> bool: ...

# Criamos  a class NotificacaoEmail com o () retornando =   
# a super classe (Notificacao):
class NotificacaoEmail(Notificacao):

    # usamos -> bool para indicar aos devs, que estamos retornando
    # True ou False
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)

        # Retornamos True pois por padrao está em None, ai para n quebrar
        # o código, nós retornamos o True
        return True


# Criamos  a class NotificacaoSMS com o () retornando =   
# a super classe (Notificacao):
class NotificacaoSMS(Notificacao):

    # usamos -> bool para indicar aos devs, que estamos retornando
    # True ou False
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)

        # Retornamos True pois por padrao está em None, ai para n quebrar
        # o código, nós retornamos o True
        return True

# Fizemos o Polimorfismo aqui nesta função...
# criamos o def notificar retornando o valor notificação: Notificação
def notificar(notificacao: Notificacao):

    # Criamos a variavel notificacao_enviada = notificacao.enviar()
    notificacao_enviada = notificacao.enviar()

    # criamos o if para se for True retornar ('Notificação enviada')
    # e o else retorna caso for false
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)
