import re


def replace_phoneno(text):
    """ function to replace all the phone numbers with keyword "phone"

    Args:
        text (str): input raw text

    Returns:
        str: cleaned text after removing all phonenumbers
    """

    cleanedText = re.sub('(\+\d{1,2}[\s-])?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}', 'phone',text)
    cleanedText = re.sub('(\+?\d{1,2}[\s-])?\(?(\d{2})?\)?\d{9}\d?', "phone", cleanedText)
    cleanedText = re.sub(r'\(?(\d{2})?\)?\s?\d{9}\d?$', "phone", cleanedText)
    return cleanedText