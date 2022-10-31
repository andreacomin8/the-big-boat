from tkinter import *

class GuiPage:
    def __init__(self, tk_object, width, height, title, background, side=None, resizable=None):

        """
            Parameters
            ----------
            width : int
                value for width.
            height : int
                value for height.
            title : str
                page title.
            background : str
                background colour.
            resizable : tuple
               not required, allow resize page sides
               e.g. (False, False).
        """

        self.tk_object = tk_object
        # params to set page shape and position
        left, top = self.calculate_left_top(tk_object, width, height)
        self.geometry = '%dx%d+%d+%d' % (width, height, left, top - 50)
        self.resizable = resizable
        self.title = title
        self.background = background
        # components to fill the page
        self.side = side


    @staticmethod
    def calculate_left_top(tk, width, height):
        left = (tk.winfo_screenwidth() - width) / 2
        top = (tk.winfo_screenheight() - height) / 2
        return left, top

    def show_page(self):
        # setup page size, shape and background
        self.tk_object.geometry(self.geometry)
        if self.resizable:
            self.tk_object.resizable(self.resizable)
        self.tk_object.title(self.title)
        self.tk_object.configure(background=self.background)
        self.tk_object.mainloop()

    def back_button(self, page_transitor):
        global img_back
        img_back = PhotoImage(file='Images/back_button.png')
        quit_button = Button(self.tk_object, command=page_transitor, text="Torna al Menu",
                             font=("ariel", 12, " bold"), image=img_back, compound="top" ,height=95)
        quit_button.place(relx=1, rely=0, anchor='ne')
