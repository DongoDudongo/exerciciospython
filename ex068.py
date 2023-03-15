from random import randint
from time import sleep

computador = randint (1,10)
print('\033[4;35m-=-\033[m'*30)
print('Eu Percimal retornei!!! iremos jogar par ou impar!!')
print('só iremos parar \033[4;31mQUANDO EU VENCER\033[m!')
print('\033[4;35m-=-\033[m' * 30)
e=''
v = 0
jogador = 0
while True:

    jogador = int(input('Escolha seu número:'))
    e = str(input('qual você escolhe [P/I]?')).strip().upper()[0]
    sleep(1)

    print('\033[4;36m-=-\033[m'* 30)
    print(f'Eu escolho {computador}.')
    print(f'Você escolheu {jogador}.')
    print('\033[4;36m-=-\033[m'* 30)
    s = jogador + computador
    sleep(0.5)
    if e == 'P' and s % 2 == 0:

        print(f'Deu {s}!Você venceu!!Que droga!!')
        v +=1

    elif e == 'I' and s % 2 == 1:
        print(f'Deu {s}!Você venceu!!Maldito!!')
        v += 1

    else:
        print('\033[4;31mVENCI!!!\033[4;31m')
        break

if v >=1:
    print(f'Demorei {v} vezes para te derrotar!!!')
    sleep(0.5)
else:
    print('INVICTO AINDA!!!!SEU RUIM!!!!')
    sleep(0.5)
print('Encerro com minha a \033[4;33mVITÓRIA!!!\033[m')