import tkinter as tk

from functions.save_to_file import save_to_file

def create_save_button(parent, output_text, file_entry):
    save_button = tk.Button(parent, text="Save to File", command=lambda: save_to_file(output_text, file_entry))
    save_button.grid(row=0, column=2, padx=10)
