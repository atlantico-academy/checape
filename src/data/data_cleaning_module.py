"""
Autores: 
Gustavo Viana - @pythonistabr
Paulo Marvin - @PauloMarvin

Data: 21-06-2022
"""

from datetime import timezone, timedelta
from pandas import to_datetime
import nltk
import re


def limpa_texto(string):
  words = string.split()
  words = [word for word in words if ("@" not in word) and ("http" not in word)]
  return " ".join(words)


def formatar_texto(texto: str) -> str:
  texto = (
    re.sub(r"(http\S+)|(@\w+)", "", texto)  # remove links, usuários #
    .replace(".", "")
    .replace(";", "")
    .replace("—", "")
  )

  texto = re.sub(r"(  +)", " ", texto)  # remove espaços duplos
  texto = texto.lower().strip()

  return texto
  

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

  
def get_period(hour):
  if hour >= 0 and hour < 6:
    return "overnight"
  elif hour >= 6 and hour < 12:
    return "morning"
  elif hour >= 12 and hour < 18:
    return "afternoon"
  elif hour >= 18 and hour < 24:
    return "night"
    

def from_utc_to_local_time(london_time: str, london_reference: int):
  london_time = to_datetime(london_time) # str para datetime
  local_time = london_time + timedelta(hours = london_reference)
  return local_time



def main():
  # test
  print("Running")

if __name__ == "__main__":
  main()