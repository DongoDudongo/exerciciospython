cores = {'limpa':'\033[m',
        'azul': '\033[0;34m',
     'vermelho' : '\033[0;31m' ,
     'verde' : '\033[0;32m'}
#condição aninhada

nome = str(input('Qual seu nome?'))

if nome == 'Ana Carolina'or nome == 'Ana':
    print('qua nome lindo esse seu {}{}{}.'.format(cores['vermelho'],nome,cores['limpa']))
elif nome == 'Pedro' or  nome == "Maria" or nome == 'João':
    print('Esse seu nome é bem comum no Brasil.')
elif nome in 'Tânia,Creuza,Marina,Selma':
    print('Parce nome de mãe.')
else: #não é necessário para exemplificar o "senão'
    print('seu nome é bem comum.')

print('Olá {}{}{},é um prazer te conhecer.'.format(cores['azul'],nome,cores['limpa']))