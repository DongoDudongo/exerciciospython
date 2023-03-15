cidade = str(input('Digite um nome de cidade:')).strip()
print('Essa cidade tem o nome Santo? {}'.format(cidade[0:].upper() == 'SANTO'))
print('tem certeza? {}'.format('SANTO' in cidade.upper()))

#caso não queira escrever ".format(nome.upper().count()"
#pode se usar str(input()).upper

nome = str(input('digite um nome:')).strip()
print('seu nome tem silva? {}'.format('silva' in nome.lower()))
print('A letra A apareceu {} vezes '.format(nome.upper().count('A')))
print('A primeira letra A está na posição {}'.format(nome.upper().find('A')+1))
print('a Ultima aparição da letra A foi na posição {}'.format(nome.upper().rfind('A')+1))

#o mesmo efeito da linha superior do "nome" conseguimos nessa sequencia de codigo

frase = str(input('digite uma frase :')).upper().strip()
print('A frase tem {} letras A'.format(frase.count('A')))
print('A primeira posição dela é {}'.format(frase.find('A')+1))
print('A ultima posição é {}'.format(frase.rfind('A')+1))

n2 = str(input('Digite seu nome completo:')).strip()
n3 = n2.split()
print('O seu primeiro nome é {}'.format(n3[0]))
print('O seu ultimo nome é {}'.format(n3[len(n3)-1]))

