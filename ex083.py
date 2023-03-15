n = []
while True:
    n1 = int(input('digite um valor:'))
    if n1 not in n:
        n.append(n1)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado ,não vou adicionar...')

    r = input('Quer continuar? [S/N]').strip().upper()[0]
    if r in 'N':
        break
print('-=-'*30)
print(f'os valores digitados foram: {sorted(n)}')