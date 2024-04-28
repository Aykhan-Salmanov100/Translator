"""
This is a simple translator app built using Tkinter and the googletrans library.
It allows users to translate text from a source language to a target language.
The app also includes features like auto-complete for language selection,
language swapping, translation history saving and viewing, and input/output clearing.
"""

import tkinter as tk
from googletrans import LANGUAGES, Translator
from tkinter import messagebox
import os

# Function to update the autocomplete list
def update_autocomplete(event):
    """
    This function updates the autocomplete listbox with language suggestions
    based on the text entered in the language entry field.
    """
    entry_text = language_entry.get()
    suggestions = [lang for lang in LANGUAGES.values() if entry_text.lower() in lang.lower()]
    autocomplete_listbox.delete(0, tk.END)
    for suggestion in suggestions[:5]:  # Show only top 5 suggestions
        autocomplete_listbox.insert(tk.END, suggestion)

# Function to handle selection from autocomplete list
def on_select(event):
    """
    This function is called when a language is selected from the autocomplete listbox.
    It updates the language entry field and sets the target_language_var with the selected language.
    """
    selected_index = autocomplete_listbox.curselection()
    if selected_index:
        selected_language = autocomplete_listbox.get(selected_index)
        language_entry.delete(0, tk.END)
        language_entry.insert(tk.END, selected_language)
        target_language_var.set(selected_language)

# Function to swap translation languages
def swap_languages():
    """
    This function swaps the source and target languages by exchanging their values
    in the respective StringVars.
    """
    source_lang = source_language_var.get()
    target_lang = target_language_var.get()
    source_language_var.set(target_lang)
    target_language_var.set(source_lang)
    update_autocomplete(None)

# Function to create language entry with autocomplete
def create_language_entry(parent):
    """
    This function creates the language entry fields, autocomplete listbox,
    and other related widgets for selecting the source and target languages.
    """
    global language_entry, autocomplete_listbox, source_language_var, target_language_var

    source_language_var = tk.StringVar()
    target_language_var = tk.StringVar()

    language_frame = tk.Frame(parent)
    language_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

    source_language_label = tk.Label(language_frame, text="Source Language:")
    source_language_label.grid(row=0, column=0)
    source_language_dropdown = tk.OptionMenu(language_frame, source_language_var, *LANGUAGES.values())
    source_language_dropdown.grid(row=0, column=1)

    swap_button = tk.Button(language_frame, text="⇄", command=swap_languages)
    swap_button.grid(row=0, column=2)

    target_language_label = tk.Label(language_frame, text="Target Language:")
    target_language_label.grid(row=0, column=3)
    language_entry = tk.Entry(language_frame)
    language_entry.grid(row=0, column=4)

    autocomplete_listbox = tk.Listbox(language_frame, height=5)
    autocomplete_listbox.grid(row=1, column=4, sticky="ew")
    autocomplete_listbox.bind("<ButtonRelease-1>", on_select)

    language_entry.bind("<KeyRelease>", update_autocomplete)

    for lang in LANGUAGES.values():
        autocomplete_listbox.insert(tk.END, lang)

    source_language_var.set("English")
    target_language_var.set("")  # Change the default target language to an empty string

# Function to translate text
def translate():
    """
    This function translates the text from the input text widget
    using the selected source and target languages.
    It then displays the translated text in the output text widget.
    """
    input_text = input_text_widget.get("1.0", "end-1c")
    target_language = target_language_var.get()
    translator = Translator()
    translated = translator.translate(input_text, src=source_language_var.get(), dest=target_language)
    translated_text = translated.text

    output_text_widget.delete("1.0", "end")
    output_text_widget.insert("1.0", translated_text)

# Function to save translation history
def save_history():
    """
    This function saves the translation history for the current user.
    It creates a text file named after the user's username and appends
    the source language, target language, input text, and translated text.
    """
    input_text = input_text_widget.get("1.0", "end-1c")
    output_text = output_text_widget.get("1.0", "end-1c")
    source_language = source_language_var.get()
    target_language = target_language_var.get()

    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return

    history_folder = os.path.join(os.getcwd(), "translation_history")
    if not os.path.exists(history_folder):
        os.makedirs(history_folder)

    user_history_file = os.path.join(history_folder, f"{username}.txt")

    try:
        with open(user_history_file, "a") as file:
            file.write(f"Source Language: {source_language}\n")
            file.write(f"Target Language: {target_language}\n")
            file.write(f"Input Text: {input_text}\n")
            file.write(f"Translated Text: {output_text}\n\n")
        messagebox.showinfo("Success", "Translation history saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save translation history: {str(e)}")

# Function to show translation history
def show_history():
    """
    This function displays the translation history for the current user.
    It opens a new window and displays the contents of the user's history file.
    """
    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return

    history_folder = os.path.join(os.getcwd(), "translation_history")
    user_history_file = os.path.join(history_folder, f"{username}.txt")

    try:
        with open(user_history_file, "r") as file:
            history_text = file.read()
        history_window = tk.Toplevel(root)
        history_window.title(f"Translation History for {username}")
        history_text_widget = tk.Text(history_window, wrap=tk.WORD)
        history_text_widget.insert("1.0", history_text)
        history_text_widget.pack(padx=10, pady=10)
    except FileNotFoundError:
        messagebox.showerror("Error", "No translation history found for this username.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load translation history: {str(e)}")

# Function to clear input and output
def clear_input_output():
    """
    This function clears the text in both the input and output text widgets.
    """
    input_text_widget.delete("1.0", "end")
    output_text_widget.delete("1.0", "end")

# Create the main window
root = tk.Tk()
root.title("My Translator App")

# Create input text widget
input_text_widget = tk.Text(root, height=10, width=50)
input_text_widget.grid(row=0, column=0, padx=10, pady=10)

# Create output text widget
output_frame = tk.Frame(root)
output_frame.grid(row=0, column=1, padx=10, pady=10)

output_text_widget = tk.Text(output_frame, height=10, width=50)
output_text_widget.pack(side=tk.TOP, pady=10)

create_language_entry(root)

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.grid(row=2, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_input_output)
clear_button.grid(row=2, column=1, padx=10, pady=10)

username_label = tk.Label(root, text="Enter your username:")
username_label.grid(row=3, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=3, column=1, padx=10, pady=10)

save_history_button = tk.Button(root, text="Save History", command=save_history)
save_history_button.grid(row=4, column=0, padx=10, pady=10)

show_history_button = tk.Button(root, text="Show History", command=show_history)
show_history_button.grid(row=4, column=1, padx=10, pady=10)

"""
This is the main event loop that keeps the application running.
It listens for user interactions and updates the GUI accordingly.
"""
root.mainloop()