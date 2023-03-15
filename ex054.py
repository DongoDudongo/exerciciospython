n = int(input('quantas pessoas você trouxe para a avaliação?'))
maior = 0
menor = 0
for c in range (1 , n + 1):
    p = float(input('peso da {}ª pessoa:'.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('o maior peso lido foi de {} Kg'.format(maior))
print('o menor peso lido foi de {} Kg'.format(menor))



