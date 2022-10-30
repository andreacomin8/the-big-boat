#Dicitura per Pyinstaller:
import sys, os
#os.chdir(sys._MEIPASS)

import pandas as pd
import json
from tkinter.ttk import *
from tkinter import *
import PIL.Image
from PIL import ImageTk,ImageOps
from random import choice
from tkinter import messagebox as mb
import mysql.connector

#### Connessione Server
try:
#### Connessione Server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        port='3307',
        database= 'app_patente_nautica'
    )
    print('Connessione al server avvenuta con successo!')
except:
    mb.showerror('Connessione','Connessione al Server Fallita!\nImpossibile procedere\nVerifica la tua connessione internet')

class Login:
    def __init__(self):
        self.show_login()
    def show_login(self):
        root = Tk()
        root.title("Login Quiz Patente Nautica")
        root.config(bg='#b8e6fe')
        height = 400
        width = 900
        left = (root.winfo_screenwidth() - width) / 2
        top = (root.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top)
        root.geometry(geometry)
        root.resizable(False, False)

        def signin():
            username = user.get()
            password = code.get()
            selected_query = 'SELECT * FROM `credenziali` WHERE `username` = %s AND `password` = %s'
            vals = (username,password)
            c = connection.cursor()
            c.execute(selected_query,vals)
            utente = c.fetchone()
            if utente is not None:
                root.destroy()
                lanch_menu_iniziale()
            else:
                mb.showerror('Invalid','Password Sbagliata')


        Label(root, text='Quiz Patente Nautica', fg='#57a1f8', bg='#b8e6fe', font=('Microsoft Yahei UI Light',25,'bold')).place(relx=0.4,y=6)
        img = PhotoImage(file='Images/login_2.png')
        Label(root,image=img,bg='#b8e6fe').place(x=50,y=40)

        frame= Frame(root,width=350,height=350,bg='#b8e6fe')
        frame.place(x=480,y=50)

        heading = Label(frame, text='Login', fg='#57a1f8', bg='#b8e6fe', font=('Microsoft Yahei UI Light',23,'bold'))
        heading.place(x=130,y=15)

