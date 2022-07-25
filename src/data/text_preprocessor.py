"""
Authors: @pythonistabr / @PauloMarvin
project: Twitter Sentiment Analysis - Atlantico Bootcamp
"""

# from nltk.stem import WordNetLemmatizer
from pandas import read_csv
import string
import spacy
import nltk
import re

nlp = spacy.load("pt_core_news_sm");

class TextPreprocessor:
    
    def stemming(texto: str) -> str:
        stemmer = nltk.stem.RSLPStemmer()
        palavras = []
        palavras = [stemmer.stem(palavra) for palavra in texto.split()]
        return " ".join(palavras)

    def lemmatization(text: str) -> str:
        doc = nlp("".join(text))
        lemmas = [token.lemma_ for token in doc]
        return " ".join(lemmas)
    
    def remove_stop_words(text: str, stop_words: list) -> str:
        stopwords = nltk.corpus.stopwords.words("portuguese") #var local diminui a performance 
        # stopwords.extend(stop_words) #lista atualizada a partir da analise exploratória.
        text = " ".join(list(filter(lambda x: x not in stopwords, text.split())))
        return text


def main():
    # imports
    from pandas import read_csv
    
    # load data
    stop_words = read_csv("stopwords.txt")
    tweet = "o rato roeu a roupa de rei de roma"
    
    # processing
    no_stopwords_tweet = TextPreprocessor.remove_stop_words(tweet, stop_words);
    lemmatized_tweet = TextPreprocessor.lemmatization(tweet);
    stemming_tweet = TextPreprocessor.stemming(tweet);
    
    print(f"Raw Twett: {tweet}\n")
    print(f"Tweet without stopwords: {no_stopwords_tweet}\n")
    print(f"Lemmatization: {lemmatized_tweet}\n")
    print(f"Stemming: {stemming_tweet}\n")
    
if __name__ == "__main__":
    main()
    
    
