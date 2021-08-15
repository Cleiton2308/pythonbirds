class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    cleiton = Pessoa(nome = 'Cleiton')
    renzo = Pessoa(cleiton, nome='Renzo')
    print(Pessoa.cumprimentar(cleiton))
    print(id(cleiton))
    print(cleiton.cumprimentar())
    print(cleiton.nome)
    print(cleiton.idade)
    for filho in cleiton.filhos:
        print(filho.nome)
    print(cleiton.filhos)



