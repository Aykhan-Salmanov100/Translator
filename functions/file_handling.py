def save_text_to_file(filename, text):
    try:
        with open(filename, "w") as file:
            file.write(text)
        return True
    except Exception as e:
        print(f"Failed to save text: {str(e)}")
        return False
