class Pessoa:
    def __init__(self, *filhos,  nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    giovana = Pessoa(nome='Giovana')
    guilherme = Pessoa(giovana, nome='Guilherme')
    print(Pessoa.cumprimentar(guilherme))
    print(id(guilherme))
    print(guilherme.cumprimentar())
    print(guilherme.nome)
    print(guilherme.idade)
    for filho in guilherme.filhos:
        print(filho.nome)
    guilherme.sobrenome = 'Pereira'
    del guilherme.filhos
    print(guilherme.__dict__)
    print(giovana.__dict__)




