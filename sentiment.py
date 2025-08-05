from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt_tab', quiet=True)

url = input("Enter the URL: ")

try:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    text = article.summary
    print("Article Summary:\n", text)

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(f"Sentiment Polarity: {sentiment} ({'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'})")
except Exception as e:
    print(f"An error occurred: {e}")

#For Text File:
# with open('sentiment.txt', 'r') as f:
#     text = f.read()