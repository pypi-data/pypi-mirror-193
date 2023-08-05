import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
    
def remove_stopwords(text, language="english"):
    """ remove stopwords from the text

    Args:
        text (str): input raw text
        language (str): language on input text

    Returns:
        str: cleaned text after removing stopwords
    """
    try:
        stopwords_set = set(stopwords.words(language)) # get set of stopwords of particular language from nltk's corpus
        filtered_words = [word.lower() for word in text.split() if word.lower() not in stopwords_set]
        text = " ".join(filtered_words)
        return text

    except OSError as e:
        print("exception : ", e)
        print("Language stopwords database not found! Stopwords not removed.")
        return " ".join(text.split())