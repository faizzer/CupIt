import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet

#basic setup
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def check_numb(word):
    out = True
    numb = {'1','2','3','4','5','6','7','8','9', '.', ',', '@', '\\', '/'}
    for i in word:
        if i in numb:
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
    lemmatizer = WordNetLemmatizer()
    pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if check_numb(word):
            if tag is None:
                # if there is no available tag, append the token as is
                lemmatized_sentence.append(word)
            else:       
                # else use the tag to lemmatize the token
                lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    lemmatized_sentence = " ".join(lemmatized_sentence)    
    return(lemmatized_sentence)
