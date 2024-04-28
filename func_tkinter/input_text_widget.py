import tkinter as tk

def create_input_text_widget(parent):
    input_text = tk.Text(parent, height=5, width=50)
    input_text.grid(row=0, column=1)
    return input_text