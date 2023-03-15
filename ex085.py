lista =[]

while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    r = input('Quer continuar [S/N]? ').strip().upper()[0]
    if r == 'N':
        break

print('-=-'*30)
print(f'O valores digitados foram: {lista}')
print(f'Tem {len(lista)}  valores na lista. ')
if 5 in lista:

    print(f'O número 5 aparece na lista {lista.count(5)} vezes.')

else:
    print('Infelizmente não tem o numero 5 na lista.')
lista.sort(reverse=True)
print(f'A ordem  invertida fica:{lista}')
