from time import time

c = {'limpa' : '\033[m',
     'azul' : '\033[4;34m',
     'vermelho' : '\033[4;31m'}

p = float(input('qual o valor do produto?'))
print('''você irá pagar como:
[ 1 ] DINHEIRO
[ 2 ] CARTÃO DÉBITO / CRÉDITO 
[ 3 ] CRÉDITO X 2
[ 4 ] CRÉDITO X 3 OU MAIS''')

o = int(input('Qual a opção escolhida:'))

d = p - ( p * 0.1)
cd = p - ( p * 0.05)
cc = p + ( p * 0.2)

if o == 1:

    print('Você pagará R$ {:.2f}.'.format(d))

elif o == 2:

    print('Você pagará R$ {:.2f}.'.format(cd))

elif o == 3:

    print('Você pagará R$ {:.2f} , cada parcela fica R$ {:.2f}.'.format(p , p/2))

elif o == 4:

    par = int(input('Em quantas parcelas:'))

    print('Você pagará R$ {:.2f} ,cada parcela fica R$ {:.2f}.'.format(cc , cc / par))

else:

    print('opção inválida')



