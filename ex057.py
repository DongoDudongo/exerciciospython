r = 'S'
while r == 'S':
    n = int(input('digite um valor:'))
    r = str(input('quer continuar [S/N]?')).upper()

print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um número:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('você digitou {} números pares e {} numeros impares.'.format(par,impar))