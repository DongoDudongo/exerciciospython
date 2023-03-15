c = float(input('digite a temperatura :'))

f = (c*9/5)+32

k = c + 273.15

print('A temperatura de {}°c, fica em {} f e {} k'.format(c,f,k))

a = int(input('Bom dia,por quanto tempo pretende alugar nosso serviço de carros?'))
ap = a * 60
k = float(input('seja bem vindo  de volta,quanto Km você percorreu com nosso veículo?'))
kp = k*0.15
pt = ap +kp
print('Sua conta senhor,o aluguel ficou em R${},a taxa de Km ficou R${},o Total a ser pago ficou em R${}'.format(ap,kp,pt))