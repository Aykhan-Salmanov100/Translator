import tkinter as tk

def create_language_entry(parent):
    language_entry = tk.Entry(parent)
    language_label = tk.Label(parent, text="Target Language:")
    language_label.grid(row=1, column=0)
    language_entry.grid(row=1, column=1)
    return language_entry