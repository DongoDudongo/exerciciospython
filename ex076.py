print('Digite 4 valores,e iremos dizer quantos núemros 9 tem,'
      'em que posição o avlor 3 está e quais são os valores pares.')

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('digite o último número: ')))
print(f'Você digitou os valores: {n}')
if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)}')
else:
    print('O valor 9 não est´no grupo para ser contado.')
if 3 in n:

    print(f'O valor 3 apareceu na {n.index(3) + 1}ª posição')
else:
    print('o Valor 3 não está em nenhuma posição')
for c in n:
    if c% 2 == 0:
        print(f'O valores pares são : {c}',end='' )
    else:
        print('não tem valores pares.')