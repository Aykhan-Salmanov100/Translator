import tkinter as tk


def create_clear_button(parent, input_text, output_text):
    clear_button = tk.Button(parent, text="Clear", command=lambda: clear_input_output(input_text, output_text))
    clear_button.grid(row=0, column=1, padx=10)