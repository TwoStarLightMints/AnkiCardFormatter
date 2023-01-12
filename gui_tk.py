from tkinter import *
from tkinter import ttk as tk

_TITLE = "Anki Card Generator"

class AnkiCardGenGui:
    def __init__(self, root: Tk):
        root.title(_TITLE)

        mainframe = tk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        tk.Label(mainframe, text="Testing here").grid(column=0, row=0)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.mainloop()

AnkiCardGenGui(Tk())