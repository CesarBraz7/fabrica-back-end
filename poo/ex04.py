class FormaGeometrica():
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

retangulo = Retangulo(int(input('digite o valor da base: ')), int(input('digite o valor da altura: ')))
area_retangulo = retangulo.calcular_area()
print("area do retângulo:", area_retangulo)

circulo = Circulo(int(input('digite o valor do raio: ')))
area_circulo = circulo.calcular_area()
print("area do círculo:", area_circulo)
