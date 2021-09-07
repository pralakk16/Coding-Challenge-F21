from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from textblob import TextBlob


text = open('input.txt', encoding='utf-8').read()

pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
def tokenize_pos_stopwords(text):
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)
    newlist = []
    for word, tag in tags:
        if word.lower() not in set(stopwords.words('english')):
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist

wordnet_lemmatizer = WordNetLemmatizer()
def lemmatizer(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos: 
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:  
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    return lemma_rew

def getSubjectivity(lemmatized_text):
    return TextBlob(lemmatized_text).sentiment.subjectivity

def getPolarity(lemmatized_text):
    return TextBlob(lemmatized_text).sentiment.polarity

def sentiment_analysis(score):
    if score < 0:
        return 'Negative Sentiment'
    elif score == 0:
        return 'Neutral Sentiment'
    else:
        return 'Positive'

def calculate(text):
    pos_data = tokenize_pos_stopwords(text)
    lemmatized_text = lemmatizer(pos_data)
    subjectivity = getSubjectivity(lemmatized_text)
    polarity = getPolarity(lemmatized_text)
    return subjectivity, polarity

print("Polarity of Text: ", calculate(text)[1])
print("Subjectivity of Text: ", calculate(text)[0])
print("Sentiment of Text: ", sentiment_analysis(calculate(text)[1]))
    


