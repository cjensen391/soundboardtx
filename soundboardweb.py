import PySimpleGUIWeb as sgw
import soundboardplay
#Port for WEBSERVER
webPort = 2222

MAX_ROWS, MAX_COL = soundboardplay.qtyRowCol()


#Button Layout for PysimpleGUIWeb
layout = [[sgw.Button('+', size=(13, 10), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
window = sgw.Window('Soundboard.tx', layout,web_port=webPort, web_start_browser=False)

#creates dictionary with list of files and positions from zip object
dicOfFiles = dict(soundboardplay.assignFiles(MAX_COL))

while True:
    # The Event Loop
    event, values = window.read()
    #print(event, values)
    if event == sgw.WIN_CLOSED or event == 'Exit':
        break
    if event in dicOfFiles.keys():
        soundboardplay.playSound(dicOfFiles[event])
        #print(str(soundboardplay.lengthOfSound(dicOfFiles[event])))
    else:
        print('no file assigned')

window.close()