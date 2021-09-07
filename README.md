# ACM Research Coding Challenge (Fall 2021)


## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Solution

### Libraries/Packages/API's Used

I have used the following libraries for this Coding Challenge:

1. NLTK
2. TextBlob

### Steps
### 1. Formatting Data

Since the Text Input (input.txt) is in an unstrucutred text format, I first formatted the data to provide a readable structure for the computer to process.

#### Tokenization, Parts of Speech, Stop Words
 
The first step to format the data is to Tokenize the text for Machine Readability. This can be seen in the following function:
After the Tokenization process we must figure out the unnecessary words, and the parts of speech. This entire process can be viewed in the following function:

```python
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
def tokenize_pos_stopwords(text):
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)
    newlist = []
    for word, tag in tags:
        if word.lower() not in set(stopwords.words('english')):
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist
```

#### Lemmetization

The second step is to Lemmetize the formatted text in the previous step. 
Lemmetization is used to find the stem words in each of the words. There are two major formating techniques: Stemmation and Lemmetization. 
Stemmation is a fast and quick approach, but unfortunately provides many drawbacks, accuracy as the main drawback. 
Lemmetization provides a more slower method, but fortunately provides a very accured stem/root word result.

The Lemmetization process can be seen in this function:

```python
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
```
### 2. The Sentiment Analysis

For the Sentiment Analysis, I have divided the seniment into two categories: Subjectivity and Polarity:

**Subjectivity** provides a statistic describing how Factual or Opioniated the Text is.

Subjectivity is measured from 0.0 - 1.0

If it is closer to 0 it is less subjective, if it is closer to 1.0, than it is more factual

For Subjectivitity I have implemented the following function:
```python
def getSubjectivity(lemmatized_text):
    return TextBlob(lemmatized_text).sentiment.subjectivity
```

**Polarity** is the real **Sentiment Analysis**, as in,  is the connotation of this text: Positive, Negative, or Neutral.

Polarity is measured on a scale from -1.0 to +1.0

If the Polarity Score is closer to -1.0 than the text has a **negative** connotation, but if the Polarity Score is closer to +1.0 than the text has a **positive** connotation, if 0.0 than it is **neutral**

The Polarity is calculated in the following function:
```python
def getPolarity(lemmatized_text):
    return TextBlob(lemmatized_text).sentiment.polarity
```



### Final Answer

## Subjectivity Score: 0.6080615942028986

# Overall Sentiment Analysis Score: 0.274909420289855
# Sentiment Analysis: Positive

# Conclusion

Since the Overall Sentiment Analaysis Score, which is the polarity score, is **greater** than 0 it means the overall text has a **Positive** connotation

Thank you for the fun challenge!

#### Citations

https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk


   

