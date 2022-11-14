from father_page import GuiPage
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox as mb
import json
import page_launcher


# modalità argomento
class SetupModalityPage(GuiPage):
    def __init__(self, tk_object, width, height, title, background,header_path):
        super().__init__(tk_object, width, height, title, background)
        # self.header_data_obj, self.page_elements = self.get_settings()
        self.background = background
        self.header_path = header_path
        self.fill_base_page()

    def fill_base_page(self):
        global header_img
        global canvas_1
        header_img = PhotoImage(file=self.header_path)
        Label(self.tk_object, image=header_img, bg=self.background).pack()
        canvas_1 = Canvas(self.tk_object, bg=self.background, bd=2, highlightthickness=2, relief='ridge')
        canvas_1.pack(padx=50 ,pady=10, fill='x')

    def topic_modality_base(self):

        l1_c1 = Label(canvas_1, text='Seleziona Argomento: ', font=('ariel', 16, 'bold'), bg=self.background)
        l2_c1 = Label(canvas_1, text='Numero Domande : ', font=('ariel', 16, 'bold'), bg=self.background)

        global argomento_selezionato
        argomento_selezionato = StringVar()
        combobox = Combobox(canvas_1, textvariable=argomento_selezionato, width=35)
        combobox['values'] = ['TUTTI', 'TEORIA DELLO SCAFO', 'MOTORI', 'SICUREZZA DELLA NAVIGAZIONE',
                              'MANOVRA E CONDOTTA', 'COLREG E SEGNALAMENTO MARITTIMO', 'METEOROLOGIA',
                              'NAVIGAZIONE CARTOGRAFICA ED ELETTRONICA', 'NORMATIVA DIPORTISTICA E AMBIENTALE']

        # impedisce di scrivere nel menu a tendina
        combobox['state'] = 'readonly'
        # default "tutti"
        combobox.set("TUTTI")
        combobox.bind('<<ComboboxSelected>>', argomento_selezionato.get())

        global numero_domande
        numero_domande = IntVar()
        slider = Scale(canvas_1, from_=1, to=100, orient='horizontal', variable=numero_domande, cursor='boat', width=30,
                       length=300, bg=self.background)
        slider_label = Label(canvas_1, text=' -- da 1 domanda a 100 domande --', font=("ariel", 10, " italic"),
                             bg=self.background)


