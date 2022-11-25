import json
from father_page import GuiPage
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox as mb
import PIL.Image
from PIL import ImageOps, ImageTk
import choose_modality

# todo Se importo pages_transition, non funziona la funzione WTF?


def load_initial_data(base_questions_path, sail_questions_path):
    # read json
    with open(base_questions_path) as f:
        base_df = json.load(f)
    with open(sail_questions_path) as f:
        sail_df = json.load(f)
    return base_df, sail_df
#sail_question: 1-Vero 2-Falso
base_questions, sail_questions = load_initial_data(base_questions_path='base_data.json',
                                                   sail_questions_path='vela_data.json')


def save_wrong_question(modality, wrong_q_index):
    col_name = 'domande_salvate_' + str(modality)

    with open('saved.json', 'r') as file:
        data = json.load(file)

    if wrong_q_index not in data[col_name]:
        data[col_name].append(wrong_q_index)

    with open('saved.json', 'w') as file:
        json.dump(data, file, indent=2)


class QuizPage(GuiPage):
    def __init__(self, tk_object, data, width, height, title, background, question_index_list_generated, header_path):
        super().__init__(tk_object, width, height, title, background, question_index_list_generated)
        self.background = background
        self.data = data

        if self.data == base_questions:
            self.mod = 'base'
        else:
            self.mod = 'vela'

        self.size_q = 18
        self.question_index_list_generated = question_index_list_generated
        self.q_no = 1
        self.quiz_answer = {}  # dict nel quale si salvano le risposte {index_domanda : risposta,...}
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
        global main_frame
        global second_frame
        global canvas_info
        global canvas_question
        global canvas_options
        global canvas_image
        global canvas_buttons
        global canvas_footer

        # Create scrollbar - necessario creare un frame, dentro il quale posizionare i canvas

        # Main Frame
        main_frame = Frame(self.tk_object, bg=self.background)
        main_frame.pack(fill=BOTH, expand=1)

        # Create Canvas
        my_canvas = Canvas(main_frame, bg=self.background)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # create scrollbar
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure canvas

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            my_canvas.yview_scroll(scroll, "units")

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        my_canvas.bind_all("<MouseWheel>", on_mousewheel)

        # second Frame
        second_frame = Frame(my_canvas, bg=self.background)

        # add new frame to a Window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')


        canvas_info = Canvas(second_frame, bg=self.background, highlightthickness=0)
        canvas_question = Canvas(second_frame, bg=self.background, highlightthickness=0)
        canvas_options = Canvas(second_frame, bg=self.background, highlightthickness=0)
        canvas_image = Canvas(second_frame, height=250,  bg=self.background, highlightthickness=0)
        canvas_buttons = Canvas(second_frame, bg=self.background, highlightthickness=0)
        canvas_footer = Canvas(second_frame, bg=self.background, highlightthickness=0)

        canvas_info.pack(fill='x')
        canvas_question.pack(fill='x')
        canvas_options.pack(fill='x')
        canvas_image.pack(fill='x')
        # usare place invece di pack, per non far continuamente muovere il punlsante ad ogni domanda
        canvas_buttons.place(relx=0.5, rely=0.87, anchor=CENTER)
        # canvas_footer.pack()

        def size_font_plus():
            global label_q
            self.size_q += 5
            label_q.configure(font=('ariel', self.size_q, 'bold'))

        def size_font_reduce():
            global label_q
            self.size_q -= 5
            label_q.configure(font=('ariel', self.size_q,'bold'))

        Button(canvas_info, text='size +', command=size_font_plus).pack()
        Button(canvas_info,text='size -', command=size_font_reduce).pack()

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

        if self.data['immagine'][self.q_selected_index] != 0:
            Label(canvas_buttons, text="clicca sulla figura per ingrandirla", bg=self.background,
                  font=('ariel', 13)).pack(pady=10)

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
        main_frame.destroy()
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
        text = f'Domanda N. {self.q_no} di {len(self.question_index_list_generated)} - {self.data["tema"][self.q_selected_index]}'
        Label(canvas_info, text=text, fg='red', font=("ariel", 15), bg=self.background).pack()

    def display_q(self):
        global label_q
        text = self.data['domande'][self.q_selected_index]
        label_q = Label(canvas_question, text=text, font=('ariel', self.size_q, 'bold'), wraplength=870,
              justify=LEFT, bg=self.background)
        label_q.pack(padx=20, pady=10, anchor='w')

    def display_options(self):
        val = 1
        for option in self.data['opzioni_risposta'][self.q_selected_index]:
            Radiobutton(canvas_options, text=option, variable=self.option_selected, value=val, font=("ariel", 15),
                        wraplength=850, justify=LEFT, bg=self.background).pack(padx=20, pady=10, anchor='w')
            val += 1

    def display_image(self):
        global q_img

        if self.data['immagine'][self.q_selected_index] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(self.data['immagine'][self.q_selected_index]) + '.jpg')
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
    # todo far vedere figura nei risultati
        #count
        wrong = 0
        correct = 0
        for k, v in self.quiz_answer.items():
            if v == self.data['risposta_corretta'][k]:
                correct += 1
            else:
                wrong += 1
                save_wrong_question(self.mod, k)

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

        results_page = GuiPage(self.tk_object, 920, 720, 'Risultati', self.background)

        # Create scrollbar - necessario creare un frame, dentro il quale posizionare i canvas

        # Main Frame
        main_frame = Frame(self.tk_object, bg=self.background)
        main_frame.pack(fill=BOTH, expand=1)

        # Create Canvas
        my_canvas = Canvas(main_frame, bg=self.background)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # create scrollbar
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure canvas

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            my_canvas.yview_scroll(scroll, "units")

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        my_canvas.bind_all("<MouseWheel>", on_mousewheel)

        # second Frame
        second_frame = Frame(my_canvas, bg=self.background)

        # add new frame to a Window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')


        Label(second_frame, text='Risultati', font=('ariel', 18, 'bold'), bg=self.background).pack()
        # k = indice domanda
        # v = risposta data 1,2 o 3

        question_number = 1
        #dizionario per tenere in memoria le immagine da stampare nei risultati
        dict_images = {}
        for k, v in self.quiz_answer.items():
            # show domanda
            results_wraplength = 850

            if v == self.data['risposta_corretta'][k]:
                bg = self.background
            else:
                bg = '#ffc2c3'

            Label(second_frame,
                  text=f'\n{question_number} - {self.data["domande"][k]}',
                  font=('ariel', 15, 'bold'),
                  bg=bg,
                  wraplength=750,
                  justify=LEFT,
                  anchor='w').pack(fill='x',padx=10)
            question_number += 1

            # todo aggiungere tasto per vedere immagine
            if self.data['immagine'][k] != 0:
                image = PIL.Image.open('Immagini Pieghevole/Im' + str(self.data['immagine'][k]) + '.jpg')
                # regolazione dimensione
                width = image.size[0]
                height = image.size[1]
                max_size = 200
                if width > height:
                    img_proportion = height / width
                    width_resized = max_size
                    height_resized = int(max_size * img_proportion)
                else:
                     img_proportion = width / height
                     width_resized = int(max_size * img_proportion)
                     height_resized = max_size

                image_resized = ImageOps.contain(image, (width_resized, height_resized))
                dict_images[k] = ImageTk.PhotoImage(image_resized)
                Label(second_frame, image=dict_images[k]).pack(padx=20,pady=5,anchor='w')

            if v == 0:
                text_answer = 'Nessuna Risposta'
            else:

                text_answer = self.data["opzioni_risposta"][k][v-1]


            if v == self.data['risposta_corretta'][k]:
                # show risposta data in verde
                Label(second_frame,
                      text='risposta corretta: ' + text_answer,
                      font=('ariel', 15, ),
                      bg=self.background,
                      fg='green',
                      wraplength=results_wraplength,
                      justify=LEFT,
                      anchor='w').pack(fill='x', padx=10)
            else:
                # show risposta data in rosso
                Label(second_frame,
                      text='risposta errata: ' + text_answer,
                      font=('ariel', 15),
                      bg=self.background,
                      fg='red',
                      wraplength=results_wraplength,
                      justify=LEFT,
                      anchor='w').pack(fill='x', padx=10)

                # show risposta corretta
                Label(second_frame,
                      text=f'risposta corretta: {self.data["opzioni_risposta"][k][self.data["risposta_corretta"][k]-1]}',
                      fg='green',
                      bg=self.background,
                      font=('ariel', 15),
                      wraplength=results_wraplength,
                      justify=LEFT,
                      anchor='w').pack(fill='x', padx=10)

#todo sistemare problema con funzione back, solito problema di importazione circolare
        # sono schifato dal codice qui sotto, però funziona

        def back_result_command(mod):
            if self.tk_object:
                self.tk_object.destroy()
            tk_object = Tk()

            if mod =='base':
            #a = choose_modality.ChooseModalityPageBase(tk_object, 920, 720, "Scegli la modalità", "#b8e6fe", header_path='Images/header_base.png')
                a = choose_modality.ChooseModalityPageBase(tk_object, 920, 720, "Scegli la modalità", background="#b8e6fe", header_path='Images/header_base.png')
            else:
                a = choose_modality.ChooseModalityPageVela(tk_object, 920, 720, "Scegli la modalità", background="#b8e6fe", header_path='Images/header_vela.png')
            a.show_page()

            # def launch_landing_page(tk_object):
            #     tk_object.destroy()
            #     tk_object = Tk()
            #     # retrieve_page_content()
            #     a = landing_page.LandingPage(tk_object, 620, 500, "Quiz Patente Nautica - Menu Iniziale", "#b8e6fe")
            #     a.show_page()

            #a.back_button(lambda: launch_landing_page(tk_object))
            #a.show_page()

        results_page.back_button(lambda: back_result_command(self.mod))
        results_page.show_page()











