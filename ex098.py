pessoas ={'nome':'Ana','Idade':29,'Sexo': 'F'}
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k,v in pessoas.itens():
    print(f'{k} = {v}')
#keys são os valores inicias,os denominadores dos dicionários
#values são os valores que se encontram dentro das keys
#itens funcionam como um marcador que engloba todas as keys com seus valores,caso haja duas keys iguais fica enumerado como itens[0] e itens[1]