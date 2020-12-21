""" List of functions

https://www.geeksforgeeks.org/text-preprocessing-in-python-set-2/?ref=rp

https://www.geeksforgeeks.org/text-preprocessing-in-python-set-1/

https://www.kaggle.com/sudalairajkumar/getting-started-with-text-preprocessing#Spelling-Correction

https://towardsdatascience.com/nlp-text-preprocessing-a-practical-guide-and-template-d80874676e79

1. preprocess - Will have string arguement for the type of pre-processing to be done on the input

Will work for different input formats -> String, List of string, list of comma seperated words

Methods for removing each of type of contamination

Methods will return in the string format.

2. Process methods list

        1. Lowercase
        2. Uppercase
        3. Numbers_into_words
        4. Remove_numbers
        5. Remove punctuation
        6. Remove_extra_whitespace
        7. Remove_stopwords
    
        9. Stemming
        10. Lemmatization
        11. POS Tagging

        13. NER
        14. Remove Emoji
        15. Remove emoticons
        16. Emoticon_to_words
        17. Remove_URL
        18. Remove_html_tags
        19. Spell correction
    20. Remove_special_char
        21. Expand_contractions
        22. Convert_accented_string
    
        24. Remove_rare_words

"""
from collections import Counter
import nltk
import string
import re
from bs4 import BeautifulSoup
import spacy
import unidecode
from word2number import w2n
# from pycontractions import Contractions
import gensim.downloader as api
from nltk.tokenize import word_tokenize  
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer 
from emo_unicode import EMOTICONS
# cont = Contractions(kv_model=model)
# cont.load_models()
import inflect 
from spellchecker import SpellChecker
import en_core_web_sm


class Preprocess:

    def __init__(self, text):

        self.text = text
        self.STOPWORDS = set(stopwords.words('english'))
        self.spell = SpellChecker()
        self.p = inflect.engine()
        self.nlp = en_core_web_sm.load()
        #self.nlp = spacy.load('en_core_web_md')
        self.model = api.load("glove-twitter-25")
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    
    def strip_html_tags(self):

        """remove html tags from text"""
        soup = BeautifulSoup(self.text, "html.parser")
        stripped_text = soup.get_text(separator=" ")
        return stripped_text
    

    def remove_accented_chars(self):

        """remove accented characters from text, e.g. café"""
        text = unidecode.unidecode(self.text)
        return text

    
    '''def expand_contractions(self, text):
        """expand shortened words, e.g. don't to do not"""
        text = list(cont.expand_texts([text], precise=True))[0]
        return text'''
    

    def pos_tagging(self): 

        word_tokens = word_tokenize(self.text) 
        return pos_tag(word_tokens)

    
    def text_lowercase(self): 

        return self.text.lower()


    def text_uppercase(self): 

        return self.text.upper()

    
    def remove_numbers(self): 

        result = re.sub(r'\d+', '', self.text) 
        return result

    
    def convert_number(self): 

        # split string into list of words 
        temp_str = self.text.split() 
        # initialise empty list 
        new_string = [] 
    
        for word in temp_str: 
            # if word is a digit, convert the digit 
            # to numbers and append into the new_string list 
            if word.isdigit(): 
                temp = p.number_to_words(word) 
                new_string.append(temp) 
    
            # append the word as it is 
            else: 
                new_string.append(word) 
    
        # join the words of new_string to form a string 
        temp_str = ' '.join(new_string) 
        return temp_str
    

    def remove_punctuation(self): 

        translator = str.maketrans('', '', string.punctuation) 
        return self.text.translate(translator)

    
    def remove_whitespace(self): 

        return  " ".join(self.text.split()) 

    
    def remove_stopwords(self):

        """custom function to remove the stopwords"""
        return " ".join([word for word in str(self.text).split() if word not in self.STOPWORDS])

    
    def stem_words(self):

        return " ".join([self.stemmer.stem(word) for word in self.text.split()])


    def lemmatize_words(self):

        return " ".join([self.lemmatizer.lemmatize(word) for word in self.text.split()])

    
    def remove_freqwords(self, df, column_name):

        """custom function to remove the frequent words"""

        cnt = Counter()

        for self.text in df["text_wo_stop"].values:
            for word in self.text.split():
                cnt[word] += 1
        FREQWORDS = set([w for (w, wc) in cnt.most_common(10)])

        return " ".join([word for word in str(self.text).split() if word not in FREQWORDS])

    
    def remove_emoji(self):

        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', self.text)

    
    def remove_emoticons(self):

        emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in EMOTICONS) + u')')
        return emoticon_pattern.sub(r'', self.text)

    
    def convert_emoticons(self):

        for emot in EMOTICONS:
            text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), self.text)
        return text


    def remove_urls(self):

        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        return url_pattern.sub(r'', self.text)

    
    def remove_html(self):

        html_pattern = re.compile('<.*?>')
        return html_pattern.sub(r'', self.text)

    
    def correct_spellings(self):

        corrected_text = []
        misspelled_words = self.spell.unknown(self.text.split())

        for word in self.text.split():
            if word in misspelled_words:
                corrected_text.append(self.spell.correction(word))
            else:
                corrected_text.append(word)

        return " ".join(corrected_text)


    def NER(self):

        doc = self.nlp(self.text)
        entity_label_map = dict()

        for entity in doc.ents:
            entity_label_map[entity.self.text] = entity.label_
        
        return entity_label_map


prep =  Preprocess("My name is Praveen")
print(prep)