### ---------------------------------------------------------------------------------------------------
        def on_enter(e):
            user.delete(0,'end')
        def on_leave(e):
            name = user.get()
            if name =='':
                user.insert(0,'Username')

        user = Entry(frame, width=35,fg='black',border=0,bg='white',font=('ariel',11))
        user.place(x=30,y=80)
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
### ---------------------------------------------------------------------------------------------------
        def on_enter(e):
            code.delete(0,'end')
        def on_leave(e):
            name = code.get()
            if name =='':
                code.insert(0,'Password')

        code = Entry(frame, show='*', width=35, fg='black', border=0, bg='white', font=('ariel', 11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#################################################################################

        Button(frame,width=30,pady=7,text='Sign in',bg='#b8e6fe', fg='black',border=0,command=signin).place(x=35,y=204)

        def lanch_signup():
            root.destroy()
            Signup()

        signup_label = Label(frame, text='Non hai un account?', bg='#b8e6fe', font=("ariel", 12, "italic"))
        signup_label.place(relx=0.35, rely=0.73)
        Button(frame, text= 'Clicca qui per crearne uno',bg='#4658fc', fg='#4658fc',font=("ariel", 12) ,command=lanch_signup).place(relx=0.25, rely=0.80)

        final_label = Label(frame, text='Created by Lorenzo Tumminello\nEmail: lorenzotumminello@gmail.com', bg='#b8e6fe', font=("ariel", 10, "italic"))
        final_label.place(relx=0.25, rely=0.90)


        root.mainloop()
class Signup:
    def __init__(self):
        self.show_signup()

    def show_signup(self):
        root = Tk()
        root.title("Signup Quiz Patente Nautica")
        root.config(bg='#c6e9c4')
        height = 400
        width = 900
        left = (root.winfo_screenwidth() - width) / 2
        top = (root.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top)
        root.geometry(geometry)
        root.resizable(False, False)


        def match_password():
            password_1 = code.get()
            password_2 = code_2.get()
            if password_1 != password_2:
                mb.showerror('Attenzione!', 'Le password non corrispondo')
            else:
                create_new_account()


        def create_new_account():
            new_username = user.get()
            new_password = code.get()
            insert_user_query = "INSERT INTO `credenziali` (`username`, `password`, `reg_date`, `exp_date`,`status`) VALUES (%s, %s, current_timestamp(), (current_timestamp() + interval 1 month),'1')"
            new_vals = (new_username, new_password)
            c = connection.cursor()
            c.execute(insert_user_query, new_vals)
            connection.commit()
            mb.showinfo('Complimenti!', 'Account creato con successo!')
            root.destroy()
            Login()


        Label(root, text='Registrazione', fg='#4658fc', bg='#c6e9c4',
              font=('Microsoft Yahei UI Light', 25, 'bold')).place(
            relx=0.4, y=6)
        img = PhotoImage(file='Images/registration.png')
        Label(root, image=img, bg='#c6e9c4').place(x=50, y=40)

        frame = Frame(root, width=350, height=350, bg='#c6e9c4')
        frame.place(x=500, y=50)

        heading = Label(frame, text='Nuove credenziali', fg='#4658fc', bg='#c6e9c4',
                        font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=80, y=15)

        ### ---------------------------------------------------------------------------------------------------
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Username')

        user = Entry(frame, width=35, fg='black', border=0, bg='white', font=('ariel', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        ### ---------------------------------------------------------------------------------------------------
        def on_enter(e):
            code.delete(0, 'end')

        def on_leave(e):
            name = code.get()
            if name == '':
                code.insert(0, 'Password')

        code = Entry(frame, width=35, fg='black', border=0, bg='white', font=('ariel', 11))

        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        def on_enter_2(e):
            code_2.delete(0, 'end')

        def on_leave_2(e):
            name = code_2.get()
            if name == '':
                code_2.insert(0, 'Ripeti Password')

        code_2 = Entry(frame, width=35, fg='black', border=0, bg='white', font=('ariel', 11))

        code_2.place(x=30, y=220)
        code_2.insert(0, 'Ripeti Password')
        code_2.bind('<FocusIn>', on_enter_2)
        code_2.bind('<FocusOut>', on_leave_2)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        #################################################################################

        Button(frame, width=30, pady=7, text='Registrati', bg='#c6e9c4', fg='black', border=0,
               command= match_password).place(x=35, y=267)
        # final_label = Label(frame, text='Created by Lorenzo Tumminello\nEmail: lorenzotumminello@gmail.com', bg='#b8e6fe', font=("ariel", 10, "italic"))
        # final_label.place(relx=0.25, rely=0.90)
        root.mainloop()

### leggere json
with open('page_classes/data/base_data.json') as f:
    data = json.load(f)

data = pd.DataFrame(data)
question = data['domande']
options = data['opzioni_risposta']
answer = data['risposta_corretta']
figure = data['immagine']
tema = data['tema']

with open('page_classes/data/vela_data.json') as f:
    data_vela = json.load(f)

data_vela = pd.DataFrame(data_vela) #todo rimuovere pandas
question_vela = data_vela['Domanda']
answer_vela = data_vela['V_F']
tema_vela = data_vela['Argomento']
sottocategoria_vela = data_vela['sottocategoria']
options_vela = ['Vero','Falso']
figure_vela = data_vela['Immagini']

## Menu Iniziale ##
class Menu_iniziale:
    def __init__(self):
        self.show_menu_iniziale()
    def show_menu_iniziale(self):
        messaggio_benvenuto = "Benvenuto\\a!\nQui puoi esercitarti con i nuovi quiz ministeriali per il conseguimento\ndella patente nautica.\n\nScegli con quali quiz vuoi esercitarti:"
        benvenuto_label = Label(gui_menu_1, text=messaggio_benvenuto,
                                font=('ariel', 16, 'bold'),
                                bg='#b8e6fe', fg='black', justify='center')
        benvenuto_label.pack(pady=10)

        canvas_sx = Canvas(gui_menu_1, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_sx.pack(padx=20,side=LEFT)
        canvas_dx = Canvas(gui_menu_1, bg="#b8e6fe", bd=2, highlightthickness=0, relief='ridge')
        canvas_dx.pack(pady=10,padx=20,side=RIGHT)

        global img_base
        img_base = PhotoImage(file ='Images/base.png')
        button_sx = Button(canvas_sx, text='Quiz Base', image=img_base, font=("ariel", 18, " bold"), compound="top",
                                      relief=RAISED, command=lanch_menu, bg='#b8e6fe', fg='green',height=150,width=150)
        button_sx.pack(pady=50,padx=50)


        global img_vela
        img_vela = PhotoImage(file ='Images/vela.png')

        button_dx = Button(canvas_dx, text='Quiz Vela', image=img_vela, font=("ariel", 18, " bold"),compound="top",
                                      relief=RAISED, command=lanch_menu_vela, bg='#b8e6fe', fg='blue',height=150,width=150)

        button_dx.pack(pady=50,padx=50)

        final_label = Label(text='Created by Lorenzo Tumminello\nEmail: lorenzotumminello@gmail.com', bg='#b8e6fe', font=("ariel", 10, "italic"))
        final_label.place(relx=0.37 , rely=0.90)
def lanch_menu_iniziale():
    global menu_iniziale
    global gui_menu_1
    try:
        gui_menu_base.destroy()
    except:
        pass
    try:
        gui.destroy()
    except:
        pass

    finally:
        gui_menu_1 = Tk()
        height = 400
        width = 630
        left = (gui_menu_1.winfo_screenwidth() - width) / 2
        top = (gui_menu_1.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top)
        gui_menu_1.geometry(geometry)
        gui_menu_1.resizable(False,False)
        gui_menu_1.title("Quiz Patente Nautica - Menu Iniziale")
        gui_menu_1.configure(background='#b8e6fe')
        menu_iniziale = Menu_iniziale()
        gui_menu_1.mainloop()

## Menu Quiz Base ##
class Menu: #TODO scrivere codice classe
    def __init__(self):
        self.show_menu()
    def show_menu(self):
        ## Label

        messaggio_benvenuto = "Quiz Base"
        benvenuto_label = Label(gui_menu_base, text=messaggio_benvenuto,
                                font=('ariel', 20, 'bold'),
                                bg='#b8e6fe', fg='#778899', justify='center')
        benvenuto_label.pack(padx=50, pady=5)
        # place(relx=0.5, rely=0, anchor=N)


        ############################################################################################

        # Create Canvas
        canvas_1 = Canvas(gui_menu_base, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_1.pack(padx=50,pady=10,fill='x', expand=False)

        canvas_2 = Canvas(gui_menu_base, bg='#b8e6fe', bd=2, highlightthickness=0, relief='ridge')
        canvas_2.pack(padx=50, fill='x', expand=False,pady=10)

        canvas_3 = Canvas(gui_menu_base, bg='#b8e6fe', bd=2, highlightthickness=0,relief='ridge')
        canvas_3.pack(padx=50, fill='x', expand=False,pady=10)

        canvas_4 = Canvas(gui_menu_base, bg='#b8e6fe', bd=2, highlightthickness=0)
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


        ################# Canvas_2

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
                #ura\''',\''certificato di sicurezza\'"")

        entry_base = Entry(canvas_2, font=("ariel", 12, " italic"), width=30)

        entry_base.insert(0, 'es. "giardinetto", "sicurezza", "figura", ecc..')
        entry_base.bind('<FocusIn>', on_enter)
        entry_base.bind('<FocusOut>', on_leave)

        base_button_cerca = Button(canvas_2, text='Genera Scheda\ncon ricerca avanzata', font=("ariel", 16, " bold"),
                                   relief=RAISED, command=self.funz_base_button_ricerca, bg='black', fg='blue', height=4,
                                   width=13)

        # Canvas_2 place widgets
        canvas_2.grid_columnconfigure((0, 1), weight=1)
        label_cerca_base.grid(row=1, column=0, padx=40, pady=10)
        entry_base.grid(row=1, column=1, padx=40, pady=5)
        base_button_cerca.grid(columnspan=2, pady=7)


        ################# Canvas_3

        # Simuluazione Button
        simulazione_button = Button(canvas_3, text='Genera Scheda\nFAC-SIMILE esame', font=("ariel", 16, " bold"),
                                    relief=RAISED, command=self.lanch_simulazione_esame, bg='#ffc0cb', fg='red', height=4,
                                    width=13)

        dom_sbagliate_button = Button(canvas_3, text='Quesiti sbagliati\nprecedentemente', font=("ariel", 16, " bold"),
                                    relief=RAISED, command= lanch_quiz_domande_sbagliate, bg='#ffc0cb', fg='#686883',
                                    height=4,
                                    width=13)

        oppure_label = Label(canvas_3, text='Oppure', font=('ariel', 16, 'bold'), bg='#b8e6fe', borderwidth=0)

        canvas_3.grid_rowconfigure(0, weight=1)
        canvas_3.grid_rowconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(0, weight=1)
        canvas_3.grid_columnconfigure(1, weight=1)
        canvas_3.grid_columnconfigure(2, weight=1)

        simulazione_button.grid(row=0, column=2, pady=10)
        oppure_label.grid(row=0, column=1,pady=10)
        dom_sbagliate_button.grid(row=0, column=0,pady=10)

        global img_cestino

        img_cestino = PhotoImage(file='Images/cestino.png')
        cancella_memoria_button = Button(canvas_3, image=img_cestino,command=cancella_memoria)
        cancella_memoria_button.place(x=220,y=30)


################# Canvas_4

        global img_arrow
        img_arrow=PhotoImage(file='Images/return.png')
        return_menu_bottom = Button(canvas_4, text='Menu',font=("ariel", 10, " bold"), image=img_arrow, compound="top",
                              relief=RAISED, command=lanch_menu_iniziale)

        return_menu_bottom.pack()

        final_label = Label(canvas_4, text='Created by Lorenzo Tumminello', bg='#b8e6fe', font=("ariel", 10, "italic"))
        final_label.pack(pady=10)

        ############################################################################################
    def lanch_quiz_personalizzato(self):
        gui_menu_base.destroy()
        lanch_Quiz(numero_domande.get(),
                   argomento_selezionato.get())  # metodo get serva a prendere il valore della variabile numero domande, che altrimenti sarebbe PY_VAR
    def lanch_simulazione_esame(self):
        gui_menu_base.destroy()
        lanch_Scheda()
    def lanch_quiz_domande_sbagliate(self):
        gui_menu_base.destroy()
        Quiz_domande_sbagliate() #TODO creare GUI
    def funz_base_button_ricerca(self):
        global index_domande_base
        index_domande_base = []
        text = entry_base.get()
        index = 0
        for domanda in question:
            if text in str(domanda):
                index_domande_base.append(index)
            index += 1
        gui_menu_base.destroy()
        lanch_base_cerca()

        ############################################################################################
class Quiz:
    def __init__(self,n_domande,argomento):
        self.q_no= 0
        self.data_size = n_domande #numero di domande per scheda
        self.correct = 0
        self.risposte_sbagliate = []
        self.risposte_date=[]
        self.argomento = argomento
        if argomento == 'TUTTI':
            self.q_selected = choice(question.index)
        else:
            self.q_selected = choice(data[tema == self.argomento].index)

        self.q_precedent_selected = []
        self.display_title()

        self.display_num_question()

        self.display_question()
        self.show_image()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)

        if score > 80 :
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
                risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i] - 1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question[self.risposte_sbagliate[i]]}\n\nRisposta data:\n{risposta_data}\n\nRisposta corretta:\n{risposta_corretta}")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
                risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i] - 1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question[self.risposte_sbagliate[i]]}\n\nRisposta data:\n{risposta_data}\n\nRisposta corretta:\n{risposta_corretta}")
        gui_quiz_base.destroy()
        lanch_menu()

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[self.q_selected]:
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)
            self.risposte_date.append(self.opt_selected.get())

    def next_btn(self):
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
            self.q_selected = temp_q_selection #randint(0,len(question)


        if self.q_no == self.data_size:
            salvataggio(self.risposte_sbagliate)
            self.display_result()
        else:
            question_label.destroy()
            num_question.destroy()

            self.display_num_question()
            self.display_question()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_quiz_base, text="Quiz Patente Nautica!", width=60, bg="blue", fg="white", font=("ariel", 20, "bold"))
        #title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema[self.q_selected]

        num_question = Label(gui_quiz_base, text=f"Domanda {self.q_no+1} di {self.data_size} - {text_tema}",fg='red', font=("ariel", 15 ))
        num_question.pack()

    def display_question(self):
        global question_label
        text = question[self.q_selected]
        question_label = Label(gui_quiz_base, text=text, width=60, height=0,
                     font=('ariel', 18, 'bold'), anchor='w',wraplength=680,justify=LEFT,borderwidth=3)
        #question_label.place(x=30, y=55)
        question_label.pack(padx=20,pady=20)
        #question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui_quiz_base.destroy()
        lanch_menu()

    def buttons(self):
        next_button = Button(gui_quiz_base, text="Conferma", command = self.next_btn,
                             width=10, height=3, bg="white", fg="green", font=("ariel", 16, "bold"), relief=RAISED)
        #next_button.pack(expand=True)
        #next_button.pack(side=TOP,expand=True, anchor=N)
        next_button.place(relx= 0.5, y=620,anchor=S)

        quit_button = Button(gui_quiz_base, text="Torna al \nMenu", command=self.quit_button_function,
                             width=5, bg="red", fg="red", font=("ariel", 16, " bold"), relief=RAISED)
        quit_button.place(x=720 ,y=0)

    def show_image(self):
        global img
        img = 0
        if figure[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (230, 230))
            canvas = Canvas(gui_quiz_base, width=image.size[0]+10, height=image.size[1]+10)
            img = ImageTk.PhotoImage(image)
            canvas.create_image(10,10, anchor=NW, image=img)
            #canvas.pack(side=TOP,fill='x',expand=True, anchor=CENTER)
            canvas.place(x=200,y=300)
        else:
            return None

    def radio_buttons(self):
        q_list = []
        y_pos = 160
        while len(q_list) < 3:
            radio_btn = Radiobutton(gui_quiz_base, text=" ", variable=self.opt_selected,
                                    value= len(q_list) + 1, font=("ariel", 14),anchor='w',wraplength=700,justify=LEFT)
            q_list.append(radio_btn)
            radio_btn.place(x=30, y=y_pos)
            y_pos += 50
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[str(self.q_selected)]:
            self.opts[val]['text'] = option
            val += 1
