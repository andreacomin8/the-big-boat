class GuiPage:
    def __init__(self, tk_object, width, height, title, background, resizable=None, header_data_obj=None,
                 page_elements=None):
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
            header_data_obj : dict
                e.g. {label: Label, pack_params: dict}.
            page_elements : list of PageElement
                list of elements and positions to fill the page
                e.g. [{canvas: {}, pack_params: {}}].
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
        self.header_data_obj = header_data_obj
        self.page_elements = page_elements

    '''
        header_data_obj = {label: header_label, pack_params: {padx: 50, pady: 10, fill='x', expand=False}}

        page_elements = [
            {
                "canvas":{
                    "tk_obj",
                    "bg":"#b8e6fe",
                    "bd":2,
                    "highlightthickness":0,
                    "relief":"ridge"
                },
                "pack_params":{
                    "padx":50,
                    "pady":10,
                    "fill":"x",
                    "expand":false
                }
            },
            {}
        ]
    '''

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

        # place label
        self.header_data_obj['label'].pack(**self.header_data_obj['pack_params'])
        # place elements
        for canvas_obj in self.page_elements:
            canvas_obj['canvas'].pack(**canvas_obj['pack_params'])
        self.tk_object.mainloop()
