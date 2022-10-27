from tkinter import *
from page_classes import landing_page, setup_quiz_base


def launch_landing_page():
    tk_object = Tk()

    # retrieve_page_content()
    a = landing_page.LandingPage(tk_object, 630, 400, "Quiz Patente Nautica - Menu Iniziale", "#b8e6fe")
    a.show_page()


def launch_setup_quiz_base_page():
    tk_object = Tk()

    # retrieve_page_content()
    a = setup_quiz_base.SetupQuizBasePage(tk_object, 730, 780, "Setup Quiz Base", "#b8e6fe")
    a.show_page()


def pages_transition(page_2_destroy, to_create):
    map_pages = {
        "landing_page": launch_landing_page,
        "setup_quiz_base": launch_setup_quiz_base_page,
        "setup_quiz_vela": 2,
        "quiz": 2,
        "results": 2
    }
    page_2_destroy.destroy()
    map_pages[to_create]()
