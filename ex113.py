def voto(ano):
    from datetime import datetime
    print('-'*30)
    a = datetime.today().year
    s = a - ano
    if s < 18:
        return f'Com {s} anos :Não vota.'
    elif 18 <= s <= 64:
        return f'com {s} anos :VOTO OBRIGATÓRIO.'
    elif s >= 65:
        return f'Com {s} anos :VOTO OPCIONAL.'

nasc = int(input('Em que ano você nasceu?'))
print(voto(nasc))

