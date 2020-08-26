import PySimpleGUI as sg
import soundboardplay

#row/column declaration
MAX_ROWS = MAX_COL = soundboardplay.qtyRowCol()

#Button Layout for PysimpleGUI
layout = [[sg.Button('+', size=(13, 10), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
window = sg.Window('Soundboard.tx', layout)

#creates dictionary with list of files and positions from zip object
dicOfFiles = dict(soundboardplay.assignFiles(MAX_ROWS))
while True:
    # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event in dicOfFiles.keys():
        soundboardplay.playSound(dicOfFiles[event])
    else:
        print('no file assigned')
window.close()
        







