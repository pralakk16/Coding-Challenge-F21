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

### Steps towards Solution

### 1. Formatting Data

Since the Text Input (input.txt) is in an unstrucutred text format, I first formatted the data to provide a readable structure for the computer to process.

#### Steps of Formatting

##### 1. Tokenization, Parts of Speech, Stop Words

