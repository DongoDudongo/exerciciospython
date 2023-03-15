moeda = float(input('R$:'))

dolar = moeda/5.1

print('$ {:.2f}'.format(dolar))

a = float(input('altura:'))
c = float(input('comprimento:'))
area = a * c
tinta = area/2

print('A área da sala é {:.1f}m²,para pintá-la você vai precisar de {:.1f}L'.format(area,tinta))

p = float(input('Qual o preço da tinta?'))
d = p *5/100
ac = p *15/100

print('O preço com desconto da loja fica R$ {}'.format(p-d))

print('porém se comprar no cartão terá um acrescimo de 15% ficando R$ {}'.format(p+ac))

