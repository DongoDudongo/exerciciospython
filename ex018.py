import random

j1 = str(input('primeiro jogador:'))
j2 = str(input('segundo jogador:'))
j3 = str(input('terceiro jogador:'))
j4 = str(input('Quarto jogador:'))
lista = [j1,j2,j3,j4]
random.shuffle(lista)

print('Aqui esta a ordem dos que vão morrer na proxima jogatina:')
print(lista)