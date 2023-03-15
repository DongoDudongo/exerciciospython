boletim = {}

boletim['nome']=str(input('Nome:'))
boletim['média']= float(input('Média:'))
if boletim['média'] >= 7:
    boletim['situação'] = 'Aprovado'
else:
    boletim['situação'] = 'Reprovado'
print('-='*30)
for k,v in boletim.items():
    print(f'--{k} é igual {v}')