"""Sets up the graphical user interface (GUI) for the Translator App.
- setup_gui(root): Creates and configures the main GUI components including input, output, and button frames, input and output text widgets, language entry widget, and save button.
- create_button_frame(root): Creates a frame to contain buttons.
- create_clear_button(parent, input_text, output_text): Creates a button to clear input and output text.
- create_input_text(parent): Creates an input text widget.
- create_output_frame(root): Creates a frame to contain output text.
- create_output_text(parent): Creates an output text widget.
- create_save_button(parent, output_text, file_entry): Creates a button to save output text to a file. Requires output text widget and file entry widget.
- create_translate_button(parent, input_text, language_entry, output_text): Creates a button to translate input text. Requires input text, language entry, and output text widgets.
- create_language_entry(parent): Creates a language entry widget.
"""
from func_tkinter.button_frame import create_button_frame
from func_tkinter.clear_button import create_clear_button
from func_tkinter.input_text import create_input_text
from func_tkinter.output_frame import create_output_frame
from func_tkinter.output_text import create_output_text
from func_tkinter.save_button import create_save_button
from func_tkinter.translate_button import create_translate_button
from func_tkinter.language_entry import create_language_entry

import tkinter as tk

def setup_gui(root):
    """Sets up the graphical user interface for the Translator App.
    
    Args:
        root (tk.Tk): The root window of the application.
    """
    root.title("Translator App")
    
    input_frame = create_output_frame(root)
    output_frame = create_output_frame(root)
    button_frame = create_button_frame(root)

    input_text = create_input_text(input_frame)
    language_entry = create_language_entry(input_frame)
    output_text = create_output_text(output_frame)

    # Directly create and assign the file entry widget
    file_entry = tk.Entry(button_frame)
    file_entry.grid(row=0, column=3, padx=10)  # Adjust the grid position as needed

    create_translate_button(button_frame, input_text, language_entry, output_text)
    create_clear_button(button_frame, input_text, output_text)
    create_save_button(button_frame, output_text, file_entry)  # Pass 'file_entry' as an argument
