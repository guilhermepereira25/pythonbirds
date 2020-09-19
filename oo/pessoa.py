class Pessoa:
    olhos = 2

    def __init__(self, *filhos,  nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    guilherme.olhos = 1
    del guilherme.olhos
    print(guilherme.__dict__)
    print(giovana.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(guilherme.olhos)
    print(giovana.olhos)
    print(id(Pessoa.olhos), id(guilherme.olhos), id(giovana.olhos))
    print(Pessoa.metodo_estatico(), guilherme.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), guilherme.nome_e_atributos_de_classe())


