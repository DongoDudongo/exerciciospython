import random

from time import sleep

import math

print('-=-' * 40)
print('RETORNO PARA MAIS UM JOGO!!EU PERCIMAL!!')
sleep(1)
print('Agora será par ou ímpar!')
print('-=-' * 40)
sleep(1.5)
cn= random.randint(0,9)

print('Eu escolho ímpar ,pois sou do mal')
sleep(1)

jogador = int(input('Escolha um número ,mortal:'))

n = (jogador + cn)% 2
n1 = jogador + cn
print("ANALISANDO")
sleep(2)
if n ==0:
    print('Não é possivel deu {}!?Como eu perdi?'.format(n1))

else:
    print('EU VENCI DEU {} ,SEU MORTAL INUTIL!!TREMA DIANTE DO MEU PODER!'.format(n1))

