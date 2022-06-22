"""
Autores: 
Gustavo Viana - @pythonistabr
Paulo Marvin - @PauloMarvin

Data: 21-06-2022
"""

import nltk
from sklearn.feature_extraction.text import CountVectorizer


def stemming(texto: str) -> str:
    stemmer = nltk.stem.RSLPStemmer()
    palavras = []
    palavras = [stemmer.stem(palavra) for palavra in texto.split()]
    return " ".join(palavras)
    

def remover_stop_words(texto: str, stop_words: list) -> str:
    stopwords = nltk.corpus.stopwords.words("portuguese")
    stopwords.extend(stop_words)
    texto = " ".join(list(filter(lambda x: x not in stopwords, texto.split())))
    return texto
    
def get_top_ngram(corpus, gram_size=None, top_gram=10):
    vec = CountVectorizer(ngram_range=(gram_size, gram_size)).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:top_gram]
    
    
    
def main():
    #test
    print("Running")
    

if __name__ == "__main__":
    main()