

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
