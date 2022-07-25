import streamlit as st
from streamlit_option_menu import option_menu
# from src.app import home, classificador, analise_exploratoria, analise_comparativa, sobre
from src.app import home, classificador, analise_exploratoria, analise_comparativa, sobre

#from src.data import tweets_downloader

#from st_on_hover_tabs import on_hover_tabs


#st.title("Análise de sentimentos em dados do Twitter")

with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ["Home", "Análise exploratória", "Análise comparativa", "Sobre"],
        icons=["house", "search", "book", "person"],
        menu_icon="cast",
        default_index=0

    )

if selected == "Home":
    home.page()
if selected == "Análise exploratória":
    analise_exploratoria.page()
if selected == "Análise comparativa":
    analise_comparativa.page()
if selected == "Sobre":
    sobre.page()


    