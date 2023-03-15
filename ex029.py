from time import sleep
import math

print('-=-' * 40)
print('Olá,sou Perci.A.I.R , seu assistente de viagem.')
print('-=-' * 40)
sleep(1)
local = float(input('Qual a distância em Km da sua localização para onde pretende viajar?'))
sleep(1)
print('Vamos ver quanto sai o custo da sua viagem.')
print('ANALISANDO')
sleep(2)

t = local * 0.50 if local <=200 else local * 0.45
if local <=200:
    print('Sua viagem vai dar R${:.2f}'.format(t))
else:
    print('Sua viagem deu R${}'.format(t))