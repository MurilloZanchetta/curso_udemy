import abc
# Importamos o abc para usar abstract


# Criamos a classe conta herdando de abc.ABC
class Conta(abc.ABC):
    
    # Criamos essa função init, retornando os valores :
    # agencia, conta, saldo = 0
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # Criamos o decorador @abc.abstractmethod, para tornar essas funções
    # abstratas
    @abc.abstractmethod

    # Criamos a função de sacar, para retirar dinheiro da conta
    def sacar(self, valor): ...

    # Criamos a função de depositar, para acrescentar dinheiro na conta
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    # Criamos a função detalhes para retornar uma mensagem str
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')

    # Criamos essa função para mostrar o class name e o attrs com o repr
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        # Aqui retornamos a fstring das variaveis
        return f'{class_name}{attrs}'

# Criamos a classe ContaPoupanca herdando da classe Conta
class ContaPoupanca(Conta):

    # Criamos a Função sacar retornando o valor
    def sacar(self, valor):

        # Criamos essa variavel subtraindo self.saldo - valor
        valor_pos_saque = self.saldo - valor

 # Criamos esse if para dizer q o valor_pos_saque precisa ser maior ou = a 0
        if valor_pos_saque >= 0:

        # Se essa condição for veridica, ele ira realizar a subtração de 
        # self.saldo -= valor
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')

            # Retornamos o valor de self.saldo
            return self.saldo

# Se o if for falso irá retornar esse print
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')

# Criamos a classe ContaCorrente herdando de Conta 
class ContaCorrente(Conta):

    # Fizemos uma função init igual a classe super, mas no final acrescentamos
    # o valor limite = 0 
    def __init__(self, agencia, conta, saldo=0, limite=0):

        # fizemos o super().__init__(agencia, conta, saldo) que retorna na 
        # classe super
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    # Criamos a função sacar para retornar o valor_pos_saque
    def sacar(self, valor):

        # Criamos a variavel valor_pos_saque para retornar o valor de
        # self.saldo - valor
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite





# Criamos esse if para verificar se o valor_pos_saque é maior ou igual
# ao limite maximo... se for verdadeiro a operação self.saldo - valor 
# irá retornar no self.saldo
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

# Se o if for falso, irá retornar esse print 
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    # Tivemos que criar essa função repr em conta corrente, pois aqui temos
    # a opção limite acrescentada
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        # Aqui retornamos a fstring das variaveis
        return f'{class_name}{attrs}'
    

# Criamos a classe Pessoa
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

# Criamos o property para retornar no self._nome
    @property
    def nome(self):
        return self._nome

# Criamos o setter para retornar o valor nome em self._nome
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

# Criamos o property para retornar no self._idade
    @property
    def idade(self):
        return self._idade

# Criamos o setter para retornar o valor idade em self._idade
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade


    # Criamos essa função para mostrar o class name e o attrs com o repr
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'

        # Aqui retornamos a fstring das variaveis
        return f'{class_name}{attrs}'
    
# Criamos a class Cliente herdando de Pessoas
class Cliente(Pessoa):

# Criamos essa função com o valor nome e idade para retornar em self.conta
    def __init__(self, nome: str, idade: int) -> None:
        # Criamos a super para repassar os valores para a class Pessoa
        super().__init__(nome, idade)

        # Aqui falamos que self.conta = a class Conta
        self.conta: Conta | None = None


# Criamos a classe Banco
class Banco(Conta):

    # Criamos essa função init com os valores de agencias, clientes e contas
    # Criamos uma lista para cada valor se verdadeiro e usamos | para se n for
    # verdadeiro, retornar um None = None
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None = None,
        contas: list[Conta] | None = None,
    ):
        
    # usamos o valor ou [] (lista)
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

# Criamos essa função para checar a agencia, retornando o valor de conta
    def _checa_agencia(self, conta):

        # Esse if foi criado para o valor conta.agencia esta em self.agencias.
        # Se for verdadeiro, retorna True
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        # Se falso, retorna False
        print('_checa_agencia', False)
        return False

# Criamos essa função para checar os clientes, retornando o valor de cliente
    def _checa_cliente(self, cliente):

        # Esse if foi criado para o valor cliente esta em self.clientes.
        # Se for verdadeiro, retorna True
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        
        # Se falso, retorna False
        print('_checa_cliente', False)
        return False

# Criamos essa função para checar a conta, retornando o valor de conta
    def _checa_conta(self, conta):

        # Esse if foi criado para o valor conta esta em self.contas.
        # Se for verdadeiro, retorna True
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        
        # Se falso, retorna False
        print('_checa_conta', False)
        return False


# Criamos essa função para checar se a conta é do cliente, 
# retornando o valor de cliente e conta
    def _checa_se_conta_e_do_cliente(self, cliente, conta):

        # Esse if foi criado para o valor conta esta em cliente.conta
        # Se for verdadeiro, retorna True
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        
        # Se falso, retorna False
        print('_checa_se_conta_e_do_cliente', False)
        return False

# Criamos essa função para autenticar os valores cliente e conta, retornando 
# da classe Pessoa e Conta
    def autenticar(self, cliente: Pessoa, conta: Conta):

        # Retornamos todas as funções com o self na frente
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

# Criamos essa função para mostrar o class name e o attrs com o repr
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'



    c1 = Cliente('Luiz', 30)
    cc1 = ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = Cliente('Maria', 18)
    cp1 = ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco.Banco(c1, c2)
    

cp1 = ContaPoupanca(111, 222)
cp1.sacar(1)
cp1.depositar(1)
cp1.sacar(1)
cp1.sacar(1)
print('##')

# cc1 = ContaCorrente(111, 222, 0, 100)
# cc1.sacar(1)
# cc1.depositar(1)
# cc1.sacar(1)
# cc1.sacar(1)
# cc1.sacar(98)
# cc1.sacar(1)
# print('##')

c1 = Cliente('Luiz', 30)
c1.conta = ContaCorrente(111, 222, 0, 0)
print(c1)
print(c1.conta)
c2 = Cliente('Maria', 18)
c2.conta = ContaPoupanca(112, 223, 100)
print(c2)
print(c2.conta)


c1 = Cliente('Luiz', 30)
cc1 = ContaCorrente(111, 222, 0, 0)
c1.conta = cc1
c2 = Cliente('Maria', 18)
cp1 = ContaPoupanca(112, 223, 100)
c2.conta = cp1
banco.Banco(c1, c2)

    # Usamos o extendd para ampliar a lista
banco.clientes.extend([c1, c2])
banco.contas.extend([cc1, cp1])
banco.agencias.extend([111, 222])

if banco.autenticar(c1, cc1):
    cc1.depositar(10)
    c1.conta.depositar(100)
    print(c1.conta)