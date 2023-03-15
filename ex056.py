from time import sleep

cor = {'limpa' : '\033[m',
       'azul' : '\033[4;34m',
       'vermelho' : '\033[4;31m',
       'magenta' : '\033[4;35m',
       'ciano' : '\033[4;36m'}

print('{}-=-{}'.format(cor['ciano'], cor['limpa']) * 30)
print('olá,sou Percy.py  um analisador  completo.')
print('{}-=-{}'.format(cor['ciano'],cor['limpa']) * 30)
sleep(2)
n = int(input('quantas pessoas,eu preciso analisar?'))

sleep(1)
print('ok, agora por favor,respondam as seguintes perguntas.')
sleep(1)

si =0 # soma das idades
mi = 0 # media de idades
nf = 0 # numero de mulheres
nh = 0 # numero de homens
mf = 0 # idade da mulher mais velha
mh = 0 # idade do homem mais velho
nvh ='' # nome do homem mais velho
nvf ='' #nome da mulher mais velha
n2 = 0 # número de mulheres com menos de 20 anos
n3 = 0 # número de homen com menos de 20 anos

for j in range(1 , n +1):

    print('{}-----{}ª PESSOA-----{}'.format(cor['azul'], j ,cor['limpa']))

    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper().strip()
    si += idade
    mi = si / n
    sleep(0.5)
    if sexo =='M':
        nh +=1
    if j == 1 and sexo == 'M':
        mh = idade
        nvh = nome
    if sexo == 'M' and  idade > mh:
        mh = idade
        nvh = nome
    if sexo =='F':
        nf += 1
    if j == 1 and sexo =='F':

        mf = idade
        nvf = nome
    if  sexo == 'F' and  idade > mf:
        mf = idade
        nvf = nome
    if sexo == 'F' and idade <= 20 :
        n2 += 1
    if sexo == 'M' and idade <= 20:
        n3 +=1

sleep(0.5)
print('{}ANALISANDO DADOS{}'.format(cor['vermelho'], cor['limpa']))
sleep(3)
print('tem {} homens e {} mulheres.'.format(nh,nf))
if n2 >0:
    print('Tem {} mulheres  com menos de 20 anos.'.format(n2))

elif n3 > 0:
    print('Tem {} homens com menos de 20 anos.'.format(n3))

elif n2 == 0:
    print("Não temos nenhuma mulher com menos de 20 anos.")

elif n3 == 0:
    print('Não temos nenhum homem com menos de 20 anos.')



print('A média das idades é {:.1f}.'.format(mi))
if nh >0:

    print('O homem mais velho se chama {} e tem {} anos.'.format(nvh,mh))

else:
    print('{}Não tem homens para serem analisados{}'.format(cor['vermelho'],cor['limpa']))
if nf >0:

    print('A mulher mais velha se chama {} e tem {}.'.format(nvf , mf))
else:
    print('{}Não tem mulheres para serem analisadas.{}'.format(cor['vermelho'],cor['limpa']))

sleep(1)
print('Agradeço por ter me escolhido como analisador geral.')