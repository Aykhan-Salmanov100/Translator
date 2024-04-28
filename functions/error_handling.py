from tkinter import messagebox

def show_error(message):
    messagebox.showerror("Error", message)

def show_success(message):
    messagebox.showinfo("Success", message)
