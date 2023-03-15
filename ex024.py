idade = int(input('qual sua idade?'))
print('você não pode nem jogar GoD'if idade<=17 else'já ta na idade dos boletos?!')  #condição simplificada
#if idade<=17:

     #print('Você não pode nem jogar GoW Ragnarok ainda!tadinho!')

#else:
     #print('já ta na idade dos boletos né?')

print('---FIM---')

n1 = float(input('Qual foi primeira sua nota?'))
n2 = float(input('qual foi sua segunda nota?'))
m = (n1 + n2)/2
print('Sua média foi {}'.format(m))
if m >=6.0:
    print('Sua média foi muito boa!Parabéns!')
else:
    print('Seu abestado,vai estudar!!Sai dos joguinhos!!')
