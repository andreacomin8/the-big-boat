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

# leggere json
with open('questions_data.json') as f:
    data = json.load(f)

data = pd.DataFrame(data)
question = data['domande']
options = data['opzioni_risposta']
answer = data['risposta_corretta']
figure = data['immagine']
tema = data['tema']

with open('quiz_vela.json') as f:
    data_vela = json.load(f)

# todo rimuovere pandas
data_vela = pd.DataFrame(data_vela)
question_vela = data_vela['Domanda']
answer_vela = data_vela['V_F']
tema_vela = data_vela['Argomento']
sottocategoria_vela = data_vela['sottocategoria']
options_vela = ['Vero', 'Falso']
figure_vela = data_vela['Immagini']


# Menu Iniziale
class LandingPage:
    def __init__(self):
        self.show_menu_iniziale()
    def show_menu_iniziale(self):
        messaggio_benvenuto = "Benvenuto\\a!\nQui puoi esercitarti con i nuovi quiz ministeriali per il conseguimento\ndella patente nautica.\n\nScegli con quali quiz vuoi esercitarti:"
        benvenuto_label = Label(gui_landing_page, text=messaggio_benvenuto,
                                font=('ariel', 16, 'bold'),
                                bg='#b8e6fe', fg='black', justify='center')
        benvenuto_label.pack(pady=10)

        canvas_sx = Canvas(gui_landing_page, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_sx.pack(padx=20, side=LEFT)
        canvas_dx = Canvas(gui_landing_page, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_dx.pack(pady=10, padx=20, side=RIGHT)

        global img_base
        img_base = PhotoImage(file='Images/base.png')
        button_sx = Button(canvas_sx, text='Quiz Base', image=img_base, font=("ariel", 18, " bold"), compound="top",
                           relief=RAISED, command=lanch_menu, bg='#b8e6fe', fg='green', height=150, width=150)
        button_sx.pack(pady=50, padx=50)

        global img_vela
        img_vela = PhotoImage(file='Images/vela.png')

        button_dx = Button(canvas_dx, text='Quiz Vela', image=img_vela, font=("ariel", 18, " bold"), compound="top",
                           relief=RAISED, command=lanch_menu_vela, bg='#b8e6fe', fg='blue', height=150, width=150)

        button_dx.pack(pady=50, padx=50)

        final_label = Label(text='Created by Lorenzo Tumminello\nEmail: lorenzotumminello@gmail.com', bg='#b8e6fe',
                            font=("ariel", 10, "italic"))
        final_label.place(relx=0.37, rely=0.90)


def launch_landing_page():
    global gui_landing_page

    # todo creare metodo che distrugge una finestra e ne lancia una nuova
    try:
        tk_obj.destroy()
    except:
        pass

    try:
        gui_setup_vela.destroy()
    except:
        pass

    finally:
        gui_landing_page = Tk()
        height = 400
        width = 630
        left = (gui_landing_page.winfo_screenwidth() - width) / 2
        top = (gui_landing_page.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top)
        gui_landing_page.geometry(geometry)
        gui_landing_page.resizable(False, False)
        gui_landing_page.title("Quiz Patente Nautica - Menu Iniziale")
        gui_landing_page.configure(background='#b8e6fe')
        LandingPage()
        gui_landing_page.mainloop()


class SetupQuiz:
    def __init__(self, tk_obj, header_label, canvas_list):
        self.tk_obj = tk_obj
        self.header_label = header_label
        self.canvas_list = canvas_list

        self.show_page()
    # canvas_list = [{canvas : {tk_obj, bg:'#b8e6fe', bd:2, highlightthickness:0, relief:'ridge'}}, pack : {padx:50, pady:10, fill:'x', expand:False}}, {}]
    def show_page(self):

        self.header_label.pack(padx=50, pady=10, fill='x', expand=False)

        for canvas_obj in self.canvas_list:
            canvas_obj.canvas.pack(canvas_obj.pack)

            
        ############################################################################################

        # Create Canvas
        canvas_1 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_1.pack(padx=50, pady=10, fill='x', expand=False)

        canvas_2 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_2.pack(padx=50, fill='x', expand=False, pady=10)

        canvas_3 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_3.pack(padx=50, fill='x', expand=False, pady=10)

        canvas_4 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0,)
        canvas_4.pack(padx=50, fill='x', expand=False)

        ############################################################################################
        # canvas_1 Labels
        label_argomento = Label(canvas_1,
                                text='Seleziona Argomento: ',
                                font=('ariel', 16, 'bold'), bg='#b8e6fe')

        label_domande = Label(canvas_1,
                              text='Numero Domande : ',
                              font=('ariel', 16, 'bold'), bg='#b8e6fe')

        # canvas_1 Combobox
        global argomento_selezionato
        argomento_selezionato = StringVar()
        combobox = Combobox(canvas_1, textvariable=argomento_selezionato, width=30, )
        combobox['values'] = ['TUTTI', 'TEORIA DELLO SCAFO', 'MOTORI', 'SICUREZZA DELLA NAVIGAZIONE',
                              'MANOVRA E CONDOTTA', 'COLREG E SEGNALAMENTO MARITTIMO', 'METEOROLOGIA',
                              'NAVIGAZIONE CARTOGRAFICA ED ELETTRONICA', 'NORMATIVA DIPORTISTICA E AMBIENTALE']
        combobox['state'] = 'readonly'  # impedisce di scrivere nel menu a tendina
        combobox.set("TUTTI")

        combobox.bind('<<ComboboxSelected>>', argomento_selezionato.get())

        # canvas_1 slider
        global numero_domande
        numero_domande = IntVar()
        slider = Scale(canvas_1, from_=1, to=100, orient='horizontal', variable=numero_domande, cursor='boat', width=30,
                       length=300, bg='#b8e6fe')
        slider_label = Label(canvas_1, text=' -- da 1 domanda a 100 domande --', font=("ariel", 10, " italic"),
                             bg='#b8e6fe')

        # canvas_1 buttons
        lanch_button = Button(canvas_1, text='Genera Scheda\npersonalizzata', font=("ariel", 16, " bold"),
                              relief=RAISED, command=self.lanch_quiz_personalizzato, bg='#b8e6fe', fg='green', height=4,
                              width=13)

        # Canvas_1 place widgets
        canvas_1.grid_columnconfigure((0, 1), weight=1)

        label_argomento.grid(row=0, column=0, padx=20, pady=20, sticky='e')
        combobox.grid(row=0, column=1, padx=20, pady=20, sticky='w')

        label_domande.grid(row=1, column=0, padx=20, pady=19, sticky='e')
        slider.grid(row=1, column=1, padx=20, pady=5, sticky='w')
        slider_label.grid(row=3, column=1)

        lanch_button.grid(columnspan=2, pady=8)

        #Canvas_2
        global entry_base
        label_cerca_base = Label(canvas_2,
                                 text='Ricerca Domande\nper parole chiave:',
                                 font=('ariel', 16, 'bold'), bg='#b8e6fe')

        def on_enter(e):
            entry_base.delete(0, 'end')

        def on_leave(e):
            name = entry_base.get()
            if name == '':
                entry_base.insert(0)
                # ura\''',\''certificato di sicurezza\'"")

        entry_base = Entry(canvas_2, font=("ariel", 12, " italic"), width=30)

        entry_base.insert(0, 'es. "giardinetto", "sicurezza", "figura", ecc..')
        entry_base.bind('<FocusIn>', on_enter)
        entry_base.bind('<FocusOut>', on_leave)

        base_button_cerca = Button(canvas_2, text='Genera Scheda\ncon ricerca avanzata', font=("ariel", 16, " bold"),
                                   relief=RAISED, command=self.funz_base_button_ricerca, bg='black', fg='blue',
                                   height=4,
                                   width=13)

        # Canvas_2 place widgets
        canvas_2.grid_columnconfigure((0, 1), weight=1)
        label_cerca_base.grid(row=1, column=0, padx=40, pady=10)
        entry_base.grid(row=1, column=1, padx=40, pady=5)
        base_button_cerca.grid(columnspan=2, pady=7)

        # Canvas_3

        # Simuluazione Button
        simulazione_button = Button(canvas_3, text='Genera Scheda\nFAC-SIMILE esame', font=("ariel", 16, " bold"),
                                    relief=RAISED, command=self.lanch_simulazione_esame, bg='#ffc0cb', fg='red',
                                    height=4,
                                    width=13)

        dom_sbagliate_button = Button(canvas_3, text='Quesiti sbagliati\nprecedentemente', font=("ariel", 16, " bold"),
                                      relief=RAISED, command=lanch_quiz_domande_sbagliate, bg='#ffc0cb', fg='#686883',
                                      height=4,
                                      width=13)

        oppure_label = Label(canvas_3, text='Oppure', font=('ariel', 16, 'bold'), bg='#b8e6fe', borderwidth=0)

        canvas_3.grid_rowconfigure(0, weight=1)
        canvas_3.grid_rowconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(0, weight=1)
        canvas_3.grid_columnconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(2, weight=1)

        simulazione_button.grid(row=0, column=2, pady=10)
        oppure_label.grid(row=0, column=1, pady=10)
        dom_sbagliate_button.grid(row=0, column=0, pady=10)

        global img_cestino

        img_cestino = PhotoImage(file='Images/cestino.png')
        cancella_memoria_button = Button(canvas_3, image=img_cestino, command=cancella_memoria)
        cancella_memoria_button.place(x=220, y=30)

        # Canvas_4

        global img_arrow
        img_arrow = PhotoImage(file='Images/return.png')
        return_menu_bottom = Button(canvas_4, text='Menu', font=("ariel", 10, " bold"), image=img_arrow, compound="top",
                                    relief=RAISED, command=launch_landing_page)

        return_menu_bottom.pack()

        final_label = Label(canvas_4, text='Created by Lorenzo Tumminello', bg='#b8e6fe', font=("ariel", 10, "italic"))
        final_label.pack(pady=10)

        ############################################################################################



# Menu Quiz Base
class SetupQuizBase:
    def __init__(self):
        self.show_page()

    def show_page(self):
        # Label

        messaggio_benvenuto = "Quiz Base"
        benvenuto_label = Label(tk_obj, text=messaggio_benvenuto,
                                font=('ariel', 20, 'bold'),
                                bg='#b8e6fe', fg='#778899', justify='center')
        benvenuto_label.pack(padx=50, pady=5)
        # place(relx=0.5, rely=0, anchor=N)

        ############################################################################################

        # Create Canvas
        canvas_1 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_1.pack(padx=50, pady=10, fill='x', expand=False)

        canvas_2 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_2.pack(padx=50, fill='x', expand=False, pady=10)

        canvas_3 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_3.pack(padx=50, fill='x', expand=False, pady=10)

        canvas_4 = Canvas(tk_obj, bg='#b8e6fe', bd=2, highlightthickness=0)
        canvas_4.pack(padx=50, fill='x', expand=False)

        ############################################################################################
        # canvas_1 Labels
        label_argomento = Label(canvas_1,
                                text='Seleziona Argomento: ',
                                font=('ariel', 16, 'bold'), bg='#b8e6fe')

        label_domande = Label(canvas_1,
                              text='Numero Domande : ',
                              font=('ariel', 16, 'bold'), bg='#b8e6fe')

        # canvas_1 Combobox
        global argomento_selezionato
        argomento_selezionato = StringVar()
        combobox = Combobox(canvas_1, textvariable=argomento_selezionato, width=30, )
        combobox['values'] = ['TUTTI', 'TEORIA DELLO SCAFO', 'MOTORI', 'SICUREZZA DELLA NAVIGAZIONE',
                              'MANOVRA E CONDOTTA', 'COLREG E SEGNALAMENTO MARITTIMO', 'METEOROLOGIA',
                              'NAVIGAZIONE CARTOGRAFICA ED ELETTRONICA', 'NORMATIVA DIPORTISTICA E AMBIENTALE']
        combobox['state'] = 'readonly'  # impedisce di scrivere nel menu a tendina
        combobox.set("TUTTI")

        combobox.bind('<<ComboboxSelected>>', argomento_selezionato.get())

        # canvas_1 slider
        global numero_domande
        numero_domande = IntVar()
        slider = Scale(canvas_1, from_=1, to=100, orient='horizontal', variable=numero_domande, cursor='boat', width=30,
                       length=300, bg='#b8e6fe')
        slider_label = Label(canvas_1, text=' -- da 1 domanda a 100 domande --', font=("ariel", 10, " italic"),
                             bg='#b8e6fe')

        # canvas_1 buttons
        lanch_button = Button(canvas_1, text='Genera Scheda\npersonalizzata', font=("ariel", 16, " bold"),
                              relief=RAISED, command=self.lanch_quiz_personalizzato, bg='#b8e6fe', fg='green', height=4,
                              width=13)

        # Canvas_1 place widgets
        canvas_1.grid_columnconfigure((0, 1), weight=1)

        label_argomento.grid(row=0, column=0, padx=20, pady=20, sticky='e')
        combobox.grid(row=0, column=1, padx=20, pady=20, sticky='w')

        label_domande.grid(row=1, column=0, padx=20, pady=19, sticky='e')
        slider.grid(row=1, column=1, padx=20, pady=5, sticky='w')
        slider_label.grid(row=3, column=1)

        lanch_button.grid(columnspan=2, pady=8)

        #Canvas_2
        global entry_base
        label_cerca_base = Label(canvas_2,
                                 text='Ricerca Domande\nper parole chiave:',
                                 font=('ariel', 16, 'bold'), bg='#b8e6fe')

        def on_enter(e):
            entry_base.delete(0, 'end')

        def on_leave(e):
            name = entry_base.get()
            if name == '':
                entry_base.insert(0)
                # ura\''',\''certificato di sicurezza\'"")

        entry_base = Entry(canvas_2, font=("ariel", 12, " italic"), width=30)

        entry_base.insert(0, 'es. "giardinetto", "sicurezza", "figura", ecc..')
        entry_base.bind('<FocusIn>', on_enter)
        entry_base.bind('<FocusOut>', on_leave)

        base_button_cerca = Button(canvas_2, text='Genera Scheda\ncon ricerca avanzata', font=("ariel", 16, " bold"),
                                   relief=RAISED, command=self.funz_base_button_ricerca, bg='black', fg='blue',
                                   height=4,
                                   width=13)

        # Canvas_2 place widgets
        canvas_2.grid_columnconfigure((0, 1), weight=1)
        label_cerca_base.grid(row=1, column=0, padx=40, pady=10)
        entry_base.grid(row=1, column=1, padx=40, pady=5)
        base_button_cerca.grid(columnspan=2, pady=7)

        # Canvas_3

        # Simuluazione Button
        simulazione_button = Button(canvas_3, text='Genera Scheda\nFAC-SIMILE esame', font=("ariel", 16, " bold"),
                                    relief=RAISED, command=self.lanch_simulazione_esame, bg='#ffc0cb', fg='red',
                                    height=4,
                                    width=13)

        dom_sbagliate_button = Button(canvas_3, text='Quesiti sbagliati\nprecedentemente', font=("ariel", 16, " bold"),
                                      relief=RAISED, command=lanch_quiz_domande_sbagliate, bg='#ffc0cb', fg='#686883',
                                      height=4,
                                      width=13)

        oppure_label = Label(canvas_3, text='Oppure', font=('ariel', 16, 'bold'), bg='#b8e6fe', borderwidth=0)

        canvas_3.grid_rowconfigure(0, weight=1)
        canvas_3.grid_rowconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(0, weight=1)
        canvas_3.grid_columnconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(2, weight=1)

        simulazione_button.grid(row=0, column=2, pady=10)
        oppure_label.grid(row=0, column=1, pady=10)
        dom_sbagliate_button.grid(row=0, column=0, pady=10)

        global img_cestino

        img_cestino = PhotoImage(file='Images/cestino.png')
        cancella_memoria_button = Button(canvas_3, image=img_cestino, command=cancella_memoria)
        cancella_memoria_button.place(x=220, y=30)

        # Canvas_4

        global img_arrow
        img_arrow = PhotoImage(file='Images/return.png')
        return_menu_bottom = Button(canvas_4, text='Menu', font=("ariel", 10, " bold"), image=img_arrow, compound="top",
                                    relief=RAISED, command=launch_landing_page)

        return_menu_bottom.pack()

        final_label = Label(canvas_4, text='Created by Lorenzo Tumminello', bg='#b8e6fe', font=("ariel", 10, "italic"))
        final_label.pack(pady=10)

        ############################################################################################
    @staticmethod
    def lanch_quiz_personalizzato():
        tk_obj.destroy()
        lanch_Quiz(numero_domande.get(),
                   # metodo get serva a prendere il valore della variabile numero domande, che altrimenti sarebbe PY_VAR
                   argomento_selezionato.get())

    @staticmethod
    def lanch_simulazione_esame():
        tk_obj.destroy()
        lanch_Scheda()

    @staticmethod
    def funz_base_button_ricerca():
        global index_domande_base
        index_domande_base = []
        text = entry_base.get()
        index = 0
        for domanda in question:
            if text in str(domanda):
                index_domande_base.append(index)
            index += 1
        tk_obj.destroy()
        lanch_base_cerca()

        ############################################################################################


# Menu Quiz Vela
class SetupQuizVela:
    def __init__(self):
        self.show_page()

    def show_page(self):
        # Label

        messaggio_benvenuto = "Quiz Vela"
        benvenuto_label = Label(gui_setup_vela, text=messaggio_benvenuto,
                                font=('ariel', 18, 'bold'),
                                bg='#b8e6fe', fg='#778899', justify='center')
        benvenuto_label.pack(padx=50, pady=10, fill='x', expand=False)

        # Create Canvas
        canvas_1 = Canvas(gui_setup_vela, bg="#ffc0cb", bd=2, highlightthickness=0, relief='ridge')
        canvas_1.pack(pady=10, padx=50, fill='x', expand=False)
        canvas_2 = Canvas(gui_setup_vela, bg="#ffc0cb", bd=2, highlightthickness=0, relief='ridge')
        canvas_2.pack(pady=20, padx=50, fill='x', expand=False)
        canvas_3 = Canvas(gui_setup_vela, bg='#b8e6fe', bd=2, highlightthickness=0)
        canvas_3.pack(padx=50, fill='x', expand=False, )

        # Canvas_1

        # Widget Canvas_1
        label_domande_vela = Label(canvas_1, text='Numero Domande : ', font=('ariel', 16, 'bold'), bg='#ffc0cb')

        # SLIDER - Canvas 1
        global num_dom_vela
        num_dom_vela = IntVar(gui_setup_vela)
        slider_vela = Scale(canvas_1, from_=1, to=50, orient='horizontal', variable=num_dom_vela, cursor='boat',
                            width=30, length=300, bg='#ffc0cb')
        slider_label_vela = Label(canvas_1, text=' -- da 1 domanda a 50 domande --', font=("ariel", 10, " italic"),
                                  bg='#ffc0cb')

        # BUTTON - Canvas 1
        vela_button_1 = Button(canvas_1, text='Genera Scheda\nQuiz Vela', font=("ariel", 16, " bold"),
                               relief=RAISED, command=self.funz_vela_button_1, bg='black', fg='blue', height=4,
                               width=13)

        # PLACE Widgets Canvas 1
        canvas_1.grid_columnconfigure((0, 1), weight=1)
        label_domande_vela.grid(row=1, column=0, padx=20, pady=19, sticky='e')
        slider_vela.grid(row=1, column=1, padx=20, pady=5, sticky='w')
        slider_label_vela.grid(row=3, column=1)
        vela_button_1.grid(columnspan=2, pady=5)

        # Canvas_2

        global entry_vela
        label_domande_vela = Label(canvas_2,
                                   text='Genera scheda\ncon ricerca avanzata',
                                   font=('ariel', 16, 'bold'), bg='#ffc0cb')

        def on_enter(e):
            entry_vela.delete(0, 'end')

        def on_leave(e):
            name = entry_vela.get()
            if name == '':
                entry_vela.insert(0, 'es. "randa", "tangone", ecc..')

        entry_vela = Entry(canvas_2, font=("ariel", 12, " italic"), width=30)
        entry_vela.insert(0, 'es. "randa", "tangone", ecc..')
        entry_vela.bind('<FocusIn>', on_enter)
        entry_vela.bind('<FocusOut>', on_leave)

        vela_button_2 = Button(canvas_2, text='Genera Scheda\ncon ricerca avanzata', font=("ariel", 16, " bold"),
                               relief=RAISED, command=self.funz_vela_button_2, bg='black', fg='green', height=4,
                               width=13)

        # Canvas_2 place widgets
        canvas_2.grid_columnconfigure((0, 1), weight=1)
        label_domande_vela.grid(row=1, column=0, padx=40, pady=19)
        entry_vela.grid(row=1, column=1, padx=40, pady=5)
        vela_button_2.grid(columnspan=2, pady=5)

        # canvas_3 buttons

        global img_arrow
        img_arrow = PhotoImage(file='Images/return.png')
        return_menu_bottom = Button(canvas_3, text='Menu', font=("ariel", 10, " bold"), image=img_arrow, compound="top",
                                    relief=RAISED, command=launch_landing_page)

        return_menu_bottom.pack()
        final_label = Label(canvas_3, text='Created by Lorenzo Tumminello', bg='#b8e6fe', font=("ariel", 10, "italic"))
        final_label.pack(pady=5)

    ############################################################################################
    def funz_vela_button_1(self):
        lanch_quiz_vela(num_dom_vela.get())

    def funz_vela_button_2(self):
        global index_domande
        index_domande = []
        text = entry_vela.get()
        index = 0
        for domanda in question_vela:
            if text in str(domanda):
                index_domande.append(index)
            index += 1
        lanch_quiz_vela_cerca()


class Quiz:
    def __init__(self, n_domande, argomento):
        self.q_no = 0
        self.data_size = n_domande  # numero di domande per scheda
        self.correct = 0
        self.risposte_sbagliate = []
        self.risposte_date = []
        self.argomento = argomento
        if argomento == 'TUTTI':
            self.q_selected = choice(question.index)
        else:
            self.q_selected = choice(data[tema == self.argomento].index)

        self.q_precedent_selected = []
        self.display_title()

        self.display_num_question()

        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.show_image()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)

        if score > 80:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")

        for i in range(len(self.risposte_sbagliate)):
            opzione_corretta = answer[self.risposte_sbagliate[i]]
            risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
            try:
                risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i] - 1]
            except:
                risposta_data = 'nessuna risposta selezionata'
            mb.showinfo("Risposte sbagliate",
                        f"Domanda:\n{question[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}\n\nRisposta data:\n{risposta_data}")

        gui_quiz_base.destroy()
        lanch_menu()

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[self.q_selected]:
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)
            self.risposte_date.append(self.opt_selected.get())

    def next_btn(self, event=None):
        if self.check_ans(self.q_selected):
            self.correct += 1
        self.q_no += 1
        self.q_precedent_selected.append(self.q_selected)
        temp_q_selection = self.q_selected

        while temp_q_selection in self.q_precedent_selected:
            if self.argomento == 'TUTTI':
                temp_q_selection = choice(question.index)
            else:
                temp_q_selection = choice(data[tema == self.argomento].index)
        else:
            self.q_selected = temp_q_selection  # randint(0,len(question)

        if self.q_no == self.data_size:
            salvataggio(self.risposte_sbagliate)
            self.display_result()
        else:

            try:
                canvas.forget()
            except:
                pass

            for btn in q_list:
                btn.forget()

            question_label.destroy()
            num_question.destroy()

            self.display_num_question()
            self.display_question()
            self.opts = self.radio_buttons()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_quiz_base, text="Quiz Patente Nautica!", width=60, bg="blue", fg="white",
                      font=("ariel", 20, "bold"))
        # title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema[self.q_selected]

        num_question = Label(gui_quiz_base, text=f"Domanda {self.q_no + 1} di {self.data_size} - {text_tema}", fg='red',
                             font=("ariel", 15))
        num_question.pack()

    def display_question(self):
        global question_label
        text = question[self.q_selected]
        question_label = Label(gui_quiz_base, text=text, font=('ariel', 18, 'bold'), anchor='w', wraplength=680,
                               justify=LEFT, borderwidth=3)
        # question_label.place(x=30, y=55)
        question_label.pack(fill=BOTH, padx=20, pady=20)
        # question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui_quiz_base.destroy()
        lanch_menu()

    def buttons(self):

        global img_conferma
        global img_back

        img_conferma = PhotoImage(file='Images/conferma_button.png')
        img_back = PhotoImage(file='Images/back_button.png')
        next_button = Button(gui_quiz_base, image=img_conferma, command=self.next_btn, bd=0, highlightthickness=0,
                             borderwidth=0, height=58)
        next_button.place(relx=0.5, y=620, anchor=S)
        gui_quiz_base.bind('<Return>', self.next_btn)
        quit_button = Button(gui_quiz_base, text="Torna al Menu", command=self.quit_button_function,
                             font=("ariel", 10, " bold"), image=img_back, compound="top")
        quit_button.place(x=727, y=0)

    def show_image(self):
        global canvas
        global img
        img = 0
        if figure[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (230, 230))
            canvas = Canvas(gui_quiz_base, width=image.size[0], height=image.size[1])
            img = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=img)
            canvas.pack(fill='y')
        else:
            return None

    def radio_buttons(self):
        global q_list
        q_list = []
        while len(q_list) < 3:
            radio_btn = Radiobutton(gui_quiz_base, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14), anchor='w', wraplength=700, justify=LEFT)
            q_list.append(radio_btn)
            radio_btn.pack(fill=BOTH, anchor='w', pady=10, padx=10)
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(4)
        for option in options[str(self.q_selected)]:
            self.opts[val]['text'] = option
            val += 1


