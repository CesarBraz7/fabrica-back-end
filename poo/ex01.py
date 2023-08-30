class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def saudacao(self):
        print(f'oi, meu nome eh {self.nome}, tenho {self.idade} anos de idade e sou {self.profissao}')
    
pessoa = Pessoa('cesar', 18, 'desenvolvedor')
pessoa.saudacao()