import json
from father_page import GuiPage
from quiz_generator import QuizGenerator
from tkinter.ttk import *
from tkinter import *
import PIL.Image
from PIL import ImageOps, ImageTk, Image



def load_initial_data(base_questions_path, sail_questions_path):
    # read json
    with open(base_questions_path) as f:
        base_df = json.load(f)
    with open(sail_questions_path) as f:
        sail_df = json.load(f)
    return base_df, sail_df


base_questions, sail_questions = load_initial_data(base_questions_path='page_classes/data/base_data.json',
                                                   sail_questions_path='page_classes/data/vela_data.json')


# test ****************************************
def topic_quiz(topic_selected, q_number):
    print('\nTOPIC\n')
    test_topic = QuizGenerator(base_questions, topic_selected=topic_selected, q_number=q_number).topic()
    print(test_topic)
    for i in test_topic:
        print(base_questions['domande'][i])


def search_quiz(word_searched):
    print('\nSEARCH\n')
    test_search = QuizGenerator(base_questions, word_searched=word_searched).search()
    print(test_search)
    for i in test_search:
        print(base_questions['domande'][i])


def exam_quiz():
    print('\nEXAM\n')
    test_exam = QuizGenerator(base_questions).exam()
    print(test_exam)
    for i in test_exam:
        print(base_questions['domande'][i], base_questions['opzioni_risposta'][i])
# test ****************************************


class QuizPage(GuiPage):
    def __init__(self, tk_object, width, height, title, background, q_index_generated):
        super().__init__(tk_object, width, height, title, background, q_index_generated)
        self.q_indeces_list = q_index_generated
        self.q_no = 1
        self.i = 0
        self.q_selected_index = self.q_indeces_list[self.i]
        self.create_base_structure()
        self.display_info()
        self.display_q()
        self.display_options()
        self.display_image()

    def create_base_structure(self):
        global header_img
        global l1
        header_img = PhotoImage(file='Images/Images_modalità/header_esame.png')
        l1 = Label(self.tk_object, image=header_img)

        global canvas_info
        global canvas_question
        global canvas_options
        global canvas_image
        global canvas_buttons
        global canvas_footer

        canvas_info = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_question = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_options = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_image = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_buttons = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_footer = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')

        l1.pack()
        canvas_info.pack()
        canvas_question.pack()
        canvas_options.pack()
        canvas_image.pack()
        canvas_buttons.pack()
        canvas_footer.pack

        def next_commnad():
            self.get_next_q_index()
            self.create_next_window()

        Button(canvas_buttons, text='next', command=next_commnad).pack()

    def get_next_q_index(self):
        if self.q_no < len(self.q_indeces_list):
            self.q_no += 1
            self.i += 1
            self.q_selected_index = self.q_indeces_list[self.i]

            return self.q_selected_index
        else:
            return None

    def create_next_window(self):
        l1.destroy()
        canvas_info.destroy()
        canvas_question.destroy()
        canvas_options.destroy()
        canvas_image.destroy()
        canvas_buttons.destroy()
        canvas_footer.destroy()

        self.create_base_structure()
        self.display_info()
        self.display_q()
        self.display_options()
        self.display_image()

    def display_info(self):
            text = base_questions['tema'][self.q_selected_index]
            Label(canvas_info, text=text).pack()

    def display_q(self):
            text = base_questions['domande'][self.q_selected_index]
            Label(canvas_question, text=text).pack()

    def display_options(self):
        for option in base_questions['opzioni_risposta'][self.q_selected_index]:
            Label(canvas_options, text=option).pack()

    def display_image(self):
        global q_img
        q_img = 0
        if base_questions['immagine'][self.q_selected_index] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(base_questions['immagine'][self.q_selected_index]) + '.jpg')
            image = ImageOps.contain(image, (150, 150))
            q_img = ImageTk.PhotoImage(image)
            canvas_image.create_image(0, 0, anchor=NW, image=q_img)
        else:
            return None
