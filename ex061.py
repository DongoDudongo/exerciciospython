from math import factorial
n = int(input('digite um número:'))
f = factorial(n)
c = n
print('Calculando {}! = '.format(n))
while c > 0:
    print('{}'.format(c),end ='')
    print(' x ' if c > 1 else ' = {}'.format(f),end = '')
    c -= 1
#print('o fatorial de {} é {}'.format(n,f))