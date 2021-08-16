class Pessoa:
    olhos = 2

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
    cleiton.sobrenome = 'Teixeira'
    del cleiton.filhos
    print(cleiton.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(cleiton.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(cleiton.olhos), id(renzo.olhos))






