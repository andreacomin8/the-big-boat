import json
from father_page import GuiPage
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox as mb
import PIL.Image
from PIL import ImageOps, ImageTk


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
        self.question_index_list_generated = question_index_list_generated
        self.q_no = 1
        self.quiz_answer = {} #dict nel quale si salvano le domande {index_domanda : risposta,...}
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

        canvas_info = Canvas(self.tk_object, bg=self.background,highlightthickness=0)
        canvas_question = Canvas(self.tk_object, bg=self.background,highlightthickness=0)
        canvas_options = Canvas(self.tk_object, bg=self.background, highlightthickness=0)
        canvas_image = Canvas(self.tk_object, height=250,  bg=self.background, highlightthickness=0)
        canvas_buttons = Canvas(self.tk_object, bg=self.background, highlightthickness=0)
        canvas_footer = Canvas(self.tk_object, bg=self.background, highlightthickness=0)

        canvas_info.pack(fill='x')
        canvas_question.pack(fill='x')
        canvas_options.pack(fill='x')
        canvas_image.pack(fill='x')
        # usare place invece di pack, per non far continuamente muovere il punlsante ad ogni domanda
        canvas_buttons.place(relx=0.5,rely=0.83,anchor=CENTER)
        #canvas_footer.pack()

        def confirm_command():
            # saving the answer
            self.quiz_answer[self.q_selected_index] = self.option_selected.get()

            # go to the next question
            self.get_next_q_index()
            self.create_next_window()

            # restore value of self.option_selected if a answer has been already given, otherwise set it to 0
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
            self.check_answer()

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
                  justify=LEFT, bg=self.background).pack(padx=20, pady=10,anchor='w')

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
                proportion = height / width
                width_resized = max_size
                height_resized = int(max_size * proportion)
            else:
                proportion = width / height
                width_resized = int(max_size * proportion)
                height_resized = max_size

            # zoom image in a new window
            def zoom_image(img):
                global zoomed_image
                # resize immagini, in base al loro lato maggiore (larghezza o altezza)
                zoomed_image = img
                width = zoomed_image.size[0]
                height = zoomed_image.size[1]
                if width > height:
                    proportion = height / width
                    width_resized = 500
                    height_resized = int(500 * proportion)
                else:
                    proportion = width / height
                    width_resized = int(500 * proportion)
                    height_resized = 500

                zoomed_image = ImageOps.contain(zoomed_image, (width_resized, height_resized))
                zoomed_image = ImageTk.PhotoImage(zoomed_image)

                zoom_win = Toplevel()
                zoom_win.title('Zoom')
                left = (zoom_win.winfo_screenwidth() - width_resized) / 2
                top = (zoom_win.winfo_screenheight() - height_resized) / 2
                geometry = '%dx%d+%d+%d' % (width_resized, height_resized, left, top - 50)
                zoom_win.geometry(geometry)
                zoom_win.resizable(False,False)
                Label(zoom_win, image=zoomed_image).pack(padx=5,pady=5)


            image_resized = ImageOps.contain(image, (width_resized,height_resized))
            q_img = ImageTk.PhotoImage(image_resized)
            Button(canvas_image, image=q_img, command=(lambda: zoom_image(image)), cursor='fleur').place(relx=0.5, rely=0.5, anchor=CENTER)

        else:
            return None

    def check_answer(self):
        for k, v in self.quiz_answer.items():
            if v == base_questions['risposta_corretta'][k]:
                print(f'CORRETTO: domanda: {k} - risposta data: {v}, risposta corretta : {base_questions["risposta_corretta"][k]}')
            else:
                print(f'SBAGLIATO: domanda: {k} - risposta data: {v}, risposta corretta : {base_questions["risposta_corretta"][k]}')
