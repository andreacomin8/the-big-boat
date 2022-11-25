# Dicitura per Pyinstaller:
import os, sys
#os.chdir(sys._MEIPASS)

import page_launcher
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)


def start_application():
    page_launcher.launch_landing_page()

start_application()




