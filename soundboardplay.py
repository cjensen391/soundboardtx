import os
import pygame

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
txsound = ''

channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel0.set_volume(1.0,0.0)
channel1.set_volume(0.0,1.0)
path = os.getcwd()

def playSound(sound):
    channel1.play(pygame.mixer.Sound(path +'/sounds/'+ sound))
#channel0.play(pygame.mixer.Sound('sounds/'+ txsound))

##def countSounds():
#    count=0
#    for path in os.listdir(path + '/sounds/'):
#        if os.path.isfile(os.path.join())

