

from func_tkinter.create_button_frame import create_button_frame
from func_tkinter.create_clear_button import create_clear_button
from func_tkinter.create_input_text import create_input_text
from func_tkinter.create_language_entry import create_language_entry
from func_tkinter.create_output_frame import create_output_frame
from func_tkinter.create_output_text import create_output_text
from func_tkinter.create_save_button import create_save_button
from func_tkinter.create_translate_button import create_translate_button


def setup_gui(root):
    root.title("Translator App")
    
    input_frame = create_output_frame(root)
    output_frame = create_output_frame(root)
    button_frame = create_button_frame(root)

    input_text = create_input_text(input_frame)
    language_entry = create_language_entry(input_frame)
    output_text = create_output_text(output_frame)

    create_translate_button(button_frame, input_text, language_entry, output_text)
    create_clear_button(button_frame, input_text, output_text)
    create_save_button(button_frame, output_text)
