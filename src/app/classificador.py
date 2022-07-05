from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st
from annotated_text import annotated_text
import joblib


# model = joblib.load('models/best_model.joblib') # carregar modelo

def get_most_liked_tweets(hashtag):
    fake_text = [
        f"{hashtag} é muito bom",
        f"Eu não gosto de {hashtag}",
        f"Isso é muito ruim {hashtag}",
        f"fazer {hashtag} é muito bom"
    ]
    return fake_text

# carregar lista de hashtags mais faladas
def get_most_popular_hashtags():
    hashtags = ['#stranger-things', '#COVID19', '#tbt', '#love']
    return hashtags

def page():
    st.title('Análise de sentimentos de redes sociais')
    options = st.multiselect(
        'Quais hashtags você quer identificar o sentimento?',
        get_most_popular_hashtags()
    )
    st.subheader('Análise de sentimentos')
    for hashtag in options:
        st.markdown(f'### `{hashtag}`')
        st.write(f'Lista dos 10 tweets mais curtidos sobre `{hashtag}`.')
        # pegar lista de 10 twittes mais curtidos
        textos = get_most_liked_tweets(hashtag)
        for texto in textos:
            # st.write(texto)
            col1, col2 = st.columns(2)
            with col1:
                annotated_text(
                    "Este ",
                    ("#love", "+"),
                    " é ",
                    ("muito", "-"),
                    ("ruim", "-"),
                    "."
                )
            with col2:
                annotated_text(
                    "Resultado: ",
                    ("positivo", "+")
                )
        st.markdown('#### Resumo')
        classes = ['negativo', 'neutro', 'positivo']
        fig = plt.figure(figsize=(5, 2))
        plt.barh(
            classes,
            [80, 15, 5]
        )
        plt.xlim([0, 100])
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig)
        with col2:
            st.info(f'A hashtag {hashtag} é majoritariamente negativa.')
        
        