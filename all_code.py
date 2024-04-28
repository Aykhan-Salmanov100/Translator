import tkinter as tk

from func_tkinter.input_text_widget import create_input_text_widget

def create_input_text(parent):
    input_text = create_input_text_widget(parent)
    input_label = tk.Label(parent, text="Enter text:")
    input_label.grid(row=0, column=0)
    return input_textimport tkinter as tk

def create_output_text(parent):
    output_text = tk.Text(parent, height=5, width=50)
    output_label = tk.Label(parent, text="Translated text:")
    output_label.grid(row=0, column=0)
    output_text.grid(row=0, column=1)
    return output_textfrom googletrans import Translator  # Importing the Translator module from googletrans library.

def translate_text(text, target_language):
    """
    Translates input text to the specified target language.
    
    Args:
        text (str): The text to be translated.
        target_language (str): The language code of the target language.
        
    Returns:
        str: The translated text.
    """
    translator = Translator()  # Creating a Translator object.
    translated_text = translator.translate(text, dest=target_language)  # Translating the input text.
    return translated_text.text  # Returning the translated text.
from tkinter import messagebox

def show_error(message):
    messagebox.showerror("Error", message)

def show_success(message):
    messagebox.showinfo("Success", message)
def save_text_to_file(filename, text):
    try:
        with open(filename, "w") as file:
            file.write(text)
        return True
    except Exception as e:
        print(f"Failed to save text: {str(e)}")
        return False
"""Defines functions for handling file saving and input/output clearing in the GUI application.
- save_to_file(output_text, file_entry='file'): Saves the content of the output text widget to a file specified in the file entry widget. If no file entry is provided, it defaults to 'file'. Shows success message upon successful saving, or error messages if there's no text to save or if the file saving fails.
- clear_input_output(input_text, output_text): Clears the content of the input and output text widgets."""
from functions.file_handling import save_text_to_file
from functions.error_handling import show_error, show_success

def save_to_file(output_text, file_entry='file'):
    """Save content of the output text widget to a file.
    
    Args:
        output_text (tk.Text): The output text widget containing the text to be saved.
        file_entry (tk.Entry, optional): The file entry widget where the filename is entered. Defaults to 'file'.
    """
    text_to_save = output_text.get("1.0", "end-1c")
    if text_to_save.strip():
        filename = file_entry.get()
        if filename.strip():
            if save_text_to_file(filename, text_to_save):
                show_success(f"Text saved to {filename} successfully.")
            else:
                show_error("Failed to save text.")
        else:
            show_error("Please enter a filename.")
    else:
        show_error("No text to save.")

def clear_input_output(input_text, output_text):
    """Clears the content of the input and output text widgets.
    
    Args:
        input_text (tk.Text): The input text widget.
        output_text (tk.Text): The output text widget.
    """
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
"""This script imports the tkinter module and a function called setup_gui from a module named func_tkinter.setup_gui.
It defines a main function which creates a Tkinter root window, calls setup_gui to set up the GUI elements, and starts the Tkinter event loop with mainloop().
Finally, it checks if the script is being run as the main program and if so, it calls the main function."""
import tkinter as tk
from func_tkinter.setup_gui import setup_gui

root = tk.Tk()
setup_gui(root)
root.mainloop()

