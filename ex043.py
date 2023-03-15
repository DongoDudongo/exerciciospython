from time import sleep

c = {'limpa' : '\033[m',
     'branco' : '\033[4;30m',
     'vermelho' : '\033[4;31m',
     'azul' : '\033[4;34m',
     'amarelo' : '\033[4;33m',
     'magenta' : '\033[4;35m',
     'ciano' : '\033[4;36m'}

print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 30)

print('Olá,vamos verificar se seu IMC está ruim,bom ou ótimo.')

print('{}-=-{}'.format(c['magenta'] , c['limpa']) * 30)

sleep(1)

print('Vamos lá preciso só de duas informações.')

sleep(1)

a = float(input('Qual sua altura em metros?'))
m =float(input('Qual seu peso em Kg?'))

print('CALCULANDO')

sleep(3)

imc = m / (a)**2

print('Seu IMC é {:.1f}.'.format(imc))

sleep(1)

if imc < 18.5:

    print('Recomendo você procurar um clínico geral,pois você está {}ABAIXO{} do peso.'.format(c['amarelo'] , c['limpa']))

elif 18.5 <= imc < 25:

    print('PARABÉNS!!Você está no peso {}IDEAL{}.'.format(c['branco'] , c['limpa']))

elif 25 <= imc < 30:

    print('Você está com {}SOBREPESO{},nada que uma dieta não resolva.'.format(c['azul'] , c['limpa']))

elif 30 <= imc < 40:

    print('Recomendo a procura de um nutricionista,você esta {}OBESO{}.'.format(c['ciano'] , c['limpa']))

elif 40 <= imc:

    print('Você esta com {}OBESIDADE MÓRBIDA{},procure o mais rápido possivel um médico.'.format(c['vermelho'] , c['limpa']))

sleep(1)

print('Espero ter ajudado você a se colocar no caminho da alimentação saúdavel.')