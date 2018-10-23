from tkinter import Tk
from tkinter.ttk import Style

from screen_utils import center_window
from ui import MainWindow

if __name__ == "__main__":
    root = Tk()
    root.title('Sample Application Tk')
    root.geometry('640x480')

    center_window(root)

    window = MainWindow(root)

    root.mainloop()
