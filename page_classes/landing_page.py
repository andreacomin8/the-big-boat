from father_page import GuiPage
from tkinter import *
import page_launcher


class LandingPage(GuiPage):
    def __init__(self, tk_object, width, height, title, background):
        super().__init__(tk_object, width, height, title, background)
        self.header_data_obj, self.page_elements = self.get_settings()

    def get_settings(self):
        messaggio_benvenuto = "Benvenuto\\a!\nQui puoi esercitarti con i nuovi quiz ministeriali per il " \
                              "conseguimento\ndella patente nautica.\n\nScegli con quali quiz vuoi esercitarti:"

        label_content = {"label": Label(self.tk_object, text=messaggio_benvenuto, font=('ariel', 16, 'bold'),
                                        bg='#b8e6fe', fg='black', justify='center'),
                         "pack_params": {"padx": 50, "pady": 10, "fill": 'x', "expand": False}}

        canvas_sx = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_dx = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_contents = [{"canvas": canvas_sx, "pack_params": {"padx": 20, "pady": 10, "side": "left"}},
                           {"canvas": canvas_dx, "pack_params": {"padx": 20, "pady": 0, "side": "right"}}]

        def button_sx_command():
            page_launcher.pages_transition(self.tk_object, "setup_quiz_base")

        global img_base
        img_base = PhotoImage(file='Images/base.png')
        button_sx = Button(canvas_sx, text='Quiz Base', image=img_base, font=("ariel", 18, " bold"), compound="top",
                           relief=RAISED, command=button_sx_command, bg='#b8e6fe', fg='green', height=150, width=150)
        button_sx.pack(pady=50, padx=50)

        def button_dx_command():
            page_launcher.pages_transition(self.tk_object, "choose_modality")

        global img_vela
        img_vela = PhotoImage(file='Images/vela.png')

        button_dx = Button(canvas_dx, text='Quiz Vela', image=img_vela, font=("ariel", 18, " bold"), compound="top",
                           relief=RAISED, command=button_dx_command, bg='#b8e6fe', fg='blue', height=150, width=150)

        button_dx.pack(pady=50, padx=50)

        final_label = Label(text='Created by Lorenzo Tumminello\nEmail: lorenzotumminello@gmail.com', bg='#b8e6fe',
                            font=("ariel", 10, "italic"))
        final_label.place(relx=0.37, rely=0.90)

        return label_content, canvas_contents
