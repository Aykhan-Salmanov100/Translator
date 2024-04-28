import tkinter as tk

from func_tkinter.input_text_widget import create_input_text_widget

def create_input_text(parent):
    input_text = create_input_text_widget(parent)
    input_label = tk.Label(parent, text="Enter text:")
    input_label.grid(row=0, column=0)
    return input_text