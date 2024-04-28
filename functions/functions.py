"""Defines functions for handling input and output in a tkinter GUI application.
- clear_input_output(input_text, output_text): Clears the content of input and output text widgets.
- show_error(message): Displays an error message dialog box with the given message.
- show_success(message): Displays a success message dialog box with the given message.
- save_to_file(output_text, file_entry): Saves the content of the output text widget to a file specified in the file entry widget."""
from tkinter import messagebox
from functions.file_handling import save_text_to_file
from functions.error_handling import show_error, show_success

def clear_input_output(input_text, output_text):
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

def show_error(message):
    messagebox.showerror("Error", message)

def show_success(message):
    messagebox.showinfo("Success", message)

def save_to_file(output_text, file_entry):
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
