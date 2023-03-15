from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO'.format(ano))

a = float(input('digite o primeiro número:'))
b = float(input('digite o segundo número:'))
c = float(input('digite o terceiro número:'))

#verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#verificando maior
maior = a
if b>a and b>c:
    maior = b
if c>b and c>a:
    maior = c

print('o menor valor é {}'.format(menor))
print('o maior valor é {}'.format(maior))