# todo sistemare il launcher
        def topic_command():
            page_launcher.pages_transition(self.tk_object, "quiz_topic_base", numero_domande=numero_domande.get(), argomento_selezionato=argomento_selezionato.get())

        global img_topic_button
        img_topic_button = PhotoImage(file='Images/personalizzata_button.png')
        b1_c1 = Button(canvas_1, command=topic_command, relief=RAISED, image=img_topic_button, height=img_topic_button.height(), width=img_topic_button.width())

        # place widgets
        canvas_1.grid_columnconfigure((0, 1), weight=2)
        l1_c1.grid(row=0, column=0, pady=20, sticky='e')
        l2_c1.grid(row=1, column=0, pady=10, sticky='e')
        combobox.grid(row=0, column=1, pady=20)
        slider.grid(row=1, column=1)
        slider_label.grid(row=3, column=1, pady=5)
        b1_c1.grid(row=5, columnspan=2, pady=10)

    def search_modality_base(self):
        global entry_base
        label_cerca_base = Label(canvas_1,
                                 text='Ricerca Domande per parole chiave:',
                                 font=('ariel', 16, 'bold'), bg=self.background)

        def on_enter(e):
            entry_base.delete(0, 'end')

        def on_leave(e):
            name = entry_base.get()
            if name == '':
                entry_base.insert(0)


        entry_base = Entry(canvas_1, font=("ariel", 12, " italic"), width=50)

        entry_base.insert(0, 'es. "giardinetto", "sicurezza", "figura", ecc..')
        entry_base.bind('<FocusIn>', on_enter)
        entry_base.bind('<FocusOut>', on_leave)


        global ricerca_button_img
        ricerca_button_img = PhotoImage(file='Images/ricerca_button.png')
        ricerca_button = Button(canvas_1, command=(lambda: page_launcher.pages_transition(self.tk_object, "quiz_search_base", entry_word=entry_base.get())), image=ricerca_button_img, relief=RAISED, height=ricerca_button_img.height(), width=ricerca_button_img.width())


        # Canvas_2 place widgets
        label_cerca_base.pack(pady=10)
        entry_base.pack(pady=10)
        ricerca_button.pack(pady=10)

    def error_modality_base(self):
        col_name = 'domande_salvate_base'
        with open('saved.json', 'r') as file:
                data = json.load(file)
        n_max = len(data[col_name])

        l1_c1 = Label(canvas_1, text='Numero Domande : ', font=('ariel', 16, 'bold'), bg=self.background)
        global numero_domande
        numero_domande = IntVar()
        slider = Scale(canvas_1, from_=1, to=n_max, orient='horizontal', variable=numero_domande, cursor='boat', width=30,
                       length=300, bg=self.background)
        slider_label = Label(canvas_1, text=' -- da 1 domanda a '+ str(n_max) + ' domande --', font=("ariel", 10, " italic"),
                             bg=self.background)

        global sbagliati_button_img
        sbagliati_button_img = PhotoImage(file='Images/sbagliati_button.png')
        sbagliati_button = Button(canvas_1,
                                  command=lambda: page_launcher.pages_transition(self.tk_object, "quiz_error_base", numero_domande=numero_domande.get()),
                                  image=sbagliati_button_img,
                                  relief=RAISED,
                                  height=sbagliati_button_img.height(),
                                  width=sbagliati_button_img.width())

        def cancella_memoria():
            warning = mb.askyesno("Attenzione",
                                  "Attenzione!\nTutti i dati salvati andranno persi.\nSei sicuro di voler continuare?")
            if warning == True:
                with open('saved.json', 'r') as f:
                    data = json.load(f)
                data['domande_salvate_base'] = list()
                print(data)
                with open('saved.json', 'w') as f:
                    json.dump(data, f,indent=2)

                mb.showinfo('formattazione', 'Tutti i dati sono stati cancellati!')

        global img_cestino

        img_cestino = PhotoImage(file='Images/cestino.png')
        cancella_memoria_button = Button(canvas_1, image=img_cestino, command=cancella_memoria)

        l1_c1.pack(pady=10)
        slider.pack(pady=10)
        slider_label.pack(pady=5)
        sbagliati_button.pack(pady=10)
        cancella_memoria_button.place(relx=0.65,rely=0.75)

    def topic_modality_vela(self):

        l1_c1 = Label(canvas_1, text='Seleziona Argomento: ', font=('ariel', 16, 'bold'), bg=self.background)
        l2_c1 = Label(canvas_1, text='Numero Domande : ', font=('ariel', 16, 'bold'), bg=self.background)

        global argomento_selezionato
        argomento_selezionato = StringVar()
        combobox = Combobox(canvas_1, textvariable=argomento_selezionato, width=35)
        combobox['values'] = ['TUTTI', "TEORIA DELLA VELA", "ATTREZZATURA DELLE UNITA' A VELA", "MANOVRE DELLE UNITA' A VELA"]

        # impedisce di scrivere nel menu a tendina
        combobox['state'] = 'readonly'
        # default "tutti"
        combobox.set("TUTTI")
        combobox.bind('<<ComboboxSelected>>', argomento_selezionato.get())

        global numero_domande
        numero_domande = IntVar()
        slider = Scale(canvas_1, from_=1, to=50, orient='horizontal', variable=numero_domande, cursor='boat', width=30,
                       length=300, bg=self.background)
        slider_label = Label(canvas_1, text=' -- da 1 domanda a 50 domande --', font=("ariel", 10, " italic"),
                             bg=self.background)


