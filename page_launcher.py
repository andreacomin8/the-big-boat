from tkinter import *
import quiz_page
import choose_modality
import setup_modality
import landing_page
from quiz_page import base_questions, sail_questions
from quiz_generator import QuizGenerator
from tkinter import messagebox as mb
import json, random


# windows size
landing_page_width = 620
landing_page_height = 500
choose_modality_width = 920
choose_modality_height = 720
setup_modality_width = 920
setup_modality_height = 380
quiz_width = 920
quiz_height = 790


def launch_landing_page():
    tk_object = Tk()
    tk_object.resizable(True, True)
    a = landing_page.LandingPage(tk_object, landing_page_width, landing_page_height, "Quiz Patente Nautica - Menu Iniziale", "#b8e6fe")
    a.show_page()
    # a.set_scaling_dpi(tk_object)


def launch_choose_modality_page_base():
    tk_object = Tk()
    tk_object.resizable(True, True)
    # retrieve_page_content()
    a = choose_modality.ChooseModalityPageBase(tk_object, choose_modality_width, choose_modality_height, "Scegli la modalità", "#b8e6fe",
                                               header_path=headers_path["base"])
    a.back_button(lambda: pages_transition(tk_object, "landing_page"))
    a.show_page()


def launch_choose_modality_page_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    # retrieve_page_content()
    a = choose_modality.ChooseModalityPageVela(tk_object, choose_modality_width, choose_modality_height, "Scegli la modalità", "#b8e6fe",
                                               header_path=headers_path["vela"])
    a.back_button(lambda: pages_transition(tk_object, "landing_page"))
    a.show_page()


def launch_topic_modality_page():
    tk_object = Tk()
    tk_object.resizable(False, False)
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, setup_modality_width, setup_modality_height, "Modalità Seleziona Argomento",
                                         color_modality['topic'],
                                         header_path=headers_path['topic'])
    a.topic_modality_base()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_topic_modality_page_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    # retrieve_page_content()
    a = setup_modality.SetupModalityPage(tk_object, setup_modality_width, setup_modality_height,
                                         "Modalità Seleziona Argomento",
                                         color_modality['topic'],
                                         header_path=headers_path['topic'])
    a.topic_modality_vela()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_vela"))
    a.show_page()


def launch_search_modality_page():
    tk_object = Tk()
    tk_object.resizable(False, False)
    a = setup_modality.SetupModalityPage(tk_object, setup_modality_width, setup_modality_height, "Modalità Ricerca Avanzata",
                                         color_modality['search'],
                                         header_path=headers_path['search'])
    a.search_modality_base()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_search_modality_page_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    a = setup_modality.SetupModalityPage(tk_object, setup_modality_width, setup_modality_height,
                                         "Modalità Ricerca Avanzata",
                                         color_modality['search'],
                                         header_path=headers_path['search'])
    a.search_modality_vela()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_vela"))
    a.show_page()


def launch_error_modality_page():
    tk_object = Tk()
    tk_object.resizable(False, False)
    a = setup_modality.SetupModalityPage(tk_object, setup_modality_width, setup_modality_height,
                                         "Modalità Errori Commessi",
                                         color_modality['error'],
                                         header_path=headers_path['error'])
    a.error_modality_base()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_error_modality_page_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    a = setup_modality.SetupModalityPage(tk_object, setup_modality_width, setup_modality_height,
                                         "Modalità Errori Commessi",
                                         color_modality['error'],
                                         header_path=headers_path['error'])
    a.error_modality_vela()
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_vela"))
    a.show_page()


def launch_quiz_exam_base():
    tk_object = Tk()
    tk_object.resizable(False,False)
    a = quiz_page.QuizPage(tk_object, base_questions, quiz_width, quiz_height, "Quiz!",
                           color_modality['exam'],
                           QuizGenerator(base_questions).exam_base(),
                           header_path=headers_path['exam'])
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()



def launch_quiz_topic_base():
    tk_object = Tk()
    tk_object.resizable(False, False)
    a = quiz_page.QuizPage(tk_object, base_questions, quiz_width, quiz_height,
                           "Quiz!",
                           color_modality['topic'],
                           QuizGenerator(base_questions, topic_selected =topic_selected, q_number=num_dom).topic(),
                           header_path=headers_path['topic'])
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
    a.show_page()


def launch_quiz_search_base():
    tk_object = Tk()
    tk_object.resizable(True, True)
    if QuizGenerator(base_questions, word_searched=word_searched).search():
        a = quiz_page.QuizPage(tk_object, base_questions, quiz_width, quiz_height,
                               "Quiz!", color_modality['search'],
                               QuizGenerator(base_questions, word_searched=word_searched).search(),
                               header_path=headers_path['search'])
        a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
        a.show_page()
    else:
        mb.showwarning("Attnezione", "La parola cercata non è stata trovata.\nEffettua una nuova ricerca!")
        pages_transition(tk_object, "setup_search_modality")


