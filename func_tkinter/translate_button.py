from func_translate.translate import translate_text
import tkinter as tk


def create_translate_button(parent, input_text, language_entry, output_text):
    def translate():
        translated_text = translate_text(input_text.get("1.0", "end-1c"), language_entry.get())
        output_text.delete("1.0", "end")
        output_text.insert("1.0", translated_text)
    translate_button = tk.Button(parent, text="Translate", command=translate)
    translate_button.grid(row=0, column=0, padx=10)