# todo sistemare il launcher
        def topic_command_vela():
            page_launcher.pages_transition(self.tk_object,
                                           "quiz_topic_vela",
                                           numero_domande=numero_domande.get(),
                                           argomento_selezionato=argomento_selezionato.get())

        global img_topic_button
        img_topic_button = PhotoImage(file='Images/personalizzata_button.png')
        b1_c1 = Button(canvas_1, command=topic_command_vela, relief=RAISED, image=img_topic_button, height=img_topic_button.height(), width=img_topic_button.width())

        # place widgets
        canvas_1.grid_columnconfigure((0, 1), weight=2)
        l1_c1.grid(row=0, column=0, pady=20, sticky='e')
        l2_c1.grid(row=1, column=0, pady=10, sticky='e')
        combobox.grid(row=0, column=1, pady=20)
        slider.grid(row=1, column=1)
        slider_label.grid(row=3, column=1, pady=5)
        b1_c1.grid(row=5, columnspan=2, pady=10)

    def search_modality_vela(self):
        global entry_base
        label_cerca_base = Label(canvas_1,
                                 text='Ricerca Domande per parole chiave:',
                                 font=('ariel', 16, 'bold'), bg=self.background)

        def on_enter(e):
            entry_base.delete(0, 'end')

        def on_leave(e):
            name = entry_base.get()
            if name == '':
                entry_base.insert(0)


        entry_base = Entry(canvas_1, font=("ariel", 12, " italic"), width=50)

        entry_base.insert(0, 'es. "randa", "tangone", ecc..')
        entry_base.bind('<FocusIn>', on_enter)
        entry_base.bind('<FocusOut>', on_leave)


        global ricerca_button_img
        ricerca_button_img = PhotoImage(file='Images/ricerca_button.png')
        ricerca_button = Button(canvas_1, command=(lambda: page_launcher.pages_transition(self.tk_object, "quiz_search_vela", entry_word=entry_base.get())), image=ricerca_button_img, relief=RAISED, height=ricerca_button_img.height(), width=ricerca_button_img.width())


        # Canvas_2 place widgets
        label_cerca_base.pack(pady=10)
        entry_base.pack(pady=10)
        ricerca_button.pack(pady=10)

    def error_modality_vela(self):
        col_name = 'domande_salvate_vela'
        with open('saved.json', 'r') as file:
            data = json.load(file)
        n_max = len(data[col_name])

        l1_c1 = Label(canvas_1, text='Numero Domande : ', font=('ariel', 16, 'bold'), bg=self.background)
        global numero_domande
        numero_domande = IntVar()
        slider = Scale(canvas_1, from_=1, to=n_max, orient='horizontal', variable=numero_domande, cursor='boat',
                       width=30,
                       length=300, bg=self.background)
        slider_label = Label(canvas_1, text=' -- da 1 domanda a ' + str(n_max) + ' domande --',
                             font=("ariel", 10, " italic"),
                             bg=self.background)

        global sbagliati_button_img
        sbagliati_button_img = PhotoImage(file='Images/sbagliati_button.png')
        sbagliati_button = Button(canvas_1,
                                  command=lambda: page_launcher.pages_transition(self.tk_object, "quiz_error_vela",
                                                                                 numero_domande=numero_domande.get()),
                                  image=sbagliati_button_img,
                                  relief=RAISED,
                                  height=sbagliati_button_img.height(),
                                  width=sbagliati_button_img.width())

        def cancella_memoria():
            warning = mb.askyesno("Attenzione",
                                  "Attenzione!\nTutti i dati salvati andranno persi.\nSei sicuro di voler continuare?")
            if warning == True:
                with open('saved.json', 'r') as f:
                    data = json.load(f)
                data['domande_salvate_vela'] = list()
                print(data)
                with open('saved.json', 'w') as f:
                    json.dump(data, f, indent=2)

                mb.showinfo('formattazione', 'Tutti i dati sono stati cancellati!')

        global img_cestino

        img_cestino = PhotoImage(file='Images/cestino.png')
        cancella_memoria_button = Button(canvas_1, image=img_cestino, command=cancella_memoria)

        l1_c1.pack(pady=10)
        slider.pack(pady=10)
        slider_label.pack(pady=5)
        sbagliati_button.pack(pady=10)
        cancella_memoria_button.place(relx=0.65,rely=0.75)
