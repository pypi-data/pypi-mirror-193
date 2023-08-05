
import langid

def detect_language(text):
    """ get the languauge code (ISO 639-1) of the text

    Args:
        text (str): raw input text

    Returns:
        str: language code of the input text
    """
    lang_id = langid.classify(text)
    
    return lang_id[0]