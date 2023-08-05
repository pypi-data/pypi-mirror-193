import re

def replace_url(text):
    """ function to detect urls and replace it with keyword "url"

    Returns:
        str: cleaned text after removing all the urls
    """
    cleanedText = re.sub(r'\b(https?|ftp|file)://\S+', 'url ', text)
    return cleanedText