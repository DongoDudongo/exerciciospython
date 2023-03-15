pergunta = int(input('Quantas pessoas você trouxe para jogar paint ball?'))
print('Preciso verificar suas idades para ver se podem jogar.')
from datetime import date
totmaior = 0
totmenor = 0
ano = date.today().year
for idade in range(0 , pergunta):
    i = int(input('em que ano você nasceu?'))
    if ano - i >= 18:
        print('você tem {} ,logo é maior de idade!'.format(ano - i))
        totmaior += 1
    else:
        print('você tem {},muito novo.'.format(ano - i))
        totmenor +=1
print('temos {} maiores de idade,e {} de menor. '.format(totmaior,totmenor))