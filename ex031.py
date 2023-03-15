from time import sleep

print('-+-' * 40)
print('Olá sou Per$ival,seu assistente para finanças.')
sleep(1)
print('vamos lá,vamos ver o quanto você irá ganhar!!')
print('-+-' * 40)
sleep(1)
salario = float(input('Quanto é seu salario?'))
print('CALCULANDO')
sleep(2)
if salario >1250:
    pagamento  = salario +(salario * 10)/100
    print('Você teve um aumento de 10%.')

if salario <=1250:
    pagamento = salario + (salario * 15)/100
    print('Você teve um aumento de 15%.')

print('Seu salário atual é de R${:.2f}'.format(pagamento))