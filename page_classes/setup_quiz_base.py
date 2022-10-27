from father_page import GuiPage
from tkinter.ttk import *
from tkinter import *
import page_launcher


class SetupQuizBasePage(GuiPage):
    def __init__(self, tk_object, width, height, title, background):
        super().__init__(tk_object, width, height, title, background)
        self.header_data_obj, self.page_elements = self.get_settings()

    def get_settings(self):
        messaggio_benvenuto = "Quiz Base"

        label_content = {"label": Label(self.tk_object, text=messaggio_benvenuto, font=('ariel', 20, 'bold'),
                                        bg='#b8e6fe', fg='#778899', justify='center'),
                         "pack_params": {"padx": 50, "pady": 5}}

        canvas_1 = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_2 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_3 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_4 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')

        canvas_contents = [{"canvas": canvas_1, "pack_params": {"padx": 50, "pady": 10, "fill": "x", "expand": False}},
                           {"canvas": canvas_2, "pack_params": {"padx": 50, "pady": 10, "fill": "x", "expand": False}},
                           {"canvas": canvas_3, "pack_params": {"padx": 50, "pady": 10, "fill": "x", "expand": False}},
                           {"canvas": canvas_4, "pack_params": {"padx": 50, "pady": 10, "fill": "x", "expand": False}}]

        # canvas_1 Labels
        Label(canvas_1, text='Seleziona Argomento: ', font=('ariel', 16, 'bold'), bg='#b8e6fe').pack()
        Label(canvas_1, text='Numero Domande : ', font=('ariel', 16, 'bold'), bg='#b8e6fe').pack()

        global argomento_selezionato
        argomento_selezionato = StringVar()
        combobox = Combobox(canvas_1, textvariable=argomento_selezionato, width=30, )
        combobox['values'] = ['TUTTI', 'TEORIA DELLO SCAFO', 'MOTORI', 'SICUREZZA DELLA NAVIGAZIONE',
                              'MANOVRA E CONDOTTA', 'COLREG E SEGNALAMENTO MARITTIMO', 'METEOROLOGIA',
                              'NAVIGAZIONE CARTOGRAFICA ED ELETTRONICA', 'NORMATIVA DIPORTISTICA E AMBIENTALE']
        combobox['state'] = 'readonly'  # impedisce di scrivere nel menu a tendina
        combobox.set("TUTTI")

        combobox.bind('<<ComboboxSelected>>', argomento_selezionato.get())
        combobox.pack()
        return label_content, canvas_contents
