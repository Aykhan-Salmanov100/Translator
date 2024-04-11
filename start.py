import tkinter as tk

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

    root.mainloop()

if __name__ == "__main__":
    main()
