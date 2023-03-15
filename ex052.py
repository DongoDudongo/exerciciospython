n = int(input('digite um número:'))
mult = 0

for c in range(1 , n + 1 ):
    if n % c == 0:
        print('\033[34m', end =' ')
        mult += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(c), end =' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n ,mult))

if mult == 2:
    print('ele é primo.')
else:
    print('ele não é primo.')

p = int(input('verifique se tem números primos até:'))
tot = 0

for d in range(1 , p + 1):
    if p % d == 0 and tot == 2:
        tot += 1

        print( d )


