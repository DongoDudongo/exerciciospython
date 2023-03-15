import math
num = int(input('digite um número:'))
raiz = math.sqrt(num)
print('A raiz {} é {:.1f},arredondando é {} ou {}'.format(num,raiz,math.floor(raiz),math.ceil(raiz)))