def launch_quiz_error_base():
    tk_object = Tk()
    tk_object.resizable(False, False)
    #read json with saved questions
    with open('saved.json', 'r') as file:
        data = json.load(file)
    question_list = data['domande_salvate_base']
    #check if question_list is not empty
    if len(question_list) == 0:
        mb.showwarning("Attenzione", "Al momento non ci sono domande sbagliate in memoria.")
        pages_transition(tk_object, "setup_error_modality")
    else:
        q_list = random.sample(question_list, k=num_dom)
        a = quiz_page.QuizPage(tk_object, base_questions, quiz_width, quiz_height,
                               "Quiz!", color_modality['error'],
                               q_list,
                               header_path=headers_path['error'])
        a.back_button(lambda: pages_transition(tk_object, "choose_modality_base"))
        a.show_page()


def launch_quiz_topic_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    # retrieve_page_content()
    a = quiz_page.QuizPage(tk_object, sail_questions, quiz_width, quiz_height, "Quiz!", color_modality['topic'], QuizGenerator(sail_questions, topic_selected =topic_selected, q_number=num_dom).topic_vela(), header_path=headers_path['topic'])
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_vela"))
    a.show_page()


def launch_quiz_search_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    if QuizGenerator(sail_questions, word_searched=word_searched).search():
        # retrieve_page_content()
        a = quiz_page.QuizPage(tk_object, sail_questions, quiz_width, quiz_height, "Quiz!", color_modality['search'], QuizGenerator(sail_questions, word_searched=word_searched).search(), header_path=headers_path['search'])
        a.back_button(lambda: pages_transition(tk_object, "choose_modality_vela"))
        a.show_page()
    else:
        mb.showwarning("Attnezione", "La parola cercata non è stata trovata.\nEffettua una nuova ricerca!")
        pages_transition(tk_object, "setup_search_modality_vela")


def launch_quiz_exam_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    # retrieve_page_content()
    a = quiz_page.QuizPage(tk_object, sail_questions, quiz_width, quiz_height, "Quiz Vela!", color_modality['exam'], QuizGenerator(sail_questions).exam_vela(), header_path=headers_path['exam'])
    a.back_button(lambda: pages_transition(tk_object, "choose_modality_vela"))
    a.show_page()


def launch_quiz_error_vela():
    tk_object = Tk()
    tk_object.resizable(False, False)
    #read json with saved questions
    with open('saved.json', 'r') as file:
        data = json.load(file)
    question_list = data['domande_salvate_vela']
    #check if question_list is not empty
    if len(question_list) == 0:
        mb.showwarning("Attenzione", "Al momento non ci sono domande sbagliate in memoria.")
        pages_transition(tk_object, "setup_error_modality_vela")
    else:
        q_list = random.sample(question_list, k=num_dom)
        a = quiz_page.QuizPage(tk_object, sail_questions, quiz_width, quiz_height,
                               "Quiz!", color_modality['error'],
                               q_list,
                               header_path=headers_path['error'])
        a.back_button(lambda: pages_transition(tk_object, "choose_modality_vela"))
        a.show_page()


def pages_transition(page_2_destroy, to_create, entry_word=None, numero_domande=None, argomento_selezionato=None):
    global word_searched
    if entry_word:
        word_searched = entry_word

    global num_dom
    if numero_domande:
        num_dom = numero_domande

    global topic_selected
    if argomento_selezionato:
        topic_selected = argomento_selezionato

    map_pages = {
        "landing_page": launch_landing_page,
        "choose_modality_base": launch_choose_modality_page_base,
        "choose_modality_vela": launch_choose_modality_page_vela,
        "setup_topic_modality": launch_topic_modality_page,
        "setup_search_modality": launch_search_modality_page,
        "setup_error_modality": launch_error_modality_page,
        "setup_topic_modality_vela": launch_topic_modality_page_vela,
        "setup_search_modality_vela":launch_search_modality_page_vela,
        "setup_error_modality_vela": launch_error_modality_page_vela,
        "quiz_topic_base": launch_quiz_topic_base,
        "quiz_search_base": launch_quiz_search_base,
        "quiz_esame_base": launch_quiz_exam_base,
        "quiz_error_base":launch_quiz_error_base,
        "quiz_search_vela": launch_quiz_search_vela,
        "quiz_topic_vela": launch_quiz_topic_vela,
        "quiz_esame_vela": launch_quiz_exam_vela,
        "quiz_error_vela": launch_quiz_error_vela,

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

