import nltk
from nltk.stem import WordNetLemmatizer 

#basic setup
nltk.download('wordnet')
nltk.download('punkt')



def lemmatizer(sentence):
    lemmatizer = WordNetLemmatizer()
    word_list = nltk.word_tokenize(sentence)
    lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
    return(lemmatized_output)