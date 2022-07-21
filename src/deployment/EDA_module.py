"""
Autores: 
Gustavo Viana - @pythonistabr
Paulo Marvin - @PauloMarvin

Data: 21-06-2022
"""

from sklearn.feature_extraction.text import CountVectorizer
  
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