import os
import pygame
import glob
import math
#import audiolab, scipy

path = os.getcwd()


#pygame initilization and setting levels/aliases
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
txsoundp = 'tx.wav'
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel0.set_volume(1.0,0.001)
channel1.set_volume(0.001,1.0)





def playSound(sound):
   # a , fs, enc = audiolab.wavread(path+'/sounds/'+sound)
   # b, fs, enc = audiolab.wavread(path+'/sounds/'+txsound)
   # c = scipy.vstack((a,b))
   # audiolab.wavwrite(c,path+'/sounds/'+sound)
    soundobj = pygame.mixer.Sound(path + '/sounds/' + sound)
    txsound = pygame.mixer.Sound(path + '/sounds/' + txsoundp)
    soundobj.set_volume(1.0)
    txsound.set_volume(1.0)
    txsound.play(maxtime=math.ceil(soundobj.get_length()))
    soundobj.play()


def countSounds():
    #Counts Files in /sounds/ folder. MP3 Play not implmented
    wav_counter = len(glob.glob1(path + '/sounds/', '*.wav')) - 1 #tx_tone
    #mp3_counter = len(glob.glob1(path + '/sounds/', '*.mp3'))
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
    position_map = zip(makelistofpositions(numofrows),namesOfFiles())
    return(position_map)




