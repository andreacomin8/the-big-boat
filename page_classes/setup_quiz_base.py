from father_page import GuiPage
from tkinter.ttk import *
from tkinter import *
import page_launcher


class SetupQuizBasePage(GuiPage):
    def __init__(self, tk_object, width, height, title, background):
        super().__init__(tk_object, width, height, title, background)
        self.header_data_obj, self.page_elements = self.get_settings()

    def get_settings(self):
        global header_base_img
        header_base_img = PhotoImage(file= 'Images/header_base_920.png')

        label_content = {"label": Label(self.tk_object, image=header_base_img, font=('ariel', 20, 'bold'),
                                        bg='#b8e6fe', fg='#778899', justify='center'),
                         "pack_params": {"padx": 50, "pady": 3}}

        canvas_1 = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_2 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_3 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_4 = Canvas(self.tk_object, bg="#b8e6fe", bd=0, highlightthickness=0, relief='ridge')

        canvas_contents = [{"canvas": canvas_1, "pack_params": {"padx": 50, "pady": 5, "fill": "x", "expand": False}},
                           {"canvas": canvas_2, "pack_params": {"padx": 50, "pady": 10, "fill": "x", "expand": False}},
                           {"canvas": canvas_3, "pack_params": {"padx": 50, "pady": 10, "fill": "x", "expand": False}},
                           {"canvas": canvas_4, "pack_params": {"padx": 50, "pady": 10, "fill": "x", "expand": False}}]

        #menubar
        def donothing():
            x=0

        menubar = Menu(self.tk_object)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuovo Quiz", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.tk_object.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        rimuovimenu = Menu(menubar, tearoff=0)
        rimuovimenu.add_command(label="Cancella Dati", command=donothing)
        menubar.add_cascade(label="Rimuovi", menu=rimuovimenu)
        self.tk_object.config(menu=menubar)

        # canvas_1
        l1_c1 = Label(canvas_1, text='Seleziona Argomento: ', font=('ariel', 16, 'bold'), bg='#b8e6fe')
        l2_c1 = Label(canvas_1, text='Numero Domande : ', font=('ariel', 16, 'bold'), bg='#b8e6fe')

        global argomento_selezionato
        argomento_selezionato = StringVar()
        combobox = Combobox(canvas_1, textvariable=argomento_selezionato, width=35)
        combobox['values'] = ['TUTTI', 'TEORIA DELLO SCAFO', 'MOTORI', 'SICUREZZA DELLA NAVIGAZIONE',
                              'MANOVRA E CONDOTTA', 'COLREG E SEGNALAMENTO MARITTIMO', 'METEOROLOGIA',
                              'NAVIGAZIONE CARTOGRAFICA ED ELETTRONICA', 'NORMATIVA DIPORTISTICA E AMBIENTALE']

        combobox['state'] = 'readonly'  # impedisce di scrivere nel menu a tendina
        # default "tutti"
        combobox.set("TUTTI")
        combobox.bind('<<ComboboxSelected>>', argomento_selezionato.get())


        global numero_domande
        numero_domande = IntVar()
        slider = Scale(canvas_1, from_=1, to=100, orient='horizontal', variable=numero_domande, cursor='boat', width=30,
                       length=300, bg='#b8e6fe')
        slider_label = Label(canvas_1, text=' -- da 1 domanda a 100 domande --', font=("ariel", 10, " italic"),
                             bg='#b8e6fe')

        global img_pers_button
        img_pers_button = PhotoImage(file='Images/personalizzata_button.png')

        b1_c1 = Button(canvas_1, relief=RAISED, image= img_pers_button, height=img_pers_button.height(), width=img_pers_button.width())

        # place widgets
        canvas_1.grid_columnconfigure((0,1), weight=2)
        l1_c1.grid(row=0, column=0, pady=20, sticky='e')
        l2_c1.grid(row=1, column=0, pady=10, sticky='e')
        combobox.grid(row=0, column=1, pady=20)
        slider.grid(row=1, column=1)
        slider_label.grid(row=3, column=1, pady=5)
        b1_c1.grid(row=5, columnspan=2, pady=10)

        # Canvas_2
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


        entry_base = Entry(canvas_2, font=("ariel", 12, " italic"), width=30)

        entry_base.insert(0, 'es. "giardinetto", "sicurezza", "figura", ecc..')
        entry_base.bind('<FocusIn>', on_enter)
        entry_base.bind('<FocusOut>', on_leave)

        global ricerca_button_img
        ricerca_button_img = PhotoImage(file='Images/ricerca_button.png')
        ricerca_button = Button(canvas_2, image=ricerca_button_img, relief=RAISED, height=ricerca_button_img.height(), width=ricerca_button_img.width())

        # Canvas_2 place widgets
        canvas_2.grid_columnconfigure((0, 1), weight=1)
        label_cerca_base.grid(row=1, column=0, padx=40, pady=10)
        entry_base.grid(row=1, column=1, padx=40, pady=5)
        ricerca_button.grid(columnspan=2, pady=7)

        # Canvas_3

        # Simuluazione Button

        global fac_simile_button_img
        fac_simile_button_img = PhotoImage(file='Images/fac_simile_button.png')
        fac_simile_button = Button(canvas_3, image=fac_simile_button_img, relief=RAISED, height=fac_simile_button_img.height(), width=fac_simile_button_img.width())


        global sbagliati_button_img
        sbagliati_button_img = PhotoImage(file='Images/sbagliati_button.png')
        sbagliati_button = Button(canvas_3, image=sbagliati_button_img, relief=RAISED, height=sbagliati_button_img.height(), width=sbagliati_button_img.width())



        oppure_label = Label(canvas_3, text='Oppure', font=('ariel', 16, 'bold'), bg='#b8e6fe', borderwidth=0)

        canvas_3.grid_rowconfigure(0, weight=1)
        canvas_3.grid_rowconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(0, weight=1)
        canvas_3.grid_columnconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(2, weight=1)

        fac_simile_button.grid(row=0, column=2, pady=10)
        oppure_label.grid(row=0, column=1, pady=10)
        sbagliati_button.grid(row=0, column=0, pady=10)

        global img_cestino
        img_cestino = PhotoImage(file='Images/cestino.png')
        cancella_memoria_button = Button(canvas_3, image=img_cestino, command=lambda: self.tk_object.quit())
        cancella_memoria_button.place(x=230, y=30)

        # Canvas_4

        global return_img
        return_img = PhotoImage(file='Images/return.png')
        return_menu_bottom = Button(canvas_4, text='Menu', font=("ariel", 10, " bold"), image=return_img, compound="top",
                                    relief=RAISED)

        return_menu_bottom.pack()

        final_label = Label(canvas_4, text='Created by\nLorenzo Tumminello e Andrea Cominotto', bg='#b8e6fe', font=("ariel", 10, "italic"))
        final_label.pack(pady=10)


        return label_content, canvas_contents
