velocidade = int(input('digite a velocidade do carro automovel: '))

multa = (7 * (velocidade - 80))

if(velocidade > 80):
    print('voce foi multado em R$', multa)
else:
    print('não foi multado')