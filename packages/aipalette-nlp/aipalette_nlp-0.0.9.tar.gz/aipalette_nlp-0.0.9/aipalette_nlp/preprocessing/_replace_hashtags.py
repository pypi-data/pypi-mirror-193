import re

def replace_hashtags(text):
    """ remove the hashtags'#' within the main caption

    Args:
        text (str): input raw text

    Returns:
        str: cleaned text after removing "#"'s
    """
    text = text.replace("#","")
    return text