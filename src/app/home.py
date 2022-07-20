import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import snscrape.modules.twitter as sntwitter
import nltk
from wordcloud import WordCloud
from src.data import tweets_downloader as td
from src.data import data_cleaning_module as dc
import demoji
from joblib import load
from streamlit_tags import st_tags

twitter_number = 500
twitter_number_remaining = 200

def page():
    tags = st_tags(label="Pesquisa por hashtags")    
    use_date = st.checkbox("Limitar data", key="date", value=False)
    col1, col2 = st.columns(2)  
    start = col1.date_input("Data inicial", key="start", disabled=not(st.session_state["date"]))
    end = col2.date_input("Data final", key="end", disabled=not(st.session_state["date"]))  
    btn = st.button("Pesquisar")
    st.write(start)
    st.write(end)
    if btn:
        with st.spinner(f"Pesquisando tweets. Isso pode levar algum tempo..."):                
            lista = tags
            tweets = td.search(twitter_number, lista, start, end)
            if tweets:
                tweets_ordenados =  sorted(tweets, key=lambda row:row['pontuacao'], reverse=1 )
                tweets_ordenados = pd.DataFrame(tweets_ordenados)

                #Remover tweets com menos de 5 palavas
                tweets_ordenados = tweets_ordenados.assign(
                    number_words=tweets_ordenados.tweet.apply(lambda x: len(x.split(" "))),
                )

                formated_tweets_ordenados = tweets_ordenados.drop(
                    tweets_ordenados[tweets_ordenados.number_words < 5].index
                ) 

                formated_tweets_ordenados.drop(["number_words"], axis=1, inplace=True)

                # Gerar lista de tweets com maior pontuação
                list_tweets = list(formated_tweets_ordenados["tweet"])                         
                list_tweets_10 = list_tweets[0:10]

                #Préprocessamento de +200
                #Aplicação de funções para remover links, nomes de usuários dos tweets e caracteres especiais.
                formated_tweets_ordenados["tweet"] = formated_tweets_ordenados["tweet"].apply(
                    lambda tweet: dc.formatar_texto(texto=tweet))
                formated_tweets_ordenados["tweet"] = formated_tweets_ordenados["tweet"].apply(
                    lambda tweet: dc.limpa_texto(tweet))
                formated_tweets_ordenados["tweet"] = formated_tweets_ordenados["tweet"].apply(
                    lambda tweet: demoji.replace(tweet, "")); # custoso


                #Remoção das stopwords e aplicação de stemming.
                nltk.download("rslp")
                stopwords = pd.read_csv("data/processed/stopwords.txt")
                df_with_stopwords = formated_tweets_ordenados.copy()
                df_with_stopwords["tweet"] = df_with_stopwords["tweet"].apply(
                    lambda tweet: dc.remover_stop_words(tweet, stopwords)
                )

                df_steamed_with_stopwords = formated_tweets_ordenados.copy()
                df_steamed_with_stopwords["tweet"] = df_with_stopwords["tweet"].apply(
                    lambda tweet: dc.stemming(texto=tweet)
                )

                # criação do corpus
                corpus = " ".join(df_with_stopwords.tweet)
                for tag in tags:
                    corpus = corpus.replace(tag, "")

                #Selecionar os 200 tweets com maior pontuação
                list_tweets = list(df_steamed_with_stopwords["tweet"])   
                list_tweets_200 = list_tweets[0:twitter_number_remaining]
                preditor = load("src/app/best_modelv3.joblib") 
                predicao = preditor.predict_proba(list_tweets_200)[:,0]

                lista_predita = []
                for pred in predicao:
                    if pred >= 0.6:
                        lista_predita.append(0)
                    elif pred <= 0.4:
                        lista_predita.append(1)
                    else:
                        lista_predita.append(2)

                classes = ['negativo', 'positivo', 'neutro']
                fig = plt.figure(figsize=(5, 2))
                plt.barh(
                    classes,
                    [lista_predita.count(0)/twitter_number_remaining*100, 
                     lista_predita.count(1)/twitter_number_remaining*100, 
                     lista_predita.count(2)/twitter_number_remaining*100]
                )
                plt.xlabel("Percentual (%)")
                plt.ylabel("Rótulos")
                plt.xlim([0, 100])
                st.markdown("#### Predição")
                st.pyplot(fig)
                st.markdown('''
                Explicar como é feita a predição.
                Os percentuais [...]

                Para mais informações acesse [texto](http:/google.com).
                ''')

                list_tweets = list(formated_tweets_ordenados["tweet"])          
                list_tweets_amos = list_tweets[0:twitter_number_remaining]
                amostra = list(zip(list_tweets_amos,lista_predita))
                df = pd.DataFrame(amostra, columns=['tweet','predição'])
                wordcloud = WordCloud(background_color="white").generate(corpus)
                fig = plt.figure(figsize=(14, 10))
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")

                with st.expander("Nuvem de palavras"):
                    st.pyplot(fig)
                    st.markdown('''
                    A nuvem de palavras [...]

                    Para mais informações acesse [texto](http:/google.com).
                    ''')

                with st.expander("Tweets mais relevantes"):
                    for tweet in list_tweets_10:
                        st.write(tweet.rstrip())
                        st.markdown("<hr />", unsafe_allow_html = True)
            else:
                st.error("Não conseguimos encontrar nenhum tweet para esta palavra chave.")
                