class Animal():
    def reproduzirSom(self):
        pass
    
class Gato(Animal):
    def __init__(self, som):
        self.som = som
    
    def reproduzirSom(self):
        print(f'o gato faz {self.som}')

class Raposa(Animal):
    def __init__(self, som):
        self.som = som
    
    def reproduzirSom(self):
        print(f'a raposa faz {self.som}')

class Cachorro(Animal):
    def __init__(self, som):
        self.som = som
    
    def reproduzirSom(self):
        print(f'o cachorro faz {self.som}')    
    
gato = Gato('miau')
gato.reproduzirSom()

raposa = Raposa('nhinhinhi')
raposa.reproduzirSom()

cachorro = Cachorro('au au')
cachorro.reproduzirSom()