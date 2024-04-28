# Function to swap translation languages
def swap_languages(source_language_var, target_language_var, update_autocomplete):
    """
    This function swaps the source and target languages by exchanging their values
    in the respective StringVars.
    """
    source_lang = source_language_var.get()
    target_lang = target_language_var.get()
    source_language_var.set(target_lang)
    target_language_var.set(source_lang)
    update_autocomplete(None)