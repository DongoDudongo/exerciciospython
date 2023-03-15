total = totamil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto:'))
    valor = float(input('R$:'))
    total += valor
    cont += 1

    if valor > 1000:
        totamil += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('fim do programa'))
print(f'O total da compra foi R${total:.2f}')
print(f'Tem um Total de {totamil} produtos  acima de R$1000.00')
print(f'o pruduto mais barato é {barato} e custa R${menor:.2f}.')