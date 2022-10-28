from tkinter import *
from page_classes import landing_page, setup_quiz_base,choose_modality, setup_modality


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

def launch_choose_modality_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = choose_modality.ChooseModalityPage(tk_object, 920, 720, "Scegli la modalità", "#b8e6fe")
    a.show_page()

def launch_topic_modality_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, 730,380, "Modalità Seleziona Argomento", "#b8e6fe").topic_modality()
    a.show_page()



def launch_search_modality_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, 730,380, "Modalità Seleziona Argomento", "#b8e6fe").search_modality()
    a.show_page()


def launch_error_modality_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, 730,380, "Modalità Seleziona Argomento", "#b8e6fe").error_modality()
    a.show_page()




def pages_transition(page_2_destroy, to_create):
    map_pages = {
        "landing_page": launch_landing_page,
        "setup_quiz_base": launch_setup_quiz_base_page,
        "choose_modality": launch_choose_modality_page,
        "setup_topic_modality" : launch_topic_modality_page,
        "setup_search_modality": launch_search_modality_page,
        "setup_error_modality": launch_error_modality_page,
        "setup_quiz_vela": 2,
        "quiz": 2,
        "results": 2
    }
    page_2_destroy.destroy()
    map_pages[to_create]()
