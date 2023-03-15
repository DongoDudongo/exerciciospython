n = [2,3,6,9,4]
print(n)
n[2]= 7 # substitue o valor  por outro na posição designada dentro do []
print(n)
n.append(8) # acrescenta um núemro no fim da lista
print(n)
n.sort(reverse=True) #reverte a ordem
print(n)
n.insert(2,0) #insere o valor(0) na posição designada(2),sempre será posição e dps valor
print(n)
print(f'Essa lista tem {len(n)} elementos.') #Contar os elementos da lista
n.pop(2) # remove pela posição
print(n)
n.remove(9) # remove o valor ou dado especifico da lista ,caso acha algum valor
# ou palavra igual,será o primeiro a ser elimidado
print(n)
if 10 in n:
    n.remove(10)
else:
    print('Não achei esse valor')

