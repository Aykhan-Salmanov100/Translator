import tkinter as tk
from googletrans import LANGUAGES
from func_translate.get_suggestions import get_suggestions

# Function to update the autocomplete list
def update_autocomplete(event):
    entry_text = language_entry.get()
    suggestions = get_suggestions(entry_text)
    # Limit the number of suggestions shown
    autocomplete_listbox.delete(0, tk.END)
    for suggestion in suggestions[:5]:  # Show only top 5 suggestions
        autocomplete_listbox.insert(tk.END, suggestion)

# Function to handle selection from autocomplete list
def on_select(event):
    selected_index = autocomplete_listbox.curselection()
    if selected_index:
        selected_language = autocomplete_listbox.get(selected_index)
        language_entry.delete(0, tk.END)
        language_entry.insert(tk.END, selected_language)

# Function to create language entry with autocomplete
def create_language_entry(parent):
    global language_entry, autocomplete_listbox
    language_entry = tk.Entry(parent)
    language_label = tk.Label(parent, text="Target Language:")
    language_label.grid(row=1, column=0)
    language_entry.grid(row=1, column=1)

    # Autocomplete listbox
    autocomplete_listbox = tk.Listbox(parent, height=5)  # Set height to limit the size
    autocomplete_listbox.grid(row=2, column=1, sticky="ew")
    autocomplete_listbox.bind("<ButtonRelease-1>", on_select)

    # Update autocomplete list on key release
    language_entry.bind("<KeyRelease>", update_autocomplete)

    # Pre-load suggestions
    for lang in LANGUAGES.values():
        autocomplete_listbox.insert(tk.END, lang)

    return language_entry
