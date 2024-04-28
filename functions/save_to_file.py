from functions.file_handling import save_text_to_file
from functions.error_handling import show_error, show_success

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

def clear_input_output(input_text, output_text):
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

