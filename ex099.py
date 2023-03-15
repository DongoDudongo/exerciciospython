brasil =[]
estado = {}
for  c in range (0,3):
    estado['uf'] = str(input('Unidade federativa:'))
    estado['sigla'] = str(input('Sigla:'))
    brasil.append(estado.copy())
#não pode usar fatiamento ,da erro,serve só para listas.
for e in brasil:
    for v in e.values():
        print(v,end='')
    print()