class Quiz_scheda_esame:
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
        self.show_image()

        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)

## CREA TESTO PER CATEGORIE
        text_finale=""
        for i in self.risposte_categorie_totali.keys():
            text= "{}: {}/{}\n".format(i, self.risposte_corrette_categorie[i],self.risposte_categorie_totali[i])
            text_finale += text

        if score > 80:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")

        mb.showinfo("Percentuali Categoria", text_finale)
        for i in range(len(self.risposte_sbagliate)):
            opzione_corretta = answer[self.risposte_sbagliate[i]]
            risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
            risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i]-1]
            mb.showinfo("Risposte sbagliate", f"Domanda:\n{question[self.risposte_sbagliate[i]]}\n\nRisposta data:\n{risposta_data}\n\nRisposta corretta:\n{risposta_corretta}")

        gui_quiz_base.destroy()
        lanch_menu()


    def check_ans(self, q_no):
        if tema[self.q_selected] not in self.risposte_corrette_categorie.keys():
            self.risposte_corrette_categorie[tema[self.q_selected]] =  0
            self.risposte_categorie_totali[tema[self.q_selected]] =  0
        else:
            pass

        if self.opt_selected.get() == answer[self.q_selected]:
            self.risposte_corrette_categorie[tema[self.q_selected]] += 1
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)
            self.risposte_date.append(self.opt_selected.get())

        self.risposte_categorie_totali[tema[self.q_selected]] += 1


    def next_btn(self):
        if self.check_ans(self.q_selected):
            self.correct += 1
        self.q_no += 1

        if self.q_no == self.data_size:
            salvataggio(self.risposte_sbagliate)
            self.display_result()
        else:
            self.q_selected = self.indici_domande[self.q_no]
            question_label.destroy()
            num_question.destroy()
            self.display_num_question()
            self.display_question()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_quiz_base, text="Quiz Patente Nautica!", width=60, bg="blue", fg="white", font=("ariel", 20, "bold"))
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
        question_label = Label(gui_quiz_base, text=text, width=60, height=0,
                               font=('ariel', 18, 'bold'), anchor='w', wraplength=700, justify=LEFT, borderwidth=3)
        question_label.place(x=30, y=55)
        # question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui_quiz_base.destroy()
        lanch_menu()

    def buttons(self):
        next_button = Button(gui_quiz_base, text="Conferma", command=self.next_btn,
                             width=10, height=3, bg="white", fg="green", font=("ariel", 16, "bold"), relief=RAISED)
        # next_button.pack(expand=True)
        # next_button.pack(side=TOP,expand=True, anchor=N)
        next_button.place(relx= 0.5, y=620,anchor=S)

        quit_button = Button(gui_quiz_base, text="Torna al\nMenu", command=self.quit_button_function,
                             width=5, bg="red", fg="red", font=("ariel", 16, " bold"), relief=RAISED)
        quit_button.place(x=720, y=0)

    def show_image(self):
        global img
        img = 0
        if figure[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (230, 230))
            canvas = Canvas(gui_quiz_base, width=image.size[0]+10, height=image.size[1]+10)
            img = ImageTk.PhotoImage(image)
            canvas.create_image(10, 10, anchor=NW, image=img)

            canvas.place(x=200, y=300)
        else:
            return None

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 3:
            radio_btn = Radiobutton(gui_quiz_base, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14), anchor='w', wraplength=700, justify=LEFT)
            q_list.append(radio_btn)
            # radio_btn.pack(side=TOP,fill='x',anchor=E)
            radio_btn.place(x=30, y=y_pos)
            y_pos += 50
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[str(self.q_selected)]:
            self.opts[val]['text'] = option
            val += 1
