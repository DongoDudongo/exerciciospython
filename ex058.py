#sexo = str(input('Qual seu sexo [M/F]?')).upper().strip()[0]

#while sexo != 'F' or sexo != 'M':
   # sexo = str(input('Dados inválidos ,poderia repetir [M/F]?')).upper().strip()[0]
    #if sexo =='M' or sexo == 'F':
        #print('Agora posso continuar a pesquisa,obrigado!')
       # break

#print('fim')


s = str(input('qual seu sexo [M/F]?')).strip().upper()[0]
while s not in 'MF':
    S = str(input('dados inválidos,qual é seu sexo [M/F]?')).strip().upper()[0]
print('FIM')