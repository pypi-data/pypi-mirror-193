import unicodedata


def fix_fonts(text):
    """ For normalizing the fonts

    Args:
        text (str): input raw text

    Returns:
        str: text with font fixed
    """
    text = unicodedata.normalize('NFKC', text)
    return text