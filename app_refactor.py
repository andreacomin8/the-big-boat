# Dicitura per Pyinstaller:
# os.chdir(sys._MEIPASS)
# import sys, os

import pandas as pd
import json
from tkinter.ttk import *
from tkinter import *
import PIL.Image
from PIL import ImageTk, ImageOps
from random import choice
from tkinter import messagebox as mb

# todo: import classes from outer files
from page_classes import page_launcher
# from page_classes.father_page import GuiPage
# from page_classes.landing_page import LandingPage


def start_application():
    page_launcher.launch_landing_page()

start_application()



