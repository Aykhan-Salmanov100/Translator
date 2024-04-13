import tkinter as tk

def create_output_text(parent):
    output_text = tk.Text(parent, height=5, width=50)
    output_label = tk.Label(parent, text="Translated text:")
    output_label.grid(row=0, column=0)
    output_text.grid(row=0, column=1)
    return output_text