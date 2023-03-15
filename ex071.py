print('=' * 30)
print('{:^30}'.format('BANCO DC'))
print('='* 30)

valor = int(input('qual valor você quer sacar? R$'))
total = valor
c = 50
tc = 0
while True:
    if total >= c:
        total -= c
        tc += 1
    else:
        if tc > 0:
            print(f'total de {tc} cédulas  de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO DC')