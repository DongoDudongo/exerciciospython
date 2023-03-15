from random import randint

from time import sleep

c = {'limpa' : '\033[m',
     'vermelho' : '\033[4;31m',
     'verde' : '\033[4;32m',
     'amarelo' : '\033[4;33m',
     'azul' : '\033[4;34m',
     'magenta' : '\033[4;35m',
     'ciano' : '\033[4;36m'}

print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 30)
print('RETORNEI MORTAL!! EU {}PERCIMAL{}!'.format(c['vermelho'] , c['limpa']))
print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 30)
sleep(1)



itens = ('pedra','papel','tesoura')

pc = randint(0,2)

print('''Vamos jogar jokenpô,você tem essas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

sleep(1)

j = int(input('Qual será sua fraca jogada mortal?'))

print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 15)

print('Percimal escolhe {}.'.format(itens[pc]))
print('jogador escolheu {}.'.format(itens[j]))

print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 15)

sleep(2)

if pc == 0:
    if j == 0:
        print('COMO {}EMPATAMOS{}'.format(c['amarelo'] , c['limpa']))
    elif j == 1:
        print('VOCÊ {}VENCEU{}!!COMO ASSIM?!'.format(c['azul'] , c['limpa']))
    elif j == 3:
        print('EU {}VENCI{}!! ERA ÓBVIO!!'.format(c['ciano'] , c['limpa']))
    else:
        print('{} você é idiota,isso nem é uma das opções!!{}'.format(c['vermelho'] , c['limpa']))

elif pc == 1:
    if j == 0:
        print('TREMA COM A MINHA {}VITÓRIA{}!'.format(c['vermelho'] , c['limpa']))
    elif j == 1:
        print('COMO ASSIM {}EMPATAMOS{}?!'.format(c['amarelo'] , c['limpa']))
    elif j == 2:
        print('EU {}PERDI{}?!'.format(c['ciano'] , c['limpa']))
    else:
        print('{}ISSO NÃO É UMA OPÇÃO!!!{}'.format(c['vermelho'] , c['limpa']))

elif pc == 2:
    if j == 0:
        print('NÃO!!!{}PERDIIIII{}!!'.format(c['azul'] , c['limpa']))
    elif j == 1:
        print('{}VITÓRIA{}!!!'.format(c['vermelho'] , c['limpa']))
    elif j == 2:
        print('UM {}EMPATE{} É PIOR QUE UMA DERROTA!!'.format(c['amarelo'] , c['limpa']))
    else:
        print('{}NÃO É UMA OPÇÃO!!!{}'.format(c['vermelho'] , c['limpa']))

else:
    print('{}VOCÊ É IDIOTA?!{}'.format(c['vermelho'] , c['limpa']))

sleep(1)

print('Encerro mais uma vez nosso duelo,voltarei para mais jogos!!')