# Function to clear input and output
def clear_input_output(input_text_widget, output_text_widget):
    """
    This function clears the text in both the input and output text widgets.
    """
    input_text_widget.delete("1.0", "end")
    output_text_widget.delete("1.0", "end")