from time import sleep

c = {'limpa': '\033[m',
     'azul': '\033[4;34m',
     'amarelo': '\033[4;33m',
     'vermelho': '\033[4;31m',
     'magenta': '\033[4;35m',
     'ciano': '\033[4;36m',
     'branco': '\033[4;30m'}

print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)

print('Vamos conferir se conseguimos montar um triângulo e qual será seu tipo.')

print('{}-=-{}'.format(c['magenta'], c['limpa']) * 30)

sleep(1)

print('agora digite três números.')

n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número:'))
n3 = float(input('terceiro número:'))

t = n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2
i = n1 == n2 != n3 or n1 != n2 == n3 or n1 == n3 != n2
e = n1 == n2 == n3
es = n1 != n2 != n3 != n1

print('ANALISANDO')

sleep(2)

if t and e:

    print('Olha que legal formamos um triângulo {}Equilátero{}.'.format(c['azul'], c['limpa']))

elif t and i:

    print('Formamos um triângulo {}Isósceles{}.'.format(c['amarelo'], c['limpa']))

elif t and es:

    print('Esse é uma triângulo {}Escaleno{}.'.format(c['magenta'], c['limpa']))

else:

    print('Infelizmente {}NÃO{} formamos nenhum tipo de triângulo.'.format(c['vermelho'], c['limpa']))

sleep(1)

print('Muito obrigado por ter participado {}S2{}.'.format(c['vermelho'], c['limpa']))

sleep(4)

print('PARTE PARA ANALISAR OUTRA RESPOSTA DE CODIGO')

if n1 < n2 +n3 and n2 < n1 + n3 and n3 < n2 + n3:

    print('é um triângulo')
    if n1 == n2 == n3:
        print('equilátero')
    #elif n1 == n2 !=n3 or n1 == n3 != n2 and n2 == n3 !=n1:
        #print('isosceles')
    elif n1 != n2 != n3 != n1:
        print('escaleno')
    else:
        print('isosceles')

else:
    print('não é triangulo')