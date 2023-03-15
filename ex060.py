from time import sleep

cor ={ 'limpa' : '\033[m',
       'azul' : '\033[4;34m',
       'vermelho' : '\033[4;31m',
       'amarelo' : '\033[4;33m',
       'magenta' : '\033[4;35m',
       'ciano' : '\033[4;36m'}

print('{}-=-{}'.format(cor['magenta'], cor['limpa']) * 30)
nome = str(input('Olá sou percival,qual seu nome?'))
print('Muito prazer {},Vamos calcular juntos.'.format(nome))
print('{}-=-{}'.format(cor['magenta'],cor['limpa']) * 30)

sleep(1)
n1 = int(input('Digite o primeiro número?'))
n2 = int(input('digite o segundo número:'))


sleep(1)
op = 0
s = 0
m = 0
sub =0
ex = 0

while op != 6:
    print('{}-=-{}'.format(cor['magenta'], cor['limpa']) * 30)
    print('''
[1] SOMAR
[2] MULTIPLICAR
[3] SUBTRAIR
[4] EXPONENCIAÇÃO
[5] NOVOS NÚMEROS
[6] SAIR DO PROGRAMA\n''')
    op = int(input('>>>>Qual sua opção?'))
    sleep(0.5)
    if op == 1:
        s = n1 + n2
        print('\nA soma dos números é {}.'.format(s))
        sleep(0.5)
    elif op == 2:
         m = n1 * n2
         print('\nA multiplicação deu {}.'.format(m))
         sleep(0.5)
    elif op == 3:
        sub = n1 - n2
        print('\nA subtração deu {}.'.format(sub))
        sleep(0.5)
    elif op ==4:
        ex = n1 **n2
        print('\nO {} elevado a {}ª potência  é igual {}.'.format(n1,n2,ex))
        sleep(0.5)
    elif op == 5:
        print('\ninforme os número npvamente.')
        n1 = int(input('digite o primeiro número:'))
        n2 = int(input('digite o segundo número:'))
        sleep(0.5)
    elif op >=7:
        print('\n{}opção inválida ,tente novamente{}'.format(cor['vermelho'],cor['limpa']))
        sleep(0.5)
sleep(1)
print('\n{}fim do programa.{}'.format(cor['ciano'],cor['limpa']))



