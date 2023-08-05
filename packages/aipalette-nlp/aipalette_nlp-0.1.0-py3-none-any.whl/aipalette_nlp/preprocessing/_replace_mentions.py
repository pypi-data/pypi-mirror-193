import re

def replace_mentions(text):
    ''''''
    """function to detect mentions and replace it with keyword "username"

    Returns:
        str: cleaned text after removing all the mentions
    """
    cleanedText = re.sub(r"@[A-Za-z0-9]+","username",text)
    return cleanedText