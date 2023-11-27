import PySimpleGUI as sg
import os

sg.theme('DarkAmber')

layout = [[sg.Text("PyQt Builder", size=(27,2),justification='c',font=(15))],[sg.Button('Build', size=(30,1))],[sg.Button("Build As Python File", size=(30,1))],[sg.Button("Always On Top", size=(30,1))],[sg.Button('Exit', size=(30,1))]]

window = sg.Window('PyQt Builder', layout)

is_on_top = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Run':
        # Run the PyQt app with uic
        os.system('python test.py')
    if event == 'Build As Python File':
        # Build the PyQt app with pyuic5 -x test.ui -o test.py
        os.system('pyuic5 -x test.ui -o test.py')
        # Run the PyQt app with python test.py
        os.system('python test.py')
    if event == 'Always On Top':
        if is_on_top:
            window.TKroot.attributes("-topmost", False)
            is_on_top = False
        else:
            window.TKroot.attributes("-topmost", True)
            is_on_top = True