class QuizSchedaEsame:
    def __init__(self, scheda_esame_indici):
        self.q_no = 0
        self.indici_domande = scheda_esame_indici
        self.data_size = len(self.indici_domande)
        self.correct = 0
        self.risposte_sbagliate = []
        self.risposte_date = []
        self.risposte_corrette_categorie = {}
        self.risposte_categorie_totali = {}
        self.q_selected = self.indici_domande[self.q_no]
        self.q_precedent_selected = []
        self.display_title()
        self.display_num_question()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.show_image()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)

        # risposte corrette per categoria
        text_finale = ""
        for i in self.risposte_categorie_totali.keys():
            text = "-{}: {}/{}\n".format(i, self.risposte_corrette_categorie[i], self.risposte_categorie_totali[i])
            text_finale += text

        if score > 80:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")

        gui_quiz_base.destroy()
        new = Tk()
        new.title("Risulati")
        new.resizable(False, False)
        height = 600
        width = 730
        left = (new.winfo_screenwidth() - width) / 2
        top = (new.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        new.geometry(geometry)

        # Per scroolbar

        # Main Frame
        main_frame = Frame(new)
        main_frame.pack(fill=BOTH, expand=1)

        # Create Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # create scrollbar
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure canvas

        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                my_canvas.xview_scroll(scroll, "units")
            else:
                my_canvas.yview_scroll(scroll, "units")

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        my_canvas.bind_all("<MouseWheel>", on_mousewheel)

        # second Frame
        second_frame = Frame(my_canvas)

        # add new frame to a Window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

        # scrittura risultati nel Frame

        Label(second_frame, text="Risultati!", fg='white', bg='blue', width=60, height=0, font=('ariel', 16, 'bold'),
              anchor=CENTER, wraplength=700).pack(fill='x')
        Label(second_frame, text='\nRisposte corrette per ciascuna categoria:\n', width=60, height=0,
              font=('ariel', 12, 'bold'), anchor='w', wraplength=700).pack(fill=BOTH)

        Label(second_frame, text=text_finale, width=60, height=0, font=('ariel', 12, 'bold'), anchor='w',
              wraplength=700, justify=LEFT, borderwidth=3).pack(fill=BOTH)
        Label(second_frame, text='\nQuesiti Sbagliati\n', width=60, height=0, font=('ariel', 12, 'bold'), anchor=CENTER,
              wraplength=700, justify=LEFT, borderwidth=3).pack(fill=BOTH)

        for i in range(len(self.risposte_sbagliate)):
            opzione_corretta = answer[self.risposte_sbagliate[i]]
            risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
            try:
                risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i] - 1]
            except:
                risposta_data = 'Nessuna risposta'
            Label(second_frame, text=str(i + 1) + " - " + question[self.risposte_sbagliate[i]],
                  font=('ariel', 12, 'bold'), anchor='w', wraplength=700, justify=LEFT, borderwidth=3).pack(fill=BOTH)
            Label(second_frame, text="Risposta corretta: " + risposta_corretta, fg='green', font=('ariel', 12),
                  anchor='w', wraplength=700, justify=LEFT, borderwidth=3).pack(fill=BOTH)
            Label(second_frame, text="Risposta data: " + risposta_data, fg='red', font=('ariel', 12), anchor='w',
                  wraplength=700, justify=LEFT, borderwidth=3).pack(fill=BOTH, pady=(0, 10))

        global img_arrow

        def fz_return_button():
            new.destroy()
            lanch_menu()

        img_arrow = PhotoImage(file='Images/return.png')
        return_menu_bottom = Button(new, text='Esci', font=("ariel", 10, " bold"), image=img_arrow, compound="top",
                                    relief=RAISED, command=fz_return_button)
        return_menu_bottom.pack()
        new.mainloop()

    def check_ans(self, q_no):
        if tema[self.q_selected] not in self.risposte_corrette_categorie.keys():
            self.risposte_corrette_categorie[tema[self.q_selected]] = 0
        else:
            pass

        if self.opt_selected.get() == answer[self.q_selected]:
            self.risposte_corrette_categorie[tema[self.q_selected]] += 1
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)
            self.risposte_date.append(self.opt_selected.get())

    def next_btn(self, event=None):
        if self.check_ans(self.q_selected):
            self.correct += 1
        self.q_no += 1

        if self.q_no == self.data_size:
            salvataggio(self.risposte_sbagliate)
            self.display_result()
        else:
            self.q_selected = self.indici_domande[self.q_no]
            try:
                canvas.forget()
            except:
                pass

            for btn in q_list:
                btn.forget()

            question_label.destroy()
            num_question.destroy()
            self.display_num_question()
            self.display_question()
            self.opts = self.radio_buttons()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_quiz_base, text="Quiz Patente Nautica!", width=60, bg="blue", fg="white",
                      font=("ariel", 20, "bold"))
        # title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema

        text_tema = tema[self.q_selected]

        if text_tema not in self.risposte_categorie_totali.keys():
            self.risposte_categorie_totali[text_tema] = 1
        else:
            self.risposte_categorie_totali[text_tema] += 1

        num_question = Label(gui_quiz_base, text=f"Domanda {self.q_no + 1} di {self.data_size} - {text_tema}", fg='red',
                             font=("ariel", 15))
        num_question.pack()

    def display_question(self):
        global question_label
        text = question[self.q_selected]
        question_label = Label(gui_quiz_base, text=text,
                               font=('ariel', 18, 'bold'), anchor='w', wraplength=680, justify=LEFT, borderwidth=3)
        question_label.pack(fill=BOTH, padx=20, pady=20)
        # question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui_quiz_base.destroy()
        lanch_menu()

    def buttons(self):

        global img_conferma
        global img_back

        img_conferma = PhotoImage(file='Images/conferma_button.png')
        img_back = PhotoImage(file='Images/back_button.png')
        next_button = Button(gui_quiz_base, image=img_conferma, command=self.next_btn, bd=0, highlightthickness=0,
                             borderwidth=0, height=58)
        next_button.place(relx=0.5, y=620, anchor=S)
        gui_quiz_base.bind('<Return>', self.next_btn)

        quit_button = Button(gui_quiz_base, text="Torna al Menu", command=self.quit_button_function,
                             font=("ariel", 10, " bold"), image=img_back, compound="top")
        quit_button.place(x=727, y=0)

    def show_image(self):
        global canvas
        global img
        img = 0
        if figure[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (230, 230))
            canvas = Canvas(gui_quiz_base, width=image.size[0], height=image.size[1])
            img = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=img)
            canvas.pack(fill='y')
        else:
            return None

    def radio_buttons(self):
        global q_list
        q_list = []
        while len(q_list) < 3:
            radio_btn = Radiobutton(gui_quiz_base, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14), anchor='w', wraplength=700, justify=LEFT)
            q_list.append(radio_btn)
            # radio_btn.pack(side=TOP,fill='x',anchor=E)
            radio_btn.pack(fill=BOTH, anchor='w', pady=10, padx=10)

        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(4)
        for option in options[str(self.q_selected)]:
            self.opts[val]['text'] = option
            val += 1


