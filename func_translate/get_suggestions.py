"""Implements text translation and language suggestions using the Google Translate API.
- translate_text(text, target_language): Translates the given text to the specified target language using Google Translate.
- get_suggestions(entry_text): Provides language suggestions based on the entry text."""
from googletrans import LANGUAGES
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def get_suggestions(entry_text):
    return [lang for lang in LANGUAGES.values() if entry_text.lower() in lang.lower()]
