from father_page import GuiPage
from tkinter.ttk import *
from tkinter import *
import page_launcher


class ChooseModalityPage(GuiPage):
    def __init__(self, tk_object, width, height, title, background):
        super().__init__(tk_object, width, height, title, background)
        #self.header_data_obj, self.page_elements = self.get_settings()
        self.fill_page()

    def fill_page(self):

        global header_base_img
        header_base_img = PhotoImage(file= 'Images/header_base_920.png')
        l1 = Label(self.tk_object, image=header_base_img, bg='#b8e6fe')
        l1.grid(row=0,columnspan=4)

        canvas_0 = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_1 = Canvas(self.tk_object, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_2 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_3 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_4 = Canvas(self.tk_object, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')

        canvas_0.grid(row=1,columnspan=4)
        canvas_1.grid(row=2,column=0,padx=10,pady=10)
        canvas_2.grid(row=2,column=1,padx=10,pady=10)
        canvas_3.grid(row=2,column=2,padx=10,pady=10)
        canvas_4.grid(row=2,column=3,padx=10,pady=10)


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


        l1 = Label(canvas_0, text='Scegli una modalità: ', font=('ariel', 20, 'bold'), bg='#b8e6fe')
        l1.pack()

        def pers_button_command():
            page_launcher.pages_transition(self.tk_object, "setup_topic_modality")

        global img_pers_button
        img_pers_button = PhotoImage(file='Images/Images_modalità/topic_1.png')
        pers_button = Button(canvas_1, command=pers_button_command, relief=RAISED, image= img_pers_button, height=img_pers_button.height(), width=img_pers_button.width())
        sub_label_topic_img = PhotoImage(file='Images/Images_modalità/sub_label_topic.png')
        pers_button.pack()

        def ricerca_button_command():
            page_launcher.pages_transition(self.tk_object, "setup_search_modality")

        global ricerca_button_img
        ricerca_button_img = PhotoImage(file='Images/Images_modalità/lente_1.png')
        ricerca_button = Button(canvas_2, command=ricerca_button_command, image=ricerca_button_img, relief=RAISED, height=ricerca_button_img.height(), width=ricerca_button_img.width())
        ricerca_button.pack()


        global fac_simile_button_img
        fac_simile_button_img = PhotoImage(file='Images/Images_modalità/exam_1.png')
        fac_simile_button = Button(canvas_3, image=fac_simile_button_img, relief=RAISED, height=fac_simile_button_img.height(), width=fac_simile_button_img.width())
        fac_simile_button.pack()

        def sbagliati_button_command():
            page_launcher.pages_transition(self.tk_object, "setup_error_modality")

        global sbagliati_button_img
        sbagliati_button_img = PhotoImage(file='Images/Images_modalità/wrong_1.png')
        sbagliati_button = Button(canvas_4, command=sbagliati_button_command, image=sbagliati_button_img, relief=RAISED, height=sbagliati_button_img.height(), width=sbagliati_button_img.width())
        sbagliati_button.pack()

