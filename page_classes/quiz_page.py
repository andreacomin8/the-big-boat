import json
from father_page import GuiPage
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox as mb
import PIL.Image
from PIL import ImageOps, ImageTk
# todo Se importo pages_transition, non funziona la funzione WTF?
# from page_launcher import pages_transition


def load_initial_data(base_questions_path, sail_questions_path):
    # read json
    with open(base_questions_path) as f:
        base_df = json.load(f)
    with open(sail_questions_path) as f:
        sail_df = json.load(f)
    return base_df, sail_df


base_questions, sail_questions = load_initial_data(base_questions_path='page_classes/data/base_data.json',
                                                   sail_questions_path='page_classes/data/vela_data.json')



class QuizPage(GuiPage):
    def __init__(self, tk_object, width, height, title, background, question_index_list_generated, header_path):
        super().__init__(tk_object, width, height, title, background, question_index_list_generated)
        self.background = background
        # self.data = data
        self.question_index_list_generated = question_index_list_generated
        self.q_no = 1
        self.quiz_answer = {}  # dict nel quale si salvano le domande {index_domanda : risposta,...}
        self.i = 0
        self.q_selected_index = self.question_index_list_generated[self.i]
        self.option_selected = IntVar()
        self.header_path = header_path
        self.set_header()
        self.create_structure()
        self.display_info()
        self.display_q()
        self.display_options()
        self.display_image()

    def set_header(self):
        global header_img
        global l1
        header_img = PhotoImage(file=self.header_path)
        l1 = Label(self.tk_object, image=header_img)
        l1.pack()

    def create_structure(self):
        global canvas_info
        global canvas_question
        global canvas_options
        global canvas_image
        global canvas_buttons
        global canvas_footer

        canvas_info = Canvas(self.tk_object, bg=self.background, highlightthickness=0)
        canvas_question = Canvas(self.tk_object, bg=self.background, highlightthickness=0)
        canvas_options = Canvas(self.tk_object, bg=self.background, highlightthickness=0)
        canvas_image = Canvas(self.tk_object, height=250,  bg=self.background, highlightthickness=0)
        canvas_buttons = Canvas(self.tk_object, bg=self.background, highlightthickness=0)
        canvas_footer = Canvas(self.tk_object, bg=self.background, highlightthickness=0)

        canvas_info.pack(fill='x')
        canvas_question.pack(fill='x')
        canvas_options.pack(fill='x')
        canvas_image.pack(fill='x')
        # usare place invece di pack, per non far continuamente muovere il punlsante ad ogni domanda
        canvas_buttons.place(relx=0.5, rely=0.83, anchor=CENTER)
        # canvas_footer.pack()

        def confirm_command():
            # saving the answer
            self.quiz_answer[self.q_selected_index] = self.option_selected.get()

            # go to the next question
            self.get_next_q_index()
            self.create_next_window()

            # restore value of self.option_selected if an answer has been already given, otherwise set it to 0
            if self.q_selected_index in self.quiz_answer.keys():
                self.option_selected.set(self.quiz_answer[self.q_selected_index])
            else:
                self.option_selected.set(0)

        global confirm_button_img
        confirm_button_img = PhotoImage(file='Images/conferma_button.png')
        Button(canvas_buttons, text='next', command=confirm_command, image=confirm_button_img, height=49).pack()

        def back_command():
            self.previous_question()
            self.create_next_window()
            # restore value of self.option_selected = 0, in order to restore the selection in the RadioButtons
            self.option_selected.set(self.quiz_answer[self.q_selected_index])

        global back_button_img
        back_button_img = PhotoImage(file='Images/back_button.png')
        Button(canvas_buttons, text='next', command=back_command, image=back_button_img, height=49).pack(pady=10)

    def get_next_q_index(self):
        if self.q_no < len(self.question_index_list_generated):
            self.q_no += 1
            self.i += 1
            self.q_selected_index = self.question_index_list_generated[self.i]
            return self.q_selected_index
        else:
            self.show_results()

    def previous_question(self):
        if self.q_no > 1:
            self.q_no -= 1
            self.i -= 1
            self.q_selected_index = self.question_index_list_generated[self.i]
        else:
            mb.showwarning("Attenzione", 'Non è possibile tornare indietro')

    def create_next_window(self):
        canvas_info.destroy()
        canvas_question.destroy()
        canvas_options.destroy()
        canvas_image.destroy()
        canvas_buttons.destroy()
        canvas_footer.destroy()

        self.create_structure()
        self.display_info()
        self.display_q()
        self.display_options()
        self.display_image()

    def display_info(self):
        text = f'Domanda N. {self.q_no} di {len(self.question_index_list_generated)} - {base_questions["tema"][self.q_selected_index]}'
        Label(canvas_info, text=text, fg='red', font=("ariel", 15), bg=self.background).pack()

    def display_q(self):
        text = base_questions['domande'][self.q_selected_index]
        Label(canvas_question, text=text, font=('ariel', 18, 'bold'), wraplength=870,
              justify=LEFT, bg=self.background).pack(padx=20, pady=10, anchor='w')

    def display_options(self):
        val = 1
        for option in base_questions['opzioni_risposta'][self.q_selected_index]:
            Radiobutton(canvas_options, text=option, variable=self.option_selected, value=val, font=("ariel", 15),
                        wraplength=850, justify=LEFT, bg=self.background).pack(padx=20, pady=10, anchor='w')
            val += 1

    def display_image(self):
        global q_img

        if base_questions['immagine'][self.q_selected_index] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(base_questions['immagine'][self.q_selected_index]) + '.jpg')
            # resize immagini, in base al loro lato maggiore (larghezza o altezza)
            width = image.size[0]
            height = image.size[1]
            max_size = 230
            if width > height:
                img_proportion = height / width
                width_resized = max_size
                height_resized = int(max_size * img_proportion)
            else:
                img_proportion = width / height
                width_resized = int(max_size * img_proportion)
                height_resized = max_size

            # zoom image in a new window
            def zoom_image(img):
                global zoomed_image
                # resize immagini, in base al loro lato maggiore (larghezza o altezza)
                zoomed_image = img
                # width = zoomed_image.size[0]
                # height = zoomed_image.size[1]
                max_zoom_side = 550
                if width > height:
                    zoom_proportion = height / width
                    width_zoom = max_zoom_side
                    height_zoom = int(max_zoom_side * zoom_proportion)
                else:
                    zoom_proportion = width / height
                    width_zoom = int(max_zoom_side * zoom_proportion)
                    height_zoom = max_zoom_side

                zoomed_image = ImageOps.contain(zoomed_image, (width_zoom, height_zoom))
                zoomed_image = ImageTk.PhotoImage(zoomed_image)

                zoom_win = Toplevel()
                zoom_win.title('Zoom')
                left = (zoom_win.winfo_screenwidth() - width_zoom) / 2
                top = (zoom_win.winfo_screenheight() - height_zoom) / 2
                geometry = '%dx%d+%d+%d' % (width_zoom, height_zoom, left, top - 50)
                zoom_win.geometry(geometry)
                zoom_win.resizable(False, False)
                Label(zoom_win, image=zoomed_image).pack(padx=5, pady=5)

            image_resized = ImageOps.contain(image, (width_resized, height_resized))
            q_img = ImageTk.PhotoImage(image_resized)
            Button(canvas_image, image=q_img, command=(lambda: zoom_image(image)), cursor='fleur').place(relx=0.5, rely=0.5, anchor=CENTER)

        else:
            return None


    def show_results(self):

        #count
        wrong = 0
        correct = 0
        for k, v in self.quiz_answer.items():
            if v == base_questions['risposta_corretta'][k]:
                correct += 1
            else:
                wrong += 1

        score = int(correct / (correct + wrong) * 100)

        if score > 80:
            mb.showinfo("Result", f"Risultati:\nRisposte Corrette: {correct}\nRisposte Sbagliate: {wrong}\n\nComplimenti!\nHai superato la prova\n")
        else:
            mb.showinfo("Result", f"Risultati:\nRisposte Corrette: {correct}\nRisposte Sbagliate: {wrong}\n\nPeccato!\nNon hai superato la prova\n")

        canvas_info.destroy()
        canvas_question.destroy()
        canvas_options.destroy()
        canvas_image.destroy()
        canvas_buttons.destroy()
        canvas_footer.destroy()

        results_page = GuiPage(self.tk_object, 920, 600, 'Risultati', self.background)
        Label(self.tk_object, text='Risultati', font=('ariel', 18, 'bold'), bg=self.background).pack()
        # k = indice domanda
        # v = risposta data 1,2 o 3
        for k, v in self.quiz_answer.items():
            print(k, v)

            # show domanda
            Label(self.tk_object,
                  text=f'\n{base_questions["domande"][k]}',
                  font=('ariel', 15, 'bold'),
                  bg=self.background,
                  wraplength=800,
                  justify=LEFT,
                  anchor='w').pack(fill='x', padx=30)

            if v == 0:
                text_answer = 'Nessuna Risposta'
            else:
                text_answer = base_questions["opzioni_risposta"][k][v-1]

            if (v-1) == base_questions['risposta_corretta'][k]:
                # show risposta data in verde
                Label(self.tk_object,
                      text=text_answer,
                      font=('ariel', 15, ),
                      bg=self.background,
                      fg='green',
                      wraplength=800,
                      justify=LEFT,
                      anchor='w').pack(fill='x', padx=30)
            else:
                # show risposta data in rosso
                Label(self.tk_object,
                      text=text_answer,
                      font=('ariel', 15, ),
                      bg=self.background,
                      fg='red',
                      wraplength=800,
                      justify=LEFT,
                      anchor='w').pack(fill='x', padx=30)

                # show risposta corretta
                Label(self.tk_object,
                      text=base_questions["opzioni_risposta"][k][base_questions["risposta_corretta"][k]-1],
                      fg='green',
                      bg=self.background,
                      font=('ariel', 15),
                      wraplength=800,
                      justify=LEFT,
                      anchor='w').pack(fill='x', padx=30)

        results_page.back_button(lambda: pages_transition(self.tk_object, "choose_modality_base"))
        results_page.show_page()









