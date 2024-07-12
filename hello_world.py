import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('New Window')

# Define event handlers
def click_event():
    button.config(text='Pressed button')


button = ttk.Button(window, text='Button', command=click_event)
button.grid(row=1, column=4, sticky='W')
window.mainloop()
