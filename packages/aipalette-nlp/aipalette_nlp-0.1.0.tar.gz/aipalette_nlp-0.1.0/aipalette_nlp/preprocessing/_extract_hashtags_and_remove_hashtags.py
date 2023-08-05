import re
import unicodedata


def extract_hashtags_and_remove_hashtags(text):
    """get the list of hashtags, and get cleaned text after removing hashtags 

    Args:
        text(str) : input raw text
    Returns:
        hashtags_list(list) : list of all hashtags.
        cleaned_text(str) : cleaned text after removing hashtags
    """

    punctuation_ls = "!\"$%&'()*+,-/.:;<=>?[\]^`{|}~"
    hashtags_list = []
    temp_list = []
    counter = 0
    split_text = re.findall(r"\w+|#\w+|@\w+|[!\"$%&'()*+,-/.:;<=>?[\]^`{|}~]", text) # split based on punctuation and whitespace 
    clean_split_text = [elem for elem in split_text if elem not in punctuation_ls]
     
    for index,part in enumerate(clean_split_text):  
        if part.startswith('#'):   # hashtag is found  
            temp_list.append(part[1:])
            counter += 1
            # check if the word is the last word in the text
            if index == len(clean_split_text)-1:
                if counter>=3:
                    hashtags_list.extend(temp_list)
                    del clean_split_text[index-counter+1:index+1] 
                else:
                    break
            continue
            
        else:  # encounter a non-hashtag
            if counter >= 3:  # add hashtags from temp to hashtags_list  
                hashtags_list.extend(temp_list)
                del clean_split_text[index-counter+1:index+1]
                temp_list = []
                counter = 0
                continue
            else: # delete the hashtags from temp_list
                temp_list = []
                counter = 0
                continue
        
    cleaned_text = " ".join(clean_split_text)
    return hashtags_list, cleaned_text