import PySimpleGUI as sg
import soundboardplay

MAX_ROWS = MAX_COL = soundboardplay.countSounds()

layout = [[sg.Button('+', size=(13, 10), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

window = sg.Window('Soundboard.tx', layout)
soundboardplay.namesOfFiles()
while True:                             # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == (1, 0):
        soundboardplay.playSound('mission.wav')
window.close()
        