# Quiz_base_cerca utilizzato anche per Quiz_domande_sbagliate
class QuizBaseCerca:
    def __init__(self, indice):
        self.q_no = 0
        self.indice = indice
        self.data_size = len(self.indice)  # numero di domande per scheda
        self.correct = 0
        self.risposte_sbagliate = []
        self.risposte_date = []
        self.q_selected = choice(self.indice)
        self.q_precedent_selected = []
        self.display_title()
        self.display_num_question()
        self.display_question()
        self.opt_selected = IntVar(gui_quiz_base)
        self.opts = self.radio_buttons()
        self.display_options()
        self.show_image()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        if score > 80:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")

        for i in range(len(self.risposte_sbagliate)):
            opzione_corretta = answer[self.risposte_sbagliate[i]]
            risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
            try:
                risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i] - 1]
            except:
                risposta_data = 'nessuna risposta selezionata'

            mb.showinfo("Risposte sbagliate",
                        f"Domanda:\n{question[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}\n\nRisposta data:\n{risposta_data}")

        gui_quiz_base.destroy()
        lanch_menu()

    def check_ans(self):
        if self.opt_selected.get() == answer[self.q_selected]:
            elimina_quesito_memory(self.q_selected)
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)
            self.risposte_date.append(self.opt_selected.get())

    def next_btn(self, event=None):
        if self.check_ans():
            self.correct += 1
        self.q_no += 1
        self.q_precedent_selected.append(self.q_selected)

        if self.q_no == self.data_size:
            salvataggio(self.risposte_sbagliate)
            self.display_result()

        else:
            temp_q_selection = self.q_selected
            while temp_q_selection in self.q_precedent_selected:
                temp_q_selection = choice(self.indice)
            else:
                self.q_selected = temp_q_selection

            try:
                canvas.forget()
            except:
                pass

            for btn in q_list:
                btn.forget()
            question_label.destroy()
            num_question.destroy()

            self.display_num_question()
            self.display_question()
            self.opts = self.radio_buttons()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_quiz_base, text="Quiz Patente Nautica!", width=60, bg="blue", fg="white",
                      font=("ariel", 20, "bold"))
        # title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema[self.q_selected]
        num_question = Label(gui_quiz_base, text=f"Domanda {self.q_no + 1} di {self.data_size} - {text_tema}", fg='red',
                             font=("ariel", 15))
        num_question.pack()

    def display_question(self):
        global question_label
        text = question[self.q_selected]
        question_label = Label(gui_quiz_base, text=text,
                               font=('ariel', 18, 'bold'), anchor='w', wraplength=680, justify=LEFT, borderwidth=3)
        # question_label.place(x=30, y=55)
        question_label.pack(fill=BOTH, padx=20, pady=20)
        # question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui_quiz_base.destroy()
        lanch_menu()

    def buttons(self):
        global img_conferma
        global img_back
        img_conferma = PhotoImage(file='Images/conferma_button.png')
        img_back = PhotoImage(file='Images/back_button.png')
        next_button = Button(gui_quiz_base, image=img_conferma, command=self.next_btn, bd=0, highlightthickness=0,
                             borderwidth=0, height=58)
        next_button.place(relx=0.5, y=620, anchor=S)
        gui_quiz_base.bind('<Return>', self.next_btn)
        quit_button = Button(gui_quiz_base, text="Torna al Menu", command=self.quit_button_function,
                             font=("ariel", 10, " bold"), image=img_back, compound="top")
        quit_button.place(x=727, y=0)

    def show_image(self):
        global canvas
        global img
        img = 0
        if figure[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (300, 230))
            canvas = Canvas(gui_quiz_base, width=image.size[0], height=image.size[1])
            img = ImageTk.PhotoImage(image, master=canvas)
            canvas.create_image(0, 0, anchor='nw', image=img)
            # canvas.pack(side=TOP,fill='x',expand=True, anchor=CENTER)
            canvas.pack(fill='y')
            # canvas.place(x=300,y=300)
        else:
            return None

    def radio_buttons(self):
        global q_list
        q_list = []
        # y_pos = 160
        while len(q_list) < 3:
            radio_btn = Radiobutton(gui_quiz_base, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14), anchor='w', wraplength=700, justify=LEFT)
            q_list.append(radio_btn)
            radio_btn.pack(fill=BOTH, anchor='w', pady=10, padx=10)
            # radio_btn.place(x=30, y=y_pos)
            # y_pos += 52
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(4)
        for option in options[str(self.q_selected)]:
            self.opts[val]['text'] = option
            val += 1


