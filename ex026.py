from random import randint
from time import sleep

computador = randint(0,5)
print('-=-' * 40)
print('Olá,sou Percimal,uma I.A. malégna')
sleep(1.5)
print('Vamos jogar um jogo de advinhação,pensarei em um número de 0 a 5,\nvamos ver se você acerta.')
sleep(1.5)
print('-=-' * 40)
jogador = int(input('qual foi o número?'))
print('PROCESSANDO')
sleep(3)
if jogador == computador:
    print('Droga,derrotado por uma bola de carne!!T-T')
else:
    print('Sua bola de carne estúpida eu pensei no {} e não no {}'.format(computador,jogador))
    sleep(1)
    print('SUCUMBAM AO MEU PODER!')
