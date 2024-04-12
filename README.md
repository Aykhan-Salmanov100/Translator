# Translator App

## Description
This is a simple translator application built using Python and Tkinter. It allows users to enter text, select a target language, and translate the text into the chosen language. Additionally, users can save the translated text to a file.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Aykhan-Salmanov100/Translator.git
   ```
2. Navigate to the project directory:
   ```
   cd translator-app
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python start.py
   ```
2. Enter the text you want to translate in the input field.
3. Specify the target language in the provided entry field.
4. Click the "Translate" button to see the translated text.
5. Optionally, click the "Clear" button to clear the input and output fields.
6. To save the translated text to a file, click the "Save to File" button and enter the desired file name.

## Project Structure
- `func_tkinter/`: Contains functions and GUI elements related to Tkinter.
  - `create_button_frame.py`: Function for creating the button frame.
  - `create_clear_button.py`: Function for creating the clear button.
  - `create_input_text_widget.py`: Function for creating the input text widget.
  - `create_input_text.py`: Function for creating the input text.
  - `create_language_entry.py`: Function for creating the language entry.
  - `create_output_frame.py`: Function for creating the output frame.
  - `create_output_text.py`: Function for creating the output text.
  - `create_save_button.py`: Function for creating the save button.
  - `create_translate_button.py`: Function for creating the translate button.
  - `setup_gui.py`: Function for setting up the GUI layout.
- `func_translate/`: Contains translation functions.
  - `save_to_file.py`: Function for saving text to a file.
  - `translate.py`: Function for translating text.
- `functions/`: Contains general-purpose functions.
  - `clear_input_output.py`: Function for clearing input and output fields.
  - `error_handling.py`: Function for error handling.
  - `file_handling.py`: Function for file handling.