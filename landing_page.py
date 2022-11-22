from father_page import GuiPage
from tkinter import *
import page_launcher

#todo impedire resizeble
class LandingPage(GuiPage):
    def __init__(self, tk_object, width, height, title, background):
        super().__init__(tk_object, width, height, title, background)
        self.fill_page()

    def fill_page(self):

        global header_landing
        header_landing = PhotoImage(file='Images/header_landing.png')
        Label(self.tk_object, image=header_landing,highlightthickness=0).pack()


        messaggio_benvenuto = "Benvenuto!\nScegli con quali quiz vuoi esercitarti:"
        Label(self.tk_object, text=messaggio_benvenuto, font=('ariel', 16, 'bold'), bg='#b8e6fe',fg='black', justify='center').pack(padx=50, pady=10, fill='x')

        canvas_buttons = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0)
        canvas_buttons.pack(padx=25, fill='x')
        canvas_buttons.columnconfigure(0, weight=1)
        canvas_buttons.columnconfigure(1, weight=1)
        canvas_buttons.rowconfigure(0, weight=1)

        def button_sx_command():
            page_launcher.pages_transition(self.tk_object, "choose_modality_base")

        global img_base
        img_base = PhotoImage(file='Images/base_1.png')
        button_sx = Button(canvas_buttons, text='Quiz Base', image=img_base, relief=RAISED, command=button_sx_command)
        button_sx.grid(row=0, column=0, sticky='e', padx=20, pady=10)
        # button_sx.pack(side=LEFT, padx=20, pady=10)

        def button_dx_command():
            page_launcher.pages_transition(self.tk_object, "choose_modality_vela")

        global img_vela
        img_vela = PhotoImage(file='Images/vela_1.png')
        button_dx = Button(canvas_buttons, text='Quiz Vela', image=img_vela, relief=RAISED, command=button_dx_command)
        button_dx.grid(row=0, column=1,sticky='w', padx=20, pady=10)

        #button_dx.pack(side=LEFT)

        text_final_label = 'Created by\nLorenzo Tumminello & Andrea Cominotto\nEmail: lorenzotumminello@gmail.com\n\nQuiz ministeriali aggiornati!\nValidi a partire dal 1 Giugno 2022 (DD n.131 del 31/05/2022)'
        Label(text= text_final_label, bg='#b8e6fe', font=("ariel", 10, "italic"), justify=CENTER).pack(fill='x')
