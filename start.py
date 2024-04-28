"""This script imports the tkinter module and a function called setup_gui from a module named func_tkinter.setup_gui.
It defines a main function which creates a Tkinter root window, calls setup_gui to set up the GUI elements, and starts the Tkinter event loop with mainloop().
Finally, it checks if the script is being run as the main program and if so, it calls the main function."""
import tkinter as tk
from func_tkinter.setup_gui import setup_gui

root = tk.Tk()
setup_gui(root)
root.mainloop()

