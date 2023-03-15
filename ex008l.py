from datetime import date

atual = date.today().year

jovem = int(input('Em qual nao você nasceu?'))

s = atual - jovem
print('Agora vamos ver se você está pronto a servir')

if s == 18:
    print('PARABÉNS!!Você está com a idade para servir a nação')
elif s < 18:
    print('Infelizmente ,ainda faltam {} anos.'.format(18 - s))
    print('O ano do seu alistamento deverá ser {}'.format((18 - s) + atual))
elif s > 18:
    print('Agradecemos seu entusiasmo,mas você chegou atrasado {} anos.'.format(s - 18))
    print('Mas você deveria ter servido em {}'.format(atual - (s - 18)))
