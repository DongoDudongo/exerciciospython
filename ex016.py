import math
angulo = float(input('digite um ângulo:'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(' o angulo {}° tem  seno {:.2f}°,cosseno {:.2f}° e tangente de {:.2f}°'.format(angulo,sen,cos,tang))