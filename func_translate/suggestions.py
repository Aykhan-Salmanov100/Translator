from googletrans import LANGUAGES  # Importing the LANGUAGES dictionary from googletrans library.

def get_suggestions(entry_text):
    """
    Provides language suggestions based on the input text.
    
    Args:
        entry_text (str): The text used to search for language suggestions.
        
    Returns:
        list: A list of languages containing the input text.
    """
    return [lang for lang in LANGUAGES.values() if entry_text.lower() in lang.lower()]
    # Returning a list of languages containing the input text (case insensitive).
