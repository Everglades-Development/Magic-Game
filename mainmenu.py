import sys
import tkinter as tk
from tkinter import ttk


def quit():
    root.destroy()

root = tk.Tk()
root.geometry('1280x720')
root.title('magic game')
root.option_add("*tearOff", False)


root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)


root.tk.call('source', 'Components\\theme\\azure-dark.tcl')
ttk.Style().theme_use('azure-dark')

quitBtn = ttk.Button(root, text='quit', style="AccentButton", command=lambda: quit())
quitBtn.grid(row=6, column=0, padx=50, pady=100, sticky="nsew")
quitBtn.place(x=20, y=20)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

root.mainloop()