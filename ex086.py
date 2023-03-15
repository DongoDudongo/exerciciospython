a = []
b = []
c = []
while True:
    n = int(input('Digite um valor:'))
    a.append(n)
    if n % 2 ==0:
        b.append(n)
    else:
        c.append(n)
    r = input('Quer continuar [S/N]?').strip().upper()[0]
    if r == 'N':
        break
print('-=-'*30)
print(f'A os valores digitados foram:{sorted(a)}')
print(f'Os números pares são:{sorted(b)}')
print(f'Os números impares são:{sorted(c)}')