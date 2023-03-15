from time import sleep

from pygame import mixer

print('VAMOS COMEÇAR NOSSA CONTAGEM PARA O ANO NOVO!!')

sleep(1)
for c in range(10 , 0 , -1):
    print(c)
    sleep(1)

mixer.init()
mixer.music.load('ex019.mp3')
mixer.music.play()

sleep(15)