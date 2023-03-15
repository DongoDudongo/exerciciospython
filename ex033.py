# comando de cores

#\033[style : texto : back   m

#quando for colocar a cor tem que por o numero do Stylo,do texto e do background

# style
#0 = none(sem estilo)
#1 = bold (negrito)
#4 = underline(sublinhado)
#7 = negative (vai inverter o tom)

#texto

#30 = branco
#31 = vermelho
#32 = verde
#33 = amarelo
#34 = azul
#35 = magenta
#36 = ciano
#37 = cinza

#back ou background

#40 = branco
#41 = vermelho
#42 = verde
#43 = amarelo
#44 = azul
#45 = magenta
#46 = ciano
#47 = cinza

print('\033[0:30:41m teste')
print('\33[35;40mteste\033[m')

#pode se criar uma variavel  onde ficaria todas as cores que vc vai usar
cores = {'limpa':'\033[m' ,
         'azul': '\033[34m' ,
         'pretoebranco': '\033[7;30m'}
nome = input('qual seu nome?')
print('olá,muito prazer {}{}{}'.format(cores['azul'] , nome , cores['limpa']))