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


def load_initial_data(base_questions_path, sail_questions_path):
    # read json
    with open(base_questions_path) as f:
        base_df = json.load(f)

    base_df = pd.DataFrame(base_df)
    question = base_df['domande']
    options = base_df['opzioni_risposta']
    answer = base_df['risposta_corretta']
    figure = base_df['immagine']
    tema = base_df['tema']

    with open(sail_questions_path) as f:
        sail_data = json.load(f)

    # todo rimuovere pandas
    sail_df = pd.DataFrame(sail_data)
    question_vela = sail_df['Domanda']
    answer_vela = sail_df['V_F']
    tema_vela = sail_df['Argomento']
    sottocategoria_vela = sail_df['sottocategoria']
    options_vela = ['Vero', 'Falso']
    figure_vela = sail_df['Immagini']

    return base_df, sail_df


def start_application():
    base_questions, sail_questions = load_initial_data(base_questions_path='questions_data.json',
                                                       sail_questions_path='quiz_vela.json')
    page_launcher.launch_landing_page()


start_application()


# def page_transition(page_to_close, page_to_open):
#     page_to_close.destroy()
