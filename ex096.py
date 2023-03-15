from random import randint
from time import sleep
lista =[]
jogos = []
print('-'*30)
print('      JOGO DA MEGA SENA     ')
print('-'*30)
q = int(input('Quantos jogos você quer sortear?'))
tot = 1
while tot <= q:
    cont= 0
    while tot <= q:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-='*5,f'  SORTEADO {q} JOGOS  ','-='*5)
sleep(0.5)
for i,l in enumerate(jogos):
    print(f' O jogo {i+1} foi : {l}')
    sleep(0.5)
print('-='*5,'< BOA SORTE! >','-='*5)