## Quiz_base_cerca richiede che gli sia passato una lista di indici domande, quindi funz anche per le domande sbagliate
class Quiz_base_cerca:
    def __init__(self,indice):
        self.q_no= 0
        self.indice = indice
        self.data_size = len(self.indice) #numero di domande per scheda
        self.correct = 0
        self.risposte_sbagliate = []
        self.risposte_date=[]
        self.q_selected = choice(self.indice)
        self.q_precedent_selected = []
        self.display_title()

        self.display_num_question()

        self.display_question()
        self.show_image()
        self.opt_selected = IntVar(gui_quiz_base)
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        if score > 80 :
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
                risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i]-1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question[self.risposte_sbagliate[i]]}\n\nRisposta data:\n{risposta_data}\n\nRisposta corretta:\n{risposta_corretta}")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = options[self.risposte_sbagliate[i]][opzione_corretta - 1]
                risposta_data = options[self.risposte_sbagliate[i]][self.risposte_date[i]-1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question[self.risposte_sbagliate[i]]}\n\nRisposta data:\n{risposta_data}\n\nRisposta corretta:\n{risposta_corretta}")

        gui_quiz_base.destroy()
        lanch_menu()
    def check_ans(self):
        if self.opt_selected.get() == answer[self.q_selected]:
            return True
        else:
            self.risposte_sbagliate.append(self.q_selected)
            self.risposte_date.append(self.opt_selected.get())
    def next_btn(self):
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

            question_label.destroy()
            num_question.destroy()
            self.display_num_question()
            self.display_question()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui_quiz_base, text="Quiz Patente Nautica!", width=60, bg="blue", fg="white", font=("ariel", 20, "bold"))
        #title.place(x=0, y=0)
        title.pack(fill='x')
    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema[self.q_selected]
        num_question = Label(gui_quiz_base, text=f"Domanda {self.q_no+1} di {self.data_size} - {text_tema}",fg='red', font=("ariel", 15 ))
        num_question.pack()
    def display_question(self):
        global question_label
        text = question[self.q_selected]
        question_label = Label(gui_quiz_base, text=text, width=60, height=0,
                     font=('ariel', 18, 'bold'), anchor='w',wraplength=680,justify=LEFT,borderwidth=3)
        #question_label.place(x=30, y=55)
        question_label.pack(padx=20,pady=20)
        #question_label.pack(side=TOP,fill='x',expand=True, anchor=N)


    def quit_button_function(self):
        gui_quiz_base.destroy()
        lanch_menu()

    def buttons(self):
        next_button = Button(gui_quiz_base, text="Conferma", command = self.next_btn,
                             width=10,height=3, bg="white", fg="green", font=("ariel", 16, "bold"), relief=RAISED)
        #next_button.pack(expand=True)
        #next_button.pack(side=TOP,expand=True, anchor=N)
        next_button.place(relx= 0.5, y=620,anchor=S)

        quit_button = Button(gui_quiz_base, text="Torna al\nMenu", command=self.quit_button_function,
                             width=5, bg="red", fg="red", font=("ariel", 16, " bold"), relief=RAISED)
        quit_button.place(x=720 ,y=0)
    def show_image(self):
        global img
        img = 0
        if figure[self.q_selected] != 0:
            image = PIL.Image.open('Immagini Pieghevole/Im' + str(figure[self.q_selected]) + '.jpg')
            image = ImageOps.contain(image, (300, 230))
            canvas = Canvas(gui_quiz_base, width=image.size[0]+10, height=image.size[1]+10)
            img = ImageTk.PhotoImage(image, master = canvas)
            canvas.create_image(10,10, anchor=NW, image=img)
            #canvas.pack(side=TOP,fill='x',expand=True, anchor=CENTER)
            canvas.place(x=300,y=300)
        else:
           return None
    def radio_buttons(self):
        q_list = []
        y_pos = 160
        while len(q_list) < 3:
            radio_btn = Radiobutton(gui_quiz_base, text=" ", variable= self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14),anchor='w',wraplength=700,justify=LEFT)
            q_list.append(radio_btn)
            #radio_btn.pack(side=TOP,fill='x',anchor=E)
            radio_btn.place(x=30, y=y_pos)
            y_pos += 50
        return q_list
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[str(self.q_selected)]:
            self.opts[val]['text'] = option
            val += 1

