# Dicitura per Pyinstaller:
import os, sys
os.chdir(sys._MEIPASS)

import page_launcher
from tkinter import messagebox as mb
from datetime import datetime

today = datetime.now()
exp_date = datetime(2022, 12, 15)

def start_application():
    page_launcher.launch_landing_page()

if today < exp_date:
    start_application()
else:
    mb.showwarning("Attenzione Licenza Scaduta")





