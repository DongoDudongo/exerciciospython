from datetime import date

from time import sleep

c = {'limpa' : '\033[m',
     'vermelho' : '\033[4;31m',
     'amarelo' : '\033[4;33m',
     'azul' : '\033[4;34m',
     'magenta' : '\033[4,35m',
     'ciano' : '\033[4;36m'}

atual = date.today().year

print('-=-' * 30)
print('olá,vamos verificar em qual categoria você se encaixa em nosso treinos de natação.')
print('-=-' * 30)
sleep(1)

i = int(input('Qual sua idade?'))

s = atual - i

print('CALCULANDO')

sleep(2)

if 4 <= s <= 9:

    print('Você é muito novo,deve se encaixar nas nossas aulas {}MIRIN{}.'.format(c['ciano'] , c['limpa']))

elif 10 <= s <= 14:

    print('Você está na faixa para nossas classe {}INFANTIL{}.'.format(c['magenta'] , c['limpa']))

elif 15 <= s <= 19:

    print('Você se encaixa na classe {}JÚNIOR{}.'.format(c['azul'] , c['limpa']))

elif 20 <= s <= 25:

    print('Você claramente pertence a nossa classe {}SÊNIOR{}.'.format(c['amarelo'] , c['limpa']))

elif 26 <= s <= 60:

    print('Devido a sua experiência você se encaixa na nossa classe {}MASTER{}.'.format(c['vermelho'] , c['limpa']))

elif s >= 61:

    print('Acho que você está muito acima da idade para praticar natação,\npeço que procure uma hidroginástica.')

elif s <= 3:

    print('você é muito novo para isso,pode ser perigoso,seus pais são loucos?!')

sleep(1)

print('Agradeço sua prefernêcia.')