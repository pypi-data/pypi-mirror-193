from ._extract_hashtags_and_remove_hashtags import extract_hashtags_and_remove_hashtags
from ._fix_fonts import fix_fonts
from ._remove_stopwords import remove_stopwords
from ._replace_hashtags import replace_hashtags
from ._replace_url import replace_url
from ._replace_mentions import replace_mentions
from ._replace_phonenumber import replace_phoneno



def clean_text(text, language="english", is_remove_stopwords = True, is_replace_url=True, is_replace_usernames=True, is_replace_phonenumber=True, is_replace_hashtags=True):

    """  get cleaned data, with custom cleaning options. 

    Args:
        text (str): input raw text
        language (str, optional): Langauge of the text. Defaults to "en".
        is_remove_stopwords (bool, optional): flag to remove stopwords from the text . Defaults to True.
        is_replace_url (bool, optional): flag to replace all url's with keyword "url". Defaults to True.
        is_replace_usernames (bool, optional): flag to replace all usernames with the keyword "username". Defaults to True.
        is_replace_phonenumber (bool, optional): flag to replace phonenumber with the keyword "phone". Defaults to True.
        is_replace_hashtags (bool, optional): flag to remove all "#" (hashes) from text. Defaults to True.

    Returns:
        dict : format -> {"hashtags" : hashtags, "cleaned_text" : cleaned_text, "text_length" : text_len}
        hashtags (list) : list of hashtags from the text, which came 3 continuosly
        cleaned_text(str) : cleaned text
        text_len(int): length of cleaned text 
    """

    # Remove irrelevant components of text
    hashtags,text = extract_hashtags_and_remove_hashtags(text)

    if is_replace_hashtags :
        text = replace_hashtags(text)
    
    if is_replace_usernames:
        text = replace_mentions(text)
    
    if is_replace_phonenumber:
        text = replace_phoneno(text)
    
    if is_replace_url:
        text = replace_url(text)

    if is_remove_stopwords:
        text = remove_stopwords(text,language)
    
    
    text = fix_fonts(text)
    cleaned_text = text.lower()
    text_len = len(cleaned_text)

    return {"hashtags" : hashtags, "cleaned_text" : cleaned_text, "text_length" : text_len}