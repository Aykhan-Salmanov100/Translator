import tkinter as tk
from turtle import clear

def main():
    root = tk.Tk()
    root.title("Translator App")

    # Input Frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="Enter text:")
    input_label.grid(row=0, column=0)

    global input_text
    input_text = create_input_text_widget(input_frame)

    language_label = tk.Label(input_frame, text="Target Language:")
    language_label.grid(row=1, column=0)

    global language_entry
    language_entry = tk.Entry(input_frame)
    language_entry.grid(row=1, column=1)

    # Output Frame
    output_frame = tk.Frame(root)
    output_frame.pack(pady=10)

    output_label = tk.Label(output_frame, text="Translated text:")
    output_label.grid(row=0, column=0)

    global output_text
    output_text = tk.Text(output_frame, height=5, width=50)
    output_text.grid(row=0, column=1)

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    translate_button = tk.Button(button_frame, text="Translate", command=translate)
    translate_button.grid(row=0, column=0, padx=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear)
    clear_button.grid(row=0, column=1, padx=10)

    save_button = tk.Button(button_frame, text="Save to File", command=save_to_file)
    save_button.grid(row=0, column=2, padx=10)

    file_label = tk.Label(button_frame, text="File Name:")
    file_label.grid(row=1, column=0)

    global file_entry
    file_entry = tk.Entry(button_frame)
    file_entry.grid(row=1, column=1, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
