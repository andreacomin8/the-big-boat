# Dicitura per Pyinstaller:
#import sys, os
#os.chdir(sys._MEIPASS)


# todo: import classes from outer files
from page_classes import page_launcher
# from page_classes.father_page import GuiPage
# from page_classes.landing_page import LandingPage


def start_application():
    page_launcher.launch_landing_page()

start_application()



