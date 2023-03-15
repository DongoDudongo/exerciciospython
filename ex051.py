from time import sleep
cor = {'limpa' : '\033[m',
       'magenta' : '\033[35m',
       'azul' : '\033[4;34m',
       'vermelho' : '\033[4;31m'}

print('{}-=-{}'.format(cor['magenta'] , cor['limpa']) * 30)
print('Olá,irei ajudar você a fazer uma {}PROGRESSÃO ARITIMÉTICA{}.'.format(cor['azul'] , cor['limpa']))
print('{}-=-{}'.format(cor['magenta'] , cor['limpa']) * 30)
sleep(1)

n = int(input('escolha o número:'))
pa = int(input('Escolha a razão da progressão:'))
t = int(input('qual o tamanho da progressão:'))
print('{}ANALISANDO{}'.format(cor['vermelho'] , cor['limpa']))
sleep(2)
term = (t + 1)*pa
for c in range(n ,term , pa ):

    print('{}'.format(c),end ='➛')
    sleep(0.5)
sleep(1)
print('ACABOU.')