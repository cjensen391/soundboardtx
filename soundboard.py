import PySimpleGUI as sg
import soundboardplay

#row/column declaration
ROWS,COL = soundboardplay.qtyRowCol()


#Button Layout for PysimpleGUI
layout = [[sg.Button('+', size=(13, 10), key=(i,j), pad=(0,0)) for j in range(COL)] for i in range(ROWS)]
window = sg.Window('Soundboard.tx', layout)

#creates dictionary with list of files and positions from zip object
dicOfFiles = dict(soundboardplay.assignFiles(COL))

while True:
    # The Event Loop
    event, values = window.read()
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event in dicOfFiles.keys():
        soundboardplay.playSound(dicOfFiles[event])
        #print(str(soundboardplay.lengthOfSound(dicOfFiles[event])))
    else:
        print('no file assigned')

window.close()