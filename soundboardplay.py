import os
import pygame
import glob

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
txsound = 'tx.wav'

channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel0.set_volume(1.0,0.0)
channel1.set_volume(0.0,1.0)
path = os.getcwd()

def playSound(sound):
    channel1.play(pygame.mixer.Sound(path +'/sounds/'+ sound))
    channel0.play(pygame.mixer.Sound(path + '/sounds/' + txsound))

def countSounds():
    wav_counter = len(glob.glob1(path + '/sounds/', '*.wav'))
    print(wav_counter)
    return wav_counter

def qtyRowCol(numofsounds):
    return()

