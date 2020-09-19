"""
Voce deve criar uma classe carro que vai possuir dois atributos compostos por duas classe

1) motor
2) direção

O motor tera a responsabilidade de controlar a velocidade
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) metodo acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabiçidade de controlar a direçao. Ela oferece os seguintes atributos:
1) Valor da direçao com valores possiveis: Norte, sul, leste, oeste;
2) metodo girar_a_direita
3) metodo girar_a_esquerda

  N
O   L
  S

  Exemplo:
  >>> #Testando o motor
  >>> motor = Motor()
  >>> motor.velocidade
  0
  >>> motor.acelerar()
  >>> motor.velocidade
  1
  >>> motor.acelerar()
  >>> motor.velocidade
  2
  >>> motor.frear()
  >>> motor.velocidade
  3
  >>> motor.frear()
  >>> motor.velocidade
  0
  >>> direçao = Direçao()
  >>> direçao.valor
  'Norte'
  >>> direçao.girar_a_direita()
  >>> direçao.valor
  'Leste'
  >>> direçao.girar_a_direita()
  >>> direçao.valor
  'Sul'
  >>> direçao.girar_a_direita()
  >>> direçao.valor
  'Oeste'
  >>> direçao.girar_a_esquerda()
  >>> direçao.valor
  'Norte'
  >>> direçao.girar_a_esquerda()
  >>> direçao.valor
  'Oeste'
  >>> direçao.girar_a_esquerda()
  >>> direçao.valor
  'Sul'
  >>> direçao.girar_a_esquerda()
  >>> direçao.valor
  'Leste'
  >>> direçao.girar_a_esquerda()
  >>> direçao.valor
  'Norte'
  >>> carro = Carro(direçao, motor)
  >>> carro.calcular_velocidade()
  0
  >>> carro.acelar()
  >>> carro.calcular_velicidade()
  1
  >>> carro.acelar()
  >>> carro.calcular_velicidade()
  2
  >>> carro.frear()
  >>> carro.calcular_velocidade()
  0
  >>> carro.calcular_direçao()
  >>> 'Norte'
  >>> carro.girar_a_direita()
  >>> carro.calcular_direçao()
  >>> 'Leste'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direçao()
  >>> 'Norte'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direçao()
  >>> 'Oeste'


 """

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direçao:
    rotaçao_a_direita_dct= {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotaçao_a_esquerda_dct= {NORTE: OESTE, LESTE: NORTE, SUL: OESTE, OESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor= self.rotaçao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor= self.rotaçao_a_esquerda_dct[self.valor]
