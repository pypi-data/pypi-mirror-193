from nltk.tokenize import word_tokenize as nltk_word_tokenizer
from .pyarabic import tokenizer as arab_tokenizer
from somajo import SoMaJo
from janome.tokenizer import Tokenizer as jp_Tokenizer
from .pykotokenizer import ko_spacing
import jieba
from pythainlp.tokenize import word_tokenize as thai_tokenizer
from pyvi import ViTokenizer, ViPosTagger
from ..preprocessing import detect_language

from langcodes import *


tokenizer_languages_supported = ['english','french','german','italian','portuguese','spanish','swedish',
                       'turkish','russian','mandarin','thai','japanese','korean','vietnamese', 'arabic']

# use nltk word_tokenize
nltk_lang = ['english', 'french', 'italian', 'portuguese',
             'spanish', 'swedish', 'turkish', 'russian']

# use tokenizers from other packages
nonnltk_lang = ['mandarin', 'thai', 'japanese', 'korean', 'vietnamese','german', 'arabic']


def arabic_tokenizer(text):
    """

    Args:
        text (str): input Arabic text to tokenize

    Returns:
        list: list of tokens of the input text
    """
    return arab_tokenizer.tokenize(text)


def german_tokenizer(text):
    """

    Args:
        text (str): input German text to tokenize

    Returns:
        list: list of tokens of the input text
    """
    tokenizer = SoMaJo("de_CMC", split_camel_case=True)
    sentences = tokenizer.tokenize_text(text)
    tokenize_text = []
    for sentence in sentences:
        for token in sentence:
                tokenize_text.append(token)
    
    return tokenize_text

def japanese_tokenizer(text):
    """

    Args:
        text (str): input Japanese text to tokenize

    Returns:
        list: list of tokens of the input text
    """
    jt = jp_Tokenizer()
    return [token.node.surface for token in jt.tokenize(text)]


def korean_tokenizer(text):
    """

    Args:
        text (str): input Korean text to tokenize

    Returns:
        list: list of tokens of the input text
    """
    
    kt = ko_spacing.KoSpacing()
    return kt(text).replace('.','').split(' ')



def mandarin_tokenizer(text):
    """

    Args:
        text (str): input Mandarin text to tokenize

    Returns:
        list: list of tokens of the input text
    """
    tokenize_text = jieba.cut(text, cut_all=False)
    try:
        tokenize_text = [str(word) for word in tokenize_text]
    except Exception as e:
        # print(text)
        print(tokenize_text)
        raise e


def thai_tokenizer(text, engine="newmm"):
    """

    Args:
        text (_type_): _description_
        engine (str, optional): _description_. Defaults to "newmm".

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    # old code block
        # tt = Tokenizer(tok_func = ThaiTokenizer, lang = 'th', pre_rules = pre_rules_th, post_rules=post_rules_th)
        # tokenizer = TokenizeProcessor(tokenizer=tt, chunksize=10000, mark_fields=False)
        # tokenize_text = tokenizer.tokenizer.process_text(text, ThaiTokenizer)

    try:
        return thai_tokenizer(text, engine="newmm")
    except Exception as e:
        print("Exception occured while tokenizing Thai text : ")
        raise e
                

def vietnamese_tokenizer(text):
    """

    Args:
        text (str): input text to tokenize

    Returns:
        list: list of tokens of the input text
    """
    return ViPosTagger.postagging(ViTokenizer.tokenize(text))[0]


def word_tokenize(text):
    """ this is the main function to be called to tokenize the text

    Args:
        text (str): input text to tokenize
        language (str): language of the text

    Returns:
        list: list of tokens of the input text.
    """
    lang_code = detect_language(text)
    language = Language.make(language=lang_code).display_name().lower()

    tokenize_text = ''

    if language == 'mandarin':
        tokenize_text = mandarin_tokenizer(text)
            
    elif language == 'thai':
        tokenize_text = thai_tokenizer(text)
        
    elif language == 'japanese':
        tokenize_text = japanese_tokenizer(text)

    elif language == "korean":
        tokenize_text = korean_tokenizer(text)
        
    elif language == "vietnamese":
        tokenize_text = vietnamese_tokenizer(text)

    elif language == "german":
        tokenize_text = german_tokenizer(text)
                
    elif language == "arabic":
        tokenize_text = arabic_tokenizer(text)
        
    else:
        # for all other language which are handled by nltk
        try:
            tokenize_text = nltk_word_tokenizer(text)

        except Exception as e:
            print("Exception occured : language not supported by this package")
            raise e


    return {"tokenized_text":tokenize_text}