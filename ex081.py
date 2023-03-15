a = [1,2,3,4]
b = a
b[2]=8
print(f'A lista A : {a}')
print(f'A lista B : {b}')
# a alteração feita na lista b ,alterou a lista a,pois quando igualamos as listas dessa forma criamos uma ligação,
#onde mescla toda e qualquer alteração feita em uma

#porém se feito dessa forma não tera alteração mesclada

c = [5,6,7,8]
d = c[:] #através de fatiamento,cria-se uma copia de c dentro de d
d[2]= 9
print(f'\nA lista C : {c}')
print(f'A lista D : {d}')