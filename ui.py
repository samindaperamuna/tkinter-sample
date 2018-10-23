from tkinter import Frame, Menu, Button, LEFT, TOP, X, Label, SUNKEN, W, BOTTOM, Canvas, BOTH, ALL, PhotoImage


class MainWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master)

        # Create the main menu.
        menu = Menu(self)
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_item_click)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        draw_menu = Menu(menu)
        menu.add_cascade(label="Draw", menu=draw_menu)
        draw_menu.add_command(label="Line", command=self.draw_black_line)
        draw_menu.add_command(label="Circle", command=self.draw_black_circle)
        draw_menu.add_separator()
        draw_menu.add_command(label="Clear", command=self.clear_canvas)

        # Create the toolbar.
        toolbar = Frame(master, bg="blue")

        insert_btn = Button(toolbar, text="Insert Image", command=self.insert_btn_click)
        insert_btn.pack(side=LEFT, padx=2, pady=2)

        self.insert_img = PhotoImage(file="resources/insert.gif")
        insert_btn.config(image=self.insert_img, compound=LEFT)

        print_btn = Button(toolbar, text="Print", command=self.print_btn_click)
        print_btn.pack(side=LEFT, padx=2, pady=2)

        self.print_img = PhotoImage(file="resources/print.gif")
        print_btn.config(image=self.print_img, compound=LEFT)

        toolbar.pack(side=TOP, fill=X)

        # Canvas object.
        self._canvas = Canvas(master, bd=1, relief=SUNKEN)
        self._canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Create status bar.
        status = Label(master, text="Status.", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        self.pack()

    def draw_black_line(self):
        self._canvas.create_line(10, 10, 200, 50)

    def draw_black_circle(self):
        self._canvas.create_oval(100, 100, 200, 200)

    def clear_canvas(self):
        self._canvas.delete(ALL)

    @staticmethod
    def insert_btn_click():
        print("Insert button clicked.")

    @staticmethod
    def print_btn_click():
        print("Print button clicked.")

    @staticmethod
    def new_item_click():
        print("New item created.")