def lanch_menu():
    global menu
    global tk_obj
    try:
        gui_landing_page.destroy()
        tk_obj = Tk()
        height = 730
        width = 730
        left = (tk_obj.winfo_screenwidth() - width) / 2
        top = (tk_obj.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        tk_obj.geometry(geometry)
        # gui_menu_base.resizable(False,False)
        tk_obj.title("Quiz Patente Nautica - Menu Quiz Base")
        tk_obj.configure(background='#b8e6fe')
        menu = SetupQuizBase()
        tk_obj.mainloop()
    except:
        tk_obj = Tk()
        height = 730
        width = 730
        left = (tk_obj.winfo_screenwidth() - width) / 2
        top = (tk_obj.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        tk_obj.geometry(geometry)
        # gui_menu_base.resizable(False,False)
        tk_obj.title("Quiz Patente Nautica - Menu Quiz Base")
        tk_obj.configure(background='#b8e6fe')
        menu = SetupQuizBase()
        tk_obj.mainloop()


def lanch_Quiz(num, argo):  # aggiungere tema
    global quiz
    global gui_quiz_base
    gui_quiz_base = Tk()
    height = 630
    width = 810
    left = (gui_quiz_base.winfo_screenwidth() - width) / 2
    top = (gui_quiz_base.winfo_screenheight() - height) / 2
    geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
    gui_quiz_base.geometry(geometry)
    # gui_menu_base.resizable(False,False)
    gui_quiz_base.title("Quiz Patente Nautica")

    quiz = Quiz(num, argo)
    gui_quiz_base.mainloop()


def genera_scheda_esame():
    # Ritorna una lista con gli indici delle domande che compongono il fac-simile della scheda d'esame
    scheda_esame_index = []
    scheda_esame = {'TEORIA DELLO SCAFO': 1, 'MOTORI': 1, 'SICUREZZA DELLA NAVIGAZIONE': 3,
                    'MANOVRA E CONDOTTA': 4, 'COLREG E SEGNALAMENTO MARITTIMO': 2, 'METEOROLOGIA': 2,
                    'NAVIGAZIONE CARTOGRAFICA ED ELETTRONICA': 4, 'NORMATIVA DIPORTISTICA E AMBIENTALE': 3}
    for i in scheda_esame.keys():
        for y in range(scheda_esame[i]):
            scheda_esame_index.append((choice(data[tema == i].index)))
    return scheda_esame_index


def lanch_Scheda():
    global quiz_scheda_esame
    global gui_quiz_base
    gui_quiz_base = Tk()
    height = 630
    width = 810
    left = (gui_quiz_base.winfo_screenwidth() - width) / 2
    top = (gui_quiz_base.winfo_screenheight() - height) / 2
    geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
    gui_quiz_base.geometry(geometry)
    gui_quiz_base.resizable(False, False)
    gui_quiz_base.title("Quiz Patente Nautica")
    quiz_scheda_esame = QuizSchedaEsame(genera_scheda_esame())

    gui_quiz_base.mainloop()


def lanch_quiz_domande_sbagliate():
    global QuizBaseCerca
    global gui_quiz_base

    with open('saved.json', 'r') as file:
        data = json.load(file)
    index_domande_sbagliate = data['domande_salvate']

    if len(index_domande_sbagliate) == 0:
        mb.showwarning('Attenzione', 'Al momento non ci sono domande sbagliate in memoria.')
        pass

    else:
        tk_obj.destroy()
        gui_quiz_base = Tk()
        height = 630
        width = 810
        left = (gui_quiz_base.winfo_screenwidth() - width) / 2
        top = (gui_quiz_base.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        gui_quiz_base.geometry(geometry)
        gui_quiz_base.resizable(False, False)
        gui_quiz_base.title("Quiz Patente Nautica")
        quiz_scheda_esame = QuizBaseCerca(index_domande_sbagliate)
        gui_quiz_base.mainloop()


def lanch_base_cerca():
    global quiz
    global gui_quiz_base
    gui_quiz_base = Tk()
    height = 630
    width = 810
    left = (gui_quiz_base.winfo_screenwidth() - width) / 2
    top = (gui_quiz_base.winfo_screenheight() - height) / 2
    geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
    gui_quiz_base.geometry(geometry)
    gui_quiz_base.resizable(False, False)
    gui_quiz_base.title("Quesiti Vela")
    try:
        quiz = QuizBaseCerca(index_domande_base)
        gui_quiz_base.mainloop()
    except:
        mb.showwarning(title='Attenzione', message="Attenzione!\nParola Non Trovata")
        gui_quiz_base.destroy()
        lanch_menu()


# Funzioni di salvataggio
def salvataggio(lista):
    with open('saved.json', 'r') as file:
        data = json.load(file)
    new = []
    for i in lista:
        if i in data['domande_salvate']:
            pass
        else:
            new.append(i)
    data['domande_salvate'].extend(new)

    with open('saved.json', 'w') as file:
        json.dump(data, file)


def cancella_memoria():
    warning = mb.askyesno("Attenzione",
                          "Attenzione!\nTutti i dati salvati andranno persi.\nSei sicuro di voler continuare?")
    if warning == True:
        with open('saved.json', 'w') as f:
            data = {}
            data['domande_salvate'] = list()
            json.dump(data, f)
        mb.showinfo('formattazione', 'Tutti i dati sono stati cancellati!')

    else:
        pass


def elimina_quesito_memory(index):
    with open('saved.json', 'r') as file:
        data = json.load(file)
    try:
        data['domande_salvate'].remove(index)
        with open('saved.json', 'w') as file:
            json.dump(data, file)
    except:
        pass



class QuizVela:
    def __init__(self, n_domande):
        self.q_no = 0
        self.data_size = n_domande  # numero di domande per scheda
        self.correct = 0
        self.risposte_sbagliate = []
        self.q_selected = choice(question_vela.index)
        self.q_precedent_selected = []
        self.display_title()

        self.display_num_question()
        self.display_question()
        self.show_image()

        self.opt_selected = IntVar(gui_setup_vela)  # 1_Vero, 2_falso
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        if score > 80:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                # opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]]  # [opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate",
                            f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                # opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]]  # [opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate",
                            f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")

        gui_setup_vela.destroy()
        lanch_menu_vela()

    def check_ans(self, q_no):
        if (answer_vela[self.q_selected] == 'V' and self.opt_selected.get() == 1) | (
                answer_vela[self.q_selected] == 'F' and self.opt_selected.get() == 2):
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)

    def next_btn(self):
        if self.check_ans(self.q_selected):
            self.correct += 1
        self.q_no += 1
        self.q_precedent_selected.append(self.q_selected)
        temp_q_selection = self.q_selected

        while temp_q_selection in self.q_precedent_selected:
            temp_q_selection = choice(question_vela.index)
        else:
            self.q_selected = temp_q_selection  # randint(0,len(question)

        if self.q_no == self.data_size:
            self.display_result()
        else:
            question_label.destroy()
            num_question.destroy()

            self.display_num_question()
            self.display_question()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_setup_vela, text="Quiz Vela!", width=60, bg="#ffc0cb", fg="white", font=("ariel", 20, "bold"))
        # title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema_vela[self.q_selected]

        num_question = Label(gui_setup_vela, text=f"Domanda {self.q_no + 1} di {self.data_size} - {text_tema}", fg='red',
                             font=("ariel", 15), )
        num_question.pack()

    def display_question(self):
        global question_label
        text = question_vela[self.q_selected]
        question_label = Label(gui_setup_vela, text=text, width=60, height=0,
                               font=('ariel', 18, 'bold'), anchor='w', wraplength=700, justify=LEFT, borderwidth=3)
        question_label.place(x=30, y=55)
        # question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui_setup_vela.destroy()
        lanch_menu_vela()

    def buttons(self):
        next_button = Button(gui_setup_vela, text="Conferma", command=self.next_btn,
                             width=10, height=3, bg="white", fg="green", font=("ariel", 16, "bold"), relief=RAISED)
        # next_button.pack(expand=True)
        # next_button.pack(side=TOP,expand=True, anchor=N)
        next_button.place(relx=0.5, y=270, anchor=S)

        quit_button = Button(gui_setup_vela, text="Torna al\nMenu", command=self.quit_button_function,
                             width=5, bg="red", fg="red", font=("ariel", 16, " bold"), relief=RAISED)
        quit_button.place(x=720, y=0)

    def radio_buttons(self):
        q_list = []
        x_pos = 320
        while len(q_list) < 2:
            radio_btn = Radiobutton(gui_setup_vela, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 18,), anchor='w', wraplength=700,
                                    justify=LEFT)
            q_list.append(radio_btn)
            # radio_btn.pack(side=TOP,fill='x',anchor=E)
            radio_btn.place(x=x_pos, y=150)
            x_pos += 100
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options_vela:
            self.opts[val]['text'] = option
            val += 1

    def show_image(self):
        global img
        img = 0
        if figure_vela[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure_vela[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (230, 230))
            canvas = Canvas(gui_setup_vela, width=image.size[0] + 10, height=image.size[1] + 10)
            img = ImageTk.PhotoImage(image)
            canvas.create_image(10, 10, anchor=NW, image=img)
            canvas.place(x=300, y=300)

        else:
            return None


class QuizVelaCerca:
    def __init__(self, indice):
        self.q_no = 0
        self.indice = indice
        self.data_size = len(self.indice)
        self.correct = 0
        self.risposte_sbagliate = []
        self.q_selected = choice(self.indice)
        self.q_precedent_selected = []
        self.display_title()

        self.display_num_question()
        self.display_question()
        self.show_image()

        self.opt_selected = IntVar(gui_setup_vela)  # 1_Vero, 2_falso
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        if score > 80:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                # opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]]  # [opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate",
                            f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                # opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]]  # [opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate",
                            f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")
        gui_setup_vela.destroy()
        lanch_menu_vela()

    def check_ans(self, q_no):
        if (answer_vela[self.q_selected] == 'V' and self.opt_selected.get() == 1) | (
                answer_vela[self.q_selected] == 'F' and self.opt_selected.get() == 2):
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)

    def next_btn(self):
        if self.check_ans(self.q_selected):
            self.correct += 1
        self.q_no += 1
        self.q_precedent_selected.append(self.q_selected)

        if self.q_no == self.data_size:
            self.display_result()
        else:
            temp_q_selection = self.q_selected

            while temp_q_selection in self.q_precedent_selected:
                temp_q_selection = choice(self.indice)
            else:
                self.q_selected = temp_q_selection  # randint(0,len(question)

            question_label.destroy()
            num_question.destroy()
            self.display_num_question()
            self.display_question()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_setup_vela, text="Quiz Vela!", width=60, bg="#ffc0cb", fg="white", font=("ariel", 20, "bold"))
        # title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema_vela[self.q_selected]

        num_question = Label(gui_setup_vela, text=f" Trovate {self.data_size} domande! Domanda {self.q_no + 1} - {text_tema}",
                             fg='red', font=("ariel", 17))
        num_question.pack(padx=20)

    def display_question(self):
        global question_label
        text = question_vela[self.q_selected]
        question_label = Label(gui_setup_vela, text=text, width=60, height=0,
                               font=('ariel', 18, 'bold'), anchor='w', wraplength=700, justify=LEFT, borderwidth=3)
        question_label.place(x=40, y=55)
        # question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui_setup_vela.destroy()
        lanch_menu_vela()

    def buttons(self):
        next_button = Button(gui_setup_vela, text="Conferma", command=self.next_btn,
                             width=10, height=3, bg="white", fg="green", font=("ariel", 16, "bold"), relief=RAISED)
        # next_button.pack(expand=True)
        # next_button.pack(side=TOP,expand=True, anchor=N)
        next_button.place(relx=0.5, y=250, anchor=S)

        quit_button = Button(gui_setup_vela, text="Torna al\nMenu", command=self.quit_button_function,
                             width=5, bg="red", fg="red", font=("ariel", 16, " bold"), relief=RAISED)
        quit_button.place(x=720, y=0)

    def radio_buttons(self):
        q_list = []
        x_pos = 0.45
        while len(q_list) < 2:
            radio_btn = Radiobutton(gui_setup_vela, text=" ", variable=self.opt_selected, value=len(q_list) + 1,
                                    font=("ariel", 18,), anchor='w', wraplength=700, justify=LEFT)
            q_list.append(radio_btn)
            # radio_btn.pack(side=TOP,fill='x',anchor=E)
            radio_btn.place(relx=x_pos, y=150, anchor=CENTER)
            x_pos += 0.1
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options_vela:
            self.opts[val]['text'] = option
            val += 1

    def show_image(self):
        global img
        img = 0
        if figure_vela[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure_vela[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (230, 230))
            canvas = Canvas(gui_setup_vela, width=image.size[0] + 10, height=image.size[1] + 10)
            img = ImageTk.PhotoImage(image)
            canvas.create_image(10, 10, anchor=NW, image=img)
            canvas.place(x=300, y=300)

        else:
            return None


def lanch_menu_vela():  # TODO scrivere codice fz lancia menu
    global menu
    global gui_setup_vela
    try:
        gui_landing_page.destroy()
        gui_setup_vela = Tk()
        height = 650
        width = 700
        left = (gui_setup_vela.winfo_screenwidth() - width) / 2
        top = (gui_setup_vela.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        gui_setup_vela.geometry(geometry)
        # menu.resizable(False,False)
        gui_setup_vela.title("Quiz Patente Nautica - Menu Vela")
        gui_setup_vela.configure(background='#b8e6fe')
        menu = SetupQuizVela()
        gui_setup_vela.mainloop()
    except:
        gui_setup_vela = Tk()
        height = 650
        width = 700
        left = (gui_setup_vela.winfo_screenwidth() - width) / 2
        top = (gui_setup_vela.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top)
        gui_setup_vela.geometry(geometry)
        gui_setup_vela.title("Quiz Patente Nautica - Menu Vela")
        gui_setup_vela.configure(background='#b8e6fe')
        menu = SetupQuizVela()
        gui_setup_vela.mainloop()


def lanch_quiz_vela(no_domande):
    global quiz_vela
    global gui_setup_vela
    try:
        gui_setup_vela.destroy()
    finally:
        gui_setup_vela = Tk()
        height = 650
        width = 820
        left = (gui_setup_vela.winfo_screenwidth() - width) / 2
        top = (gui_setup_vela.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        gui_setup_vela.geometry(geometry)
        gui_setup_vela.resizable(False, False)
        gui_setup_vela.title("Quesiti Vela")
        quiz_vela = QuizVela(no_domande)
        gui_setup_vela.mainloop()


def lanch_quiz_vela_cerca():
    global quiz_vela
    global gui_setup_vela
    try:
        gui_setup_vela.destroy()
    finally:
        gui_setup_vela = Tk()
        height = 650
        width = 820
        left = (gui_setup_vela.winfo_screenwidth() - width) / 2
        top = (gui_setup_vela.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        gui_setup_vela.geometry(geometry)
        gui_setup_vela.resizable(False, False)
        gui_setup_vela.title("Quesiti Vela")
    try:
        quiz_vela = QuizVelaCerca(index_domande)
        gui_setup_vela.mainloop()
    except:
        mb.showinfo(title='Attenzione', message="Attenzione!\nParola Non Trovata!")
        gui_setup_vela.destroy()
        lanch_menu_vela()


launch_landing_page()
