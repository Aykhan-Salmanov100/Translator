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