def lanch_menu():
    # TODO scrivere codice fz lancia menu
    global menu
    global gui_menu_base
    try:
        gui_menu_1.destroy()
        gui_menu_base = Tk()
        height = 730
        width = 730
        left = (gui_menu_base.winfo_screenwidth() - width) / 2
        top = (gui_menu_base.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
        gui_menu_base.geometry(geometry)
        #gui_menu_base.resizable(False,False)
        gui_menu_base.title("Quiz Patente Nautica - Menu Quiz Base")
        gui_menu_base.configure(background='#b8e6fe')
        menu = Menu()
        gui_menu_base.mainloop()
    except:
        gui_menu_base = Tk()
        height = 730
        width = 730
        left = (gui_menu_base.winfo_screenwidth() - width) / 2
        top = (gui_menu_base.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
        gui_menu_base.geometry(geometry)
        #gui_menu_base.resizable(False,False)
        gui_menu_base.title("Quiz Patente Nautica - Menu Quiz Base")
        gui_menu_base.configure(background='#b8e6fe')
        menu = Menu()
        gui_menu_base.mainloop()

def lanch_Quiz(num, argo):## aggiungere tema
    global quiz
    global gui_quiz_base
    gui_quiz_base = Tk()
    height = 630
    width = 810
    left = (gui_quiz_base.winfo_screenwidth() - width) / 2
    top = (gui_quiz_base.winfo_screenheight() - height) / 2
    geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
    gui_quiz_base.geometry(geometry)
    # gui_menu_base.resizable(False,False)
    gui_quiz_base.title("Quiz Patente Nautica")

    quiz = Quiz(num,argo)
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
    geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
    gui_quiz_base.geometry(geometry)
    gui_quiz_base.resizable(False, False)
    gui_quiz_base.title("Quiz Patente Nautica")
    quiz_scheda_esame = Quiz_scheda_esame(genera_scheda_esame())
    gui_quiz_base.mainloop()
def lanch_quiz_domande_sbagliate():
    global Quiz_base_cerca
    global gui_quiz_base

    with open('saved.json','r') as file:
        data = json.load(file)
    index_domande_sbagliate = data['domande_salvate']

    if len(index_domande_sbagliate) == 0:
        mb.showwarning('Attenzione', 'Al momento non ci sono domande sbagliate in memoria.')
        pass

    else:
        gui_menu_base.destroy()
        gui_quiz_base = Tk()
        height = 630
        width = 810
        left = (gui_quiz_base.winfo_screenwidth() - width) / 2
        top = (gui_quiz_base.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
        gui_quiz_base.geometry(geometry)
        gui_quiz_base.resizable(False, False)
        gui_quiz_base.title("Quiz Patente Nautica")
        quiz_scheda_esame = Quiz_base_cerca(index_domande_sbagliate)
        gui_quiz_base.mainloop()

def lanch_base_cerca():
    global quiz
    global gui_quiz_base
    gui_quiz_base = Tk()
    height = 630
    width = 810
    left = (gui_quiz_base.winfo_screenwidth() - width) / 2
    top = (gui_quiz_base.winfo_screenheight() - height) / 2
    geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
    gui_quiz_base.geometry(geometry)
    gui_quiz_base.resizable(False, False)
    gui_quiz_base.title("Quesiti Vela")
    try:
        quiz = QuizBaseCerca(index_domande_base)
        gui_quiz_base.mainloop()
    except:
        mb.showinfo(title='Attenzione',message="Attenzione!\nParola Non Trovata")
        gui_quiz_base.destroy()
        lanch_menu()

###### Funzioni di salvataggio
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

    warning = mb.askyesno("Attenzione", "Attenzione!\nTutti i dati salvati andranno persi.\nSei sicuro di voler continuare?")
    if warning == True:
        with open('saved.json','w') as f:
            data = {}
            data['domande_salvate'] = list()
            json.dump(data,f)
        mb.showinfo('formattazione', 'Tutti i dati sono stati cancellati!')

    else:
        pass

## Menu Quiz Vela ##
class Menu_vela:
    def __init__(self):
        self.show_menu()
    def show_menu(self):
        ## Label

        messaggio_benvenuto = "Quiz Vela"
        benvenuto_label = Label(gui, text=messaggio_benvenuto,
                                font=('ariel', 18, 'bold'),
                                bg='#b8e6fe', fg='#778899', justify='center')
        benvenuto_label.pack(padx=50,pady=10, fill='x', expand=False)

        # Create Canvas
        canvas_1 = Canvas(gui, bg="#ffc0cb", bd=2, highlightthickness=0, relief='ridge')
        canvas_1.pack(pady=10, padx=50, fill='x', expand=False)
        canvas_2 = Canvas(gui, bg="#ffc0cb", bd=2, highlightthickness=0, relief='ridge')
        canvas_2.pack(pady=20, padx=50, fill='x', expand=False)
        canvas_3 = Canvas(gui, bg='#b8e6fe', bd=2, highlightthickness=0)
        canvas_3.pack(padx=50,  fill='x', expand=False,)

        ################# Canvas_1

        ## Widget Canvas_1
        label_domande_vela = Label(canvas_1,text='Numero Domande : ',font=('ariel', 16, 'bold'), bg='#ffc0cb')

        # SLIDER - Canvas 1
        global num_dom_vela
        num_dom_vela = IntVar(gui)
        slider_vela = Scale(canvas_1, from_=1, to=50, orient='horizontal', variable=num_dom_vela, cursor='boat',
                            width=30, length=300, bg='#ffc0cb')
        slider_label_vela = Label(canvas_1, text=' -- da 1 domanda a 50 domande --', font=("ariel", 10, " italic"),
                                  bg='#ffc0cb')

        # BUTTON - Canvas 1
        vela_button_1 = Button(canvas_1, text='Genera Scheda\nQuiz Vela', font=("ariel", 16, " bold"),
                             relief=RAISED, command=self.funz_vela_button_1, bg='black', fg='blue', height=4, width=13)

        # PLACE Widgets Canvas 1
        canvas_1.grid_columnconfigure((0, 1), weight=1)
        label_domande_vela.grid(row=1, column=0, padx=20, pady=19, sticky='e')
        slider_vela.grid(row=1, column=1, padx=20, pady=5, sticky='w')
        slider_label_vela.grid(row=3, column=1)
        vela_button_1.grid(columnspan=2, pady=5)

        ################# Canvas_2

        global entry_vela
        label_domande_vela = Label(canvas_2,
                                   text='Genera scheda\ncon ricerca avanzata',
                                   font=('ariel', 16, 'bold'), bg='#ffc0cb')

        def on_enter(e):
            entry_vela.delete(0, 'end')

        def on_leave(e):
            name = entry_vela.get()
            if name == '':
                entry_vela.insert(0, 'es. "randa", "tangone", ecc..' )

        entry_vela = Entry(canvas_2, font= ("ariel", 12, " italic"),width=30)
        entry_vela.insert(0, 'es. "randa", "tangone", ecc..')
        entry_vela.bind('<FocusIn>', on_enter)
        entry_vela.bind('<FocusOut>', on_leave)




        vela_button_2 = Button(canvas_2, text='Genera Scheda\ncon ricerca avanzata', font=("ariel", 16, " bold"),
                             relief=RAISED, command= self.funz_vela_button_2, bg='black', fg='green', height=4, width=13)

        # Canvas_2 place widgets
        canvas_2.grid_columnconfigure((0, 1), weight=1)
        label_domande_vela.grid(row=1, column=0, padx=40, pady=19)
        entry_vela.grid(row=1,column=1,padx=40, pady=5)
        vela_button_2.grid(columnspan=2, pady=5)

        # canvas_3 buttons

        global img_arrow
        img_arrow = PhotoImage(file='Images/return.png')
        return_menu_bottom = Button(canvas_3, text='Menu', font=("ariel", 10, " bold"), image=img_arrow, compound="top",
                                    relief=RAISED, command=lanch_menu_iniziale)

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
class Quiz_vela:
    def __init__(self,n_domande):
        self.q_no= 0
        self.data_size = n_domande #numero di domande per scheda
        self.correct = 0
        self.risposte_sbagliate = []
        self.q_selected = choice(question_vela.index)
        self.q_precedent_selected = []
        self.display_title()

        self.display_num_question()
        self.display_question()
        self.show_image()

        self.opt_selected = IntVar(gui)  # 1_Vero, 2_falso
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()


    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        if score > 80 :
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                #opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]] #[opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                #opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]]#[opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")

        gui.destroy()
        lanch_menu_vela()

    def check_ans(self, q_no):
        if (answer_vela[self.q_selected] == 'V' and self.opt_selected.get() == 1) | (answer_vela[self.q_selected] == 'F' and self.opt_selected.get() == 2):
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
            self.q_selected = temp_q_selection #randint(0,len(question)


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
        title = Label(gui, text="Quiz Vela!", width=60, bg="#ffc0cb", fg="white", font=("ariel", 20, "bold"))
        #title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema_vela[self.q_selected]

        num_question = Label(gui, text=f"Domanda {self.q_no+1} di {self.data_size} - {text_tema}",fg='red', font=("ariel", 15 ), )
        num_question.pack()

    def display_question(self):
        global question_label
        text = question_vela[self.q_selected]
        question_label = Label(gui, text=text, width=60, height=0,
                     font=('ariel', 18, 'bold'), anchor='w',wraplength=700,justify=LEFT,borderwidth=3)
        question_label.place(x=30, y=55)
        #question_label.pack(side=TOP,fill='x',expand=True, anchor=N)

    def quit_button_function(self):
        gui.destroy()
        lanch_menu_vela()

    def buttons(self):
        next_button = Button(gui, text="Conferma", command = self.next_btn,
                             width=10, height=3,bg="white", fg="green", font=("ariel", 16, "bold"), relief=RAISED)
        #next_button.pack(expand=True)
        #next_button.pack(side=TOP,expand=True, anchor=N)
        next_button.place(relx= 0.5, y=270,anchor=S)

        quit_button = Button(gui, text="Torna al\nMenu", command=self.quit_button_function,
                             width=5, bg="red", fg="red", font=("ariel", 16, " bold"), relief=RAISED)
        quit_button.place(x=720 ,y=0)

    def radio_buttons(self):
        q_list = []
        x_pos=320
        while len(q_list) < 2:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 18,),anchor='w',wraplength=700,justify=LEFT)
            q_list.append(radio_btn)
            #radio_btn.pack(side=TOP,fill='x',anchor=E)
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
            canvas = Canvas(gui, width=image.size[0]+10, height=image.size[1]+10)
            img = ImageTk.PhotoImage(image)
            canvas.create_image(10, 10, anchor=NW, image=img)
            canvas.place(x=300, y=300)

        else:
            return None
class Quiz_vela_cerca:
    def __init__(self,indice):
        self.q_no= 0
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

        self.opt_selected = IntVar(gui)  # 1_Vero, 2_falso
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Risposte Corrette: {self.correct}"
        wrong = f"Risposte Sbagliate: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        if score > 80 :
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nComplimenti!\nHai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                #opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]] #[opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")
        else:
            mb.showinfo("Result", f"Risultati:\n{correct}\n{wrong}\n\nPeccato!\nNon Hai superato la prova\n")
            for i in range(len(self.risposte_sbagliate)):
                #opzione_corretta = answer[self.risposte_sbagliate[i]]
                risposta_corretta = answer_vela[self.risposte_sbagliate[i]]#[opzione_corretta - 1]
                mb.showinfo("Risposte sbagliate", f"Domanda:\n{question_vela[self.risposte_sbagliate[i]]}\n\nRisposta corretta:\n{risposta_corretta}")
        gui.destroy()
        lanch_menu_vela()

    def check_ans(self, q_no):
        if (answer_vela[self.q_selected] == 'V' and self.opt_selected.get() == 1) | (answer_vela[self.q_selected] == 'F' and self.opt_selected.get() == 2):
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
                self.q_selected = temp_q_selection #randint(0,len(question)

            question_label.destroy()
            num_question.destroy()
            self.display_num_question()
            self.display_question()
            self.display_options()
            self.show_image()

    def display_title(self):
        title = Label(gui, text="Quiz Vela!", width=60, bg="#ffc0cb", fg="white", font=("ariel", 20, "bold"))
        #title.place(x=0, y=0)
        title.pack(fill='x')

    def display_num_question(self):
        global num_question
        global q_tema
        text_tema = tema_vela[self.q_selected]

        num_question = Label(gui, text=f" Trovate {self.data_size} domande! Domanda {self.q_no+1} - {text_tema}",fg='red', font=("ariel", 17 ))
        num_question.pack(padx=20)

    def display_question(self):
        global question_label
        text = question_vela[self.q_selected]
        question_label = Label(gui, text=text, width=60, height=0,
                     font=('ariel', 18, 'bold'), anchor='w',wraplength=700,justify=LEFT,borderwidth=3)
        question_label.place(x=40, y=55)
        #question_label.pack(side=TOP,fill='x',expand=True, anchor=N)
    def quit_button_function(self):
        gui.destroy()
        lanch_menu_vela()

    def buttons(self):
        next_button = Button(gui, text="Conferma", command = self.next_btn,
                             width=10, height=3,bg="white", fg="green", font=("ariel", 16, "bold"), relief=RAISED)
        #next_button.pack(expand=True)
        #next_button.pack(side=TOP,expand=True, anchor=N)
        next_button.place(relx= 0.5, y=250,anchor=S)

        quit_button = Button(gui, text="Torna al\nMenu", command=self.quit_button_function,
                             width=5, bg="red", fg="red", font=("ariel", 16, " bold"), relief=RAISED)
        quit_button.place(x=720,y=0)

    def radio_buttons(self):
        q_list = []
        x_pos= 0.45
        while len(q_list) < 2:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected, value=len(q_list) + 1, font=("ariel", 18,),anchor='w',wraplength=700,justify=LEFT)
            q_list.append(radio_btn)
            #radio_btn.pack(side=TOP,fill='x',anchor=E)
            radio_btn.place(relx=x_pos, y=150,anchor=CENTER)
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
            canvas = Canvas(gui, width=image.size[0]+10, height=image.size[1]+10)
            img = ImageTk.PhotoImage(image)
            canvas.create_image(10, 10, anchor=NW, image=img)
            canvas.place(x=300, y=300)

        else:
            return None

