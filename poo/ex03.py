class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def acelerarCarro (self, velocidade, acelerar):
        self.acelerar = acelerar
        self.velocidade = velocidade
        self.velocidade = int(input('qual a velocidade atual do carro? \n'))
        while True:
            self.acelerar = input('deseja acelerar o carro? digite "não" caso não queira ')
            if self.acelerar == 'sim':
                self.velocidade += 10
            else:
                print(f'{self.velocidade}km/h')
                break
                
carro = Carro(input('digite a marca do carro: '), input('qual o modelo? '), int(input('qual o ano de fabricação? ')))
carro.acelerarCarro(0, 0)