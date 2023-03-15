s = 0
cont = 0
maior = 0
menor = 0
r = 'S'

while r in 'S':
    n = int(input('digite um número:'))
    cont += 1
    s += n
    m = s / cont
    r = str(input('Quer continuar [S/N]?')).strip().upper()[0]

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('{} é o maior,{} é o menor e {} é a média.'.format(maior,menor,m))


