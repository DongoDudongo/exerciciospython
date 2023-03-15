from time import sleep
cor ={'limpa' : '\033[m',
      'azul' : '\033[4;34m',
      'vermelho' : '\033[4;31m',
      'magenta' : '\033[4;35m',
      'ciano' : '\033[4;36m'}



print('{}-=-{}'.format(cor['magenta'],cor['limpa']) * 10)
print('GERADOR DE PA')
print('{}-=-{}'.format(cor['magenta'],cor['limpa']) * 10)
sleep(1)
n1 = int(input('primeiro termo:'))
ra = int(input('qual a razão?'))

termo = n1
cont = 1
op = 10
total = 0

print('{}CALCULANDO{}'.format(cor['magenta'],cor['limpa']))
sleep(2)
print('{}-=-{}'.format(cor['vermelho'],cor['limpa']) * 20)

while op !=0 :
    total = total + op
    while  cont <= total :

        print('{} -> '.format(termo) , end= '')
        termo += ra
        cont +=1

    print('PAUSA')
    print('{}-=-{}'.format(cor['vermelho'], cor['limpa']) * 20)
    sleep(0.5)
    op = int(input('{}deseja estender a PA em quantos números:{}'.format(cor['ciano'], cor['limpa'])))
    sleep(0.5)
    print('{}-=-{}'.format(cor['vermelho'],cor['limpa']) * 20)

print('Fim do programa!')

