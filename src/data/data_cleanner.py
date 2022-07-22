"""
Authors: @pythonistabr / @PauloMarvin
project: Twitter Sentiment Analysis - Atlantico Bootcamp
"""

import string
import spacy
import nltk
import re

class DataCleanner:
    
    def remove_special_chars(text: str) -> str:
        chars = re.escape(string.punctuation)
        clean_text = re.sub(r'['+chars+']','', text)
        return clean_text
    
    def text_cleanning(string):
        words = string.split()
        words = [word for word in words if ("@" not in word) and ("http" not in word)]
        return " ".join(words)
    
    def format_text(text: str) -> str:
        text = (
            re.sub(r"(http\S+)|(@\w+)", "", text)  # remove links, usuários #
            .replace(".", "")
            .replace(";", "")
            .replace("—", ""))

        text = re.sub(r"(  +)", " ", text)  # remove espaços duplos
        text = text.lower().strip()

        return text
    

def main():
        
    # Tests
    raw_string = "@NeroImperador o rato roeu a roupa do rei de roma"
    formated_string = DataCleanner.format_text(raw_string) #remove links, usuarios etc
    string_no_special_chars = DataCleanner.remove_special_chars(raw_string)
    string_no_users = DataCleanner.text_cleanning(raw_string)
    
    print(f"texto sem formastação -> {raw_string}\n")
    print(f"texto sem caracteres especiais -> {string_no_special_chars}\n")
    print(f"texto sem menção de usuarios -> {string_no_users}\n")
    
    print("fim do teste")

if __name__ == '__main__':
    main()
