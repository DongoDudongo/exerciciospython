from time import sleep

cores = {'limpa': '\033[m',
         'azul': '\033[4;34m',
         'vermelho': '\033[4;31m',
         'pretobranco': '\033[7m'}

print('{}-=-{}'.format(cores['pretobranco'],cores['limpa']) * 20)
print('Olá sou Percival,seu assistente virtual.')
print('{}-=-{}'.format(cores['pretobranco'],cores['limpa']) * 20)

E = float(input('Quanto custa a casa que você quer comprar?'))
A = float(input('Em quantos anos você espera quitar?'))
S = float(input('Quanto é sua renda mensal?'))

calculo = E / (A * 12)
print('CALCULANDO')
sleep(2)
print('veremos agora se você conseguirá arcar com nosso emprestimo.')
sleep(2)
print('Para comprar uma casa no valor de R${} em {} anos , o valor das parcelas será de R${:.02f}'.format(E, A, calculo))
meses = A * 12
parcela = S * 0.30
Media = E / meses

sleep(2)

if Media > parcela:

    print('Infelizmente {}NÂO{} poderei fazer o empréstimo.'.format(cores['vermelho'],cores['limpa']))

elif Media <= parcela:

    print('Vejo que você {}CONSEGUIRÁ{} pagar suas parcelas sem problema.'.format(cores['azul'],cores['limpa']))

print('Agradeço ter nos procurado.')