def lanch_menu_vela():  # TODO scrivere codice fz lancia menu
    global menu
    global gui
    try:
        gui_menu_1.destroy()
        gui = Tk()
        height = 650
        width = 700
        left = (gui.winfo_screenwidth() - width) / 2
        top = (gui.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
        gui.geometry(geometry)
            # menu.resizable(False,False)
        gui.title("Quiz Patente Nautica - Menu Vela")
        gui.configure(background='#b8e6fe')
        menu = Menu_vela()
        gui.mainloop()
    except:
        gui = Tk()
        height = 650
        width = 700
        left = (gui.winfo_screenwidth() - width) / 2
        top = (gui.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top)
        gui.geometry(geometry)
        gui.title("Quiz Patente Nautica - Menu Vela")
        gui.configure(background='#b8e6fe')
        menu = Menu_vela()
        gui.mainloop()
def lanch_quiz_vela(no_domande):
    global quiz_vela
    global gui
    try:
        gui.destroy()
    finally:
        gui = Tk()
        height = 650
        width = 820
        left = (gui.winfo_screenwidth() - width) / 2
        top = (gui.winfo_screenheight() - height) / 2
        geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
        gui.geometry(geometry)
        gui.resizable(False,False)
        gui.title("Quesiti Vela")
        quiz_vela = Quiz_vela(no_domande)
        gui.mainloop()
def lanch_quiz_vela_cerca():
        global quiz_vela
        global gui
        try:
            gui.destroy()
        finally:
            gui = Tk()
            height = 650
            width = 820
            left = (gui.winfo_screenwidth() - width) / 2
            top = (gui.winfo_screenheight() - height) / 2
            geometry = '%dx%d+%d+%d' % (width, height, left, top-50)
            gui.geometry(geometry)
            gui.resizable(False, False)
            gui.title("Quesiti Vela")
        try:
            quiz_vela = Quiz_vela_cerca(index_domande)
            gui.mainloop()
        except:
            mb.showinfo(title='Attenzione', message="Attenzione!\nParola Non Trovata!")
            gui.destroy()
            lanch_menu_vela()

Login()
#lanch_menu_iniziale()

