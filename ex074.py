time =  ('palmeiras','internacional','fluminense','corinthians','flamengo','athlético - PR','athlético -MG','fortaleza',
         'são paulo','américa-MG','botafogo','santos','goias','bragantino','coritiba','cuiabá','ceara SC',
         'athletico-GO','avai','juventude')

print('='* 30)
print(f'Os times em ordem alfabética fica :\n{sorted(time)}')
print('='*30)
print(f'Os cinco primeiros são :\n{time[0:6]}')
print('='*30)
print(f'Os 5 ultimos:\n{time[-5:]}')
print('='*30)
print(f'O corinthians está noa {time.index("corinthians")+1}ª psoição')