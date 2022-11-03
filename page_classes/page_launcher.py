from tkinter import *
from page_classes import landing_page, choose_modality, setup_modality,quiz_page
from quiz_page import base_questions
from quiz_generator import QuizGenerator



def launch_landing_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = landing_page.LandingPage(tk_object, 620, 500, "Quiz Patente Nautica - Menu Iniziale", "#b8e6fe")
    a.show_page()


def launch_choose_modality_page_base():
    tk_object = Tk()
    # retrieve_page_content()
    a = choose_modality.ChooseModalityPage(tk_object, 920, 720, "Scegli la modalità", "#b8e6fe",
                                           header_path=headers_path["base"])
    a.back_button(lambda: pages_transition(tk_object, "landing_page"))
    a.show_page()

def launch_choose_modality_page_vela():
    tk_object = Tk()
    # retrieve_page_content()
    a = choose_modality.ChooseModalityPage(tk_object, 920, 720, "Scegli la modalità", "#b8e6fe",
                                           header_path=headers_path["vela"])
    a.back_button(lambda: pages_transition(tk_object, "landing_page"))
    a.show_page()

#todo logica back button, dovrebbe salvare precedente
def launch_topic_modality_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, 920, 380, "Modalità Seleziona Argomento", color_modality['topic'], header_path=headers_path['topic'])
    a.topic_modality()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_search_modality_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, 920, 380, "Modalità Ricerca Avanzata", color_modality['search'], header_path=headers_path['search'])
    a.search_modality()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_error_modality_page():
    tk_object = Tk()
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, 920, 380, "Modalità Errori Commessi", color_modality['error'], header_path=headers_path['error'])
    a.error_modality()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_quiz_exam_base():
    tk_object = Tk()
    # retrieve_page_content()
    a = quiz_page.QuizPage(tk_object, 920, 800, "Quiz!", color_modality['exam'], QuizGenerator(base_questions).exam(), header_path=headers_path['exam'])
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


# todo capire come passargli i parametri topic_Selcted e q_number al QuizGenerator
def launch_quiz_topic_base():
    tk_object = Tk()
    # retrieve_page_content()
    a = quiz_page.QuizPage(tk_object, 920, 800, "Quiz!", color_modality['topic'], QuizGenerator(base_questions, topic_selected="COLREG E SEGNALAMENTO MARITTIMO", q_number=2 ).topic(), header_path=headers_path['topic'])
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_quiz_search_base():
    tk_object = Tk()
    # retrieve_page_content()
    a = quiz_page.QuizPage(tk_object, 920, 800, "Quiz!", color_modality['search'], QuizGenerator(base_questions, word_searched='figur').search(), header_path=headers_path['search'])
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def pages_transition(page_2_destroy, to_create):
    map_pages = {
        "landing_page": launch_landing_page,
        # "setup_quiz_base": launch_setup_quiz_base_page,
        "choose_modality_base": launch_choose_modality_page_base,
        "choose_modality_vela": launch_choose_modality_page_vela,
        "setup_topic_modality": launch_topic_modality_page,
        "setup_search_modality": launch_search_modality_page,
        "setup_error_modality": launch_error_modality_page,
        "quiz_esame_base": launch_quiz_exam_base,
        "quiz_topic_base": launch_quiz_topic_base,
        "quiz_search_base": launch_quiz_search_base,
        "setup_quiz_vela": 2,
        "quiz": 2,
        "results": 2
    }
    page_2_destroy.destroy()
    map_pages[to_create]()


headers_path = {
    "base": 'Images/header_base.png',
    "vela": 'Images/header_vela.png',
    "exam": 'Images/Images_modalità/header_esame.png',
    "topic": 'Images/Images_modalità/header_topic.png',
    "search": 'Images/Images_modalità/header_search.png',
    "error": 'Images/Images_modalità/header_error.png'
}

color_modality = {
    "exam": "#ffd094",
    "topic": "#e1ffd7",
    "search": "#b8e6fe",
    "error": "#ffc2c3"
}

