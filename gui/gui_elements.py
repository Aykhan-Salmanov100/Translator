import tkinter as tk

def create_input_text_widget(parent):
    input_text = tk.Text(parent, height=5, width=50)
    input_text.grid(row=0, column=1)
    return input_text

import tkinter as tk
from functions.clear_input_output import clear_input_output
from gui.gui_elements import create_input_text_widget
from func_translate.translation_function import translate_text
from functions.file_function import save_to_file

def setup_gui(root):
    root.title("Translator App")
    
    input_frame = create_input_frame(root)
    output_frame = create_output_frame(root)
    button_frame = create_button_frame(root)

    input_text = create_input_text(input_frame)
    language_entry = create_language_entry(input_frame)
    output_text = create_output_text(output_frame)

    create_translate_button(button_frame, input_text, language_entry, output_text)
    create_clear_button(button_frame, input_text, output_text)
    create_save_button(button_frame, output_text)

def create_input_frame(root):
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    return input_frame

def create_output_frame(root):
    output_frame = tk.Frame(root)
    output_frame.pack(pady=10)
    return output_frame

def create_button_frame(root):
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    return button_frame

def create_input_text(parent):
    input_text = create_input_text_widget(parent)
    input_label = tk.Label(parent, text="Enter text:")
    input_label.grid(row=0, column=0)
    return input_text

def create_language_entry(parent):
    language_entry = tk.Entry(parent)
    language_label = tk.Label(parent, text="Target Language:")
    language_label.grid(row=1, column=0)
    language_entry.grid(row=1, column=1)
    return language_entry

def create_output_text(parent):
    output_text = tk.Text(parent, height=5, width=50)
    output_label = tk.Label(parent, text="Translated text:")
    output_label.grid(row=0, column=0)
    output_text.grid(row=0, column=1)
    return output_text

def create_translate_button(parent, input_text, language_entry, output_text):
    def translate():
        translated_text = translate_text(input_text.get("1.0", "end-1c"), language_entry.get())
        output_text.delete("1.0", "end")
        output_text.insert("1.0", translated_text)
    translate_button = tk.Button(parent, text="Translate", command=translate)
    translate_button.grid(row=0, column=0, padx=10)

def create_clear_button(parent, input_text, output_text):
    clear_button = tk.Button(parent, text="Clear", command=lambda: clear_input_output(input_text, output_text))
    clear_button.grid(row=0, column=1, padx=10)

def create_save_button(parent, output_text):
    save_button = tk.Button(parent, text="Save to File", command=lambda: save_to_file(output_text.get("1.0", "end-1c")))
    save_button.grid(row=0, column=2, padx=10)
