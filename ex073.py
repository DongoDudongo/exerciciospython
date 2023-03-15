n = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
p = 0
for c in n:
    p = int(input('digite um numero de 0 a 20:'))
    if p in n:
        print(f'Você escolheu {p}.')
        break
    else:
        print('Tente novamente',end =',')
        p = int(input('Digite um número de 0 a 20:'))

print('FIM.')

#resolução do curso em video

cont = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
        'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('digite um número entre 0 e 20:'))
    if 0 <= num <= 20:
        break
    print('tente novamente,',end ='')
print(f'você digitou o número {cont[num]}')