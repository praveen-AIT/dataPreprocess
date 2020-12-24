# dataPreprocess 0.2.7

Use this library to get an out of the box solution for all text pre-processing related problems. 
A wide range of text processing methods have been added to this library and I will keep on adding more methods.
The use of this library is very simple and intuitive and makes it very easy to clean the data for your NLP/NLU/Machine learning pipelines.

Pre-requiste steps to be completed before use:

- Download the nltk stopwords with the following command on your python interpreter:

```python
>>> nltk.download('stopwords')
```

- Install spacy en_core_web_sm with the following command on your machine's terminal:

```bash
$ python3 -m spacy download en
```

- Install pathlib package with the command:

```bash
$ pip install pathlib
```

- Make sure that the python version is 3.x and above


Sample demonstration of some of the methods in the library:

```python
>>> from dataPreprocess.preprocess import Preprocess
>>> text = "<br> This is   the firt     line. And this    is the 23   secodn lie. </br>"
>>> Data_preprocessor = Preprocess()
>>> clean_text = Data_preprocessor.strip_html_tags(text)
>>> clean_text = Data_preprocessor.text_lowercase(clean_text)
>>> clean_text = Data_preprocessor.correct_spellings(clean_text)
>>> clean_text = Data_preprocessor.remove_stopwords(clean_text)
>>> clean_text = Data_preprocessor.remove_whitespace(clean_text)
>>> clean_text = Data_preprocessor.remove_numbers(clean_text)
```

As demonstrated above, the methods of the library can be used in series without any hassle. It also takes out the headache of matching
the input format requirements of various libraries that are otherwise available online by different contributers.
PS: I have written the code from scratch and not copy pasted the code of the other contributers.

Note that despite supporting various functions, this library is very fast. That means that this adding this library to your production
pipeline will not hold you back at all ;)

Right now this library supports 21 different functions to clean your text right out of the box.
The list of functions is as follows:

1. text_lowercase
2. text_uppercase
3. remove_numbers
4. remove_punctuation
5. remove_whitespace
6. remove_stopwords
7. stem_words
8. lemmatize_words
9. pos_tagging
10. NER
11. remove_emoji
12. remove_emoticons
13. emoticon_to_words
14. remove_urls
15. remove_html
16. correct_spellings
17. Remove_special_char
18. Expand_contractions
19. remove_accented_chars
20. convert_number_towords
21. remove_freqwords

The functionalities of the methods listed above is pretty self-explanatory

This library is still in development phase and I will keep adding more and more functions to it other than just text cleaning.
