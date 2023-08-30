class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def sacarDinheiro(self, saque):
        self.saque = saque
        self.saldo = self.saldo - self.saque
        print(f'seu saldo apos o saque eh de: {self.saldo}')
        
    def depositarDinheiro(self, deposito):
        self.deposito = deposito
        self.saldo = self.saldo + self.deposito
        print(f'seu saldo apos o deposito eh de: {self.saldo}')
        
pessoa = ContaBancaria(input('digite seu nome: '), int(input('digite seu saldo: ')))

comando = int(input('\ndigite 1 para sacar ou 2 para depositar: '))
match comando:
    case 1:
        pessoa.sacarDinheiro(int(input('digite o valor do saque: ')))
    case 2:
        pessoa.depositarDinheiro(int(input('digite o valor do deposito: ')))