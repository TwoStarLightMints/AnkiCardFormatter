from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

_TITLE = "Anki Card Generator"

class AnkiCardGenGui:
    def __init__(self, root: Tk):
        root.title(_TITLE)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Testing here").grid(column=0, row=1)
        ttk.Label(mainframe, text="Testing here").grid(column=1, row=0)
        ttk.Label(mainframe, text="Testing here").grid(column=1, row=1)
        ttk.Button(mainframe, text="Load File").grid(column=0, row=0)
        
        inside_frame = ttk.Frame(mainframe, padding="3 3 12 12", relief="sunken")
        inside_frame.grid(columnspan=2, row=2)
        inside_frame.columnconfigure(0, weight=1)
        inside_frame.rowconfigure(0, weight=1)
        ttk.Label(inside_frame, text="Hello").grid(column=0, row=0)
        tree = ttk.Treeview(inside_frame, columns=("Card", "Another thing"))
        tree.column('Card', width=100, anchor='center')
        tree.heading('Card', text='Card')

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        for child in inside_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.mainloop()

AnkiCardGenGui(Tk())