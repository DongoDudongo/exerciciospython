c = {'limpa' : '\033[m',
     'azul' : '\033[4;34m',
     'vermelho' : '\033[4;31m',
     'amarelo' : '\033[4;33m'}

portugues = float(input('Qual foi sua nota em portugûes:'))
ch = float(input('Qual foi sua nota em Ciências humanas?'))
matematica = float(input('Qual foi sua nota de matemática?'))
red = float(input('Qual foi a nota da sua redação?'))

m = (portugues + ch + matematica + red) / 4

if m < 5:
    print('Infelizmente você foi {}REPROVADO{} no esimulado com a nota {:.1f}'.format(c['vermelho'] , c['limpa'], m))
elif 5 <= m <= 6.9:
    print('Você ainda tem uma chance com a nota {:.1f} na {}RECUPERAÇÃO{}'.format(m , c['amarelo'], c['limpa']))
elif 7 <= m <= 10:
    print('Parabéns!! você tirou {} foi {}APROVADO{}'.format(m , c['azul'] , c['limpa']))
else:
    print('acho que você está mentindo sobre sua nota')

