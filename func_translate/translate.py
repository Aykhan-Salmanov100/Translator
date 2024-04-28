from googletrans import Translator  # Importing the Translator module from googletrans library.

def translate_text(text, target_language):
    """
    Translates input text to the specified target language.
    
    Args:
        text (str): The text to be translated.
        target_language (str): The language code of the target language.
        
    Returns:
        str: The translated text.
    """
    translator = Translator()  # Creating a Translator object.
    translated_text = translator.translate(text, dest=target_language)  # Translating the input text.
    return translated_text.text  # Returning the translated text.
