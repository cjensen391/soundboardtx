import os
import pygame
import glob
import math

#pygame initilization and setting levels/aliases
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
txsound = 'tx.wav'
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel0.set_volume(1.0,0.002)
channel1.set_volume(0.002,1.0)
path = os.getcwd()

def lengthOfSound(sound):
    return pygame.mixer.Sound.get_length(path + '/sounds/'+ sound)

def playSound(sound):
    #plays sound on right ch and tx activation sound on left channel
    channel1.play(pygame.mixer.Sound(path +'/sounds/'+ sound))
    channel0.play(pygame.mixer.Sound(path + '/sounds/' + txsound),maxtime=1000)

def countSounds():
    #Counts Files in /sounds/ folder. MP3 Play not implmented
    wav_counter = len(glob.glob1(path + '/sounds/', '*.wav')) - 1 #tx_tone
    mp3_counter = len(glob.glob1(path + '/sounds/', '*.mp3'))
    print(wav_counter)
    print (mp3_counter)
    return wav_counter


def qtyRowCol():
    rows = 1
    if countSounds() >= 9:
        columns  = 9
        rows = math.ceil(countSounds()/9)
        return (rows,columns)
    if countSounds() <= 9:
        columns = countSounds()
        return(rows,columns)

def namesOfFiles():
    # Gets the names of all the mp3 and wav files and returns list
    names = []
    count = 0
    extensions = ('.mp3', '.wav')
    for subdir, dirs, files in os.walk(path+'/sounds/'):
        for file in files:
            count += 1
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                names.insert(count,os.path.join(file))
    return(names)

def makelistofpositions(numofrows):
    ##Makes list of positions availible
    positions = []
    for row in range(numofrows):
        for column in range(numofrows):
            positions.append((row,column))
    return positions

def assignFiles(numofrows):
    #assigns files to positons
    file_positions = {}
    names = namesOfFiles()
    position_map = zip(makelistofpositions(numofrows),namesOfFiles())
    return(position_map)




