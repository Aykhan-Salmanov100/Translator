from googletrans import LANGUAGES

def get_suggestions(entry_text):
    return [lang for lang in LANGUAGES.values() if entry_text.lower() in lang.lower()]
