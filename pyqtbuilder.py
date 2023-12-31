import PySimpleGUI as sg
import os
import threading
import time

sg.theme('DarkAmber')

layout = [[sg.Text("PyQt Builder", size=(27, 2), justification='c', font=15)], [sg.Button('Run', size=(37, 1))],[sg.Button("Always On Top", size=(37, 1))],
[sg.Button('Exit', size=(37, 1))]]

window = sg.Window('PyQt Builder', layout)

is_on_top = False

def hot_reload_thread():
    global last_mtime_test_py, last_mtime_test_ui

    # Initialize last modified times
    last_mtime_test_py = os.path.getmtime('test.py') if os.path.exists('test.py') else 0
    last_mtime_test_ui = os.path.getmtime('test.ui') if os.path.exists('test.ui') else 0

    while True:
        # Check if test.py or test.ui has changed
        if os.path.exists('test.py') and os.path.getmtime('test.py') > last_mtime_test_py:
            # Close the current window
            if event == sg.WIN_CLOSED:
                hot_reload_thread.exit()

            # Restart the PyQt app
            os.system('python test.py')

            # Update last modified time
            last_mtime_test_py = os.path.getmtime('test.py')

        if os.path.exists('test.ui') and os.path.getmtime('test.ui') > last_mtime_test_ui:
            # Close the current window
            if event == sg.WIN_CLOSED:
                hot_reload_thread.exit()

            # Restart the PyQt app
            os.system('python test.py')

            # Update last modified time
            last_mtime_test_ui = os.path.getmtime('test.ui')

        # Sleep for a second
        time.sleep(1)

last_mtime_test_py = 0
last_mtime_test_ui = 0

# Start hot reload thread
hot_reload_thread = threading.Thread(target=hot_reload_thread)
hot_reload_thread.start()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Run':
        # Run the PyQt app with uic
        os.system('python test.py')
    if event == 'Always On Top':
        if is_on_top:
            window.TKroot.attributes("-topmost", False)
            is_on_top = False
        else:
            window.TKroot.attributes("-topmost", True)
            is_on_top = True

# Stop hot reload thread when window is closed
hot_reload_thread.join()
