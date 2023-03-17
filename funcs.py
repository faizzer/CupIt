import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
import re
import string
import unicodedata
from itertools import filterfalse
import conf

#basic setup
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

STOPWORDS = conf.STOPWORDS

# most encounter issue check
freq = {'i','be','he','she','me','it','s','ll','t','d', 're', 'm','ve'}

def checking(word):
    out = True
    stop = {'1','2','3','4','5','6','7','8','9','.',',','@','\\','/',':','(', ')','\'','\"','`',
           '!','?','#','$','%','^','&','|','<','>','{','}','[','[',']',':',';','-','_',}
    for i in word:
        if i in stop:
            out = False
            break
    return out

def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:         
        return None

def lemmatizer_func(sentence):
    
    # intitial removing of comon words
    sentence = " ".join(filterfalse(lambda x: x in STOPWORDS, sentence.split()))
    
    lemmatizer = WordNetLemmatizer()
    pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        #check for invalid words with symbols
        if checking(word) and word not in freq:
            if tag is None:
                # if there is no available tag, append the token as is
                lemmatized_sentence.append(word)
            else:       
                # else use the tag to lemmatize the token
                lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    lemmatized_sentence = " ".join(lemmatized_sentence)    
    return(lemmatized_sentence)

def text_preprocessing(sentence):
    #print(f'Processing row {index}')
    # convert to all text into lower case
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-zA-Z0-9]', ' ', sentence)
    # replace abbreviations
    #sentence = re.sub(r'(\b)([A-Z])', r'\1 \2', sentence)

    # remove accents
    sentence = ''.join(c for c in unicodedata.normalize('NFD', sentence)
                       if unicodedata.category(c) != 'Mn')

    # remove website links
    sentence = sentence.replace("https://", "").replace("http://", "")

    # remove usernames
    sentence = sentence.replace("@", "")

    # remove punctuation marks
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    # remove stop words
    sentence = " ".join(filterfalse(lambda x: x in STOPWORDS, sentence.split()))


    # remove tabs
    sentence = sentence.translate(str.maketrans("", "", "\t"))

    # remove new lines
    sentence = sentence.translate(str.maketrans("", "", "\n"))

    # remove extra spaces
    #sentence = " ".join([word for word in sentence.split() if not word.isspace()])
    
    # Replace abbreviations
    #sentence = sentence.replace("u", "you").replace("r", "are").replace("thx", "thanks")
    
    # lemmatize the words
    lemmatizer = WordNetLemmatizer()
    sentence = " ".join([lemmatizer.lemmatize(word) for word in sentence.split()])
    
    
    return sentence
