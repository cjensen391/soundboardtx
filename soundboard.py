import PySimpleGUI as sg
import soundboardplay

MAX_ROWS = MAX_COL = 10

layout = [[sg.Button('+', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

window = sg.Window('Soundboard.tx', layout)
soundboardplay.countSounds()
while True:                             # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == (1, 0):
        soundboardplay.playSound('mission.wav')
window.close()
        







