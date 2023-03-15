from random import randint
from time import sleep

c ={'limpa' : '\033[m',
    'azul' : '\033[4;34m',
    'vermelho' : '\033[4;31m',
    'magenta' : '\033[4;35m'}

print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)
print('Olá ,sou percival,vamos jogar um jogo?!')
print('{}-=-{}'.format(c['magenta'],c['limpa']) * 30)
sleep(1)
print('Vou pensar em número de 1 a 5 ,tente adivinha.')
computador = randint(0,5)
jogador = int(input('Qual número você acha que pensei?'))
sleep(1)

print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 30)
print('Percival escolheu {}.'.format(computador))
print('Jogador escolheu {}.'.format(jogador))
print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 30)

sleep(1)
t = 0
v = 0

r = ''


while r =='S':

    if jogador == computador:
        print('Você venceu!!')
        sleep(1)
        r = str(input('Você quer tentar mais uma vez [S/N?]')).strip().upper()[0]

        ogador = int(input('Escolha um número de 1 a 5 :'))
        computador = randint(0, 5)
        sleep(1)
        print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)
        print('Percival escolheu {}.'.format(computador))
        print('Jogador escolheu {}.'.format(jogador))
        print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)
        v += 1
    elif jogador > 5:
        print('número invalido,vamos de novo!')
        sleep(1)
        r = str(input('Você quer tentar mais uma vez [S/N?]')).strip().upper()[0]

        jogador = int(input('Escolha um número de 1 a 5 :'))
        computador = randint(0,5)
        sleep(1)
        print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)
        print('Percival escolheu {}.'.format(computador))
        print('Jogador escolheu {}.'.format(jogador))
        print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)
        t +=1
    else:
        print('venci,vamos de novo!')
        sleep(1)
        r = str(input('Você quer tentar mais uma vez [S/N?]')).strip().upper()[0]
        sleep(1)
        jogador = int(input('Escolha um número de 1 a 5 :'))
        computador = randint(0, 5)
        sleep(1)
        print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)
        print('Percival escolheu {}.'.format(computador))
        print('Jogador escolheu {}.'.format(jogador))
        print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)
        t += 1




sleep(1)
if t >= 1:
    print('print você teve {} erradas até acabar'.format(t))
elif t == 0 :
    print('Só vitórias!!!')
else:
    print('você teve {} derrotas e {} vitórias.'.format(t, v))
print('E por hoje é só,obrigado por ter jogado comigo {}S2{}.'.format(c['vermelho'] , c['limpa']))



