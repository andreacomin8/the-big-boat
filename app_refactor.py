# Dicitura per Pyinstaller:
import os, sys
#os.chdir(sys._MEIPASS)


# todo: import classes from outer files
import page_launcher


def start_application():
    page_launcher.launch_landing_page()

start